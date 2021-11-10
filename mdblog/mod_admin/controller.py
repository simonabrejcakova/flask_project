from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import flash
from werkzeug.security import generate_password_hash

from mdblog.models import db
from mdblog.models import Location
from mdblog.models import Article
from mdblog.models import User

from .forms import ArticleForm
from .forms import LocationForm
from .forms import ChangePasswordForm
from .forms import LoginForm
from .forms import NewUserForm

from .utils import login_required, login_required1

from mdblog.tasks import notify_newsletter

admin = Blueprint("admin", __name__)


#MAIN ADMIN
@admin.route("/admin")
@login_required
def view_admin():
    return render_template("mod_admin/admin.jinja")

#LOGIN 
@admin.route("/login/", methods=["GET"])
def view_login():
    login_form = LoginForm()
    return render_template("mod_admin/login.jinja", form=login_form)



#ARTICLES a newsletter

@admin.route("/articles/new/", methods=["GET"])
@login_required
def view_add_article():
    form = ArticleForm()
    return render_template("mod_admin/article_editor.jinja", form=form)

@admin.route("/articles/", methods=["POST"])
@login_required
def add_article():
    add_form = ArticleForm(request.form)
    if add_form.validate():
        new_article = Article(
                title = add_form.title.data,
                content = add_form.content.data,
                html_render = add_form.html_render.data)
        db.session.add(new_article)
        db.session.commit()
        flash("Article was saved", "alert-success")

        article_url = url_for("blog.view_article", art_id = new_article.id)
        article_url = request.url_root + article_url[1:]
        notify_newsletter.delay(article_url)
      


        return redirect(url_for("blog.view_articles"))
    else:
        for error in add_form.errors:
            flash("{} is required".format(error), "alert-danger")
        return render_template("mod_admin/article_editor.jinja", form=add_form)


@admin.route("/articles/<int:art_id>/edit/", methods=["GET"])
@login_required
def view_article_editor(art_id):
    article = Article.query.filter_by(id=art_id).first()
    if article:
        form = ArticleForm()
        form.title.data = article.title
        form.content.data = article.content
        return render_template("mod_admin/article_editor.jinja", form=form, article=article)
    return render_template("mod_blog/article_not_found.jinja", art_id=art_id)


@admin.route("/articles/<int:art_id>/", methods=["POST"])
@login_required
def edit_article(art_id):
    article = Article.query.filter_by(id=art_id).first()
    if article:
        edit_form = ArticleForm(request.form)
        if edit_form.validate():
            article.title = edit_form.title.data
            article.content = edit_form.content.data
            article.html_render = edit_form.html_render.data
            db.session.add(article)
            db.session.commit()
            flash("Edit saved", "alert-success")
            return redirect(url_for("blog.view_article", art_id=art_id))
        else:
            for error in login_form.errors:
                flash("{} is missing".format(error), "alert-danger")
            return redirect(url_for("admin.view_login"))



#LOGIN,ChangePassword,Logout
@admin.route("/login/", methods=["POST"])
def login_user():
    login_form = LoginForm(request.form)
    if login_form.validate():
        user = User.query.filter_by(username = login_form.username.data).first()
        if user and user.check_password(login_form.password.data) and user.id==1:
            session["logged"] = user.username
            flash("Login successful", "alert-success")
            return redirect(url_for("admin.view_admin"))
        elif user and user.check_password(login_form.password.data) and user.id!=1:
            session["ahoj"]=user.username
            flash("Login user successful", "alert-success")
            return redirect(url_for("blog.view_articles"))
        else:
            flash("Invalid credentials", "alert-danger")
            return render_template("mod_admin/login.jinja", form=login_form)
    else:
        for error in login_form.errors:
            flash("{} is missing".format(error), "alert-danger")
        return redirect(url_for("main.view_welcome_page"))


@admin.route("/changepassword/", methods=["GET"])
@login_required
def view_change_password():
    form = ChangePasswordForm()
    return render_template("mod_admin/change_password.jinja", form=form)

@admin.route("/changepassword/", methods=["POST"])
@login_required
def change_password():
    form = ChangePasswordForm(request.form)
    if form.validate():
        user = User.query.filter_by(username = session["logged"]).first()
        if user and user.check_password(form.old_password.data):
            user.set_password(form.new_password.data)
            db.session.add(user)
            db.session.commit()
            flash("Password changed!", "alert-success")
            return redirect(url_for("admin.view_admin"))
        else:
            flash("Invalid credentials", "alert-danger")
            return render_template("mod_admin/change_password.jinja", form=form)
    else:
        for error in form.errors:
            flash("{} is missing".format(error), "alert-danger")
        return render_template("mod_admin/change_password.jinja", form=form)




@admin.route("/changepasswordahoj/", methods=["GET"])
@login_required1
def view_change_password_ahoj():
    form = ChangePasswordForm()
    return render_template("mod_admin/change_password_ahoj.jinja", form=form)




@admin.route("/changepasswordahoj/", methods=["POST"])
@login_required1
def change_password_ahoj():
    form = ChangePasswordForm(request.form)
    if form.validate():
        user = User.query.filter_by(username = session["ahoj"]).first()
        if user and user.check_password(form.old_password.data):
            user.set_password(form.new_password.data)
            db.session.add(user)
            db.session.commit()
            flash("Password changed!", "alert-success")
            return redirect(url_for("main.view_welcome_page"))
        else:
            flash("Invalid credentials", "alert-danger")
            return render_template("mod_admin/change_password_ahoj.jinja", form=form)
    else:
        for error in form.errors:
            flash("{} is missing".format(error), "alert-danger")
        return render_template("mod_admin/change_password_ahoj.jinja", form=form)




@admin.route("/newuser", methods=["GET", "POST"])
@login_required
def new_user():
    form=NewUserForm(request.form)
    if request.method== "POST" and form.validate():
        hashed_password = generate_password_hash(form.password.data, method="sha256")
        
        new_user= User(
            username = form.username.data,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()
        flash("User created", "alert-success")
        return redirect(url_for("admin.view_admin"))
        
    else:
        return render_template("mod_admin/new_user.jinja", form=form)


@admin.route("/logout/", methods=["POST"])
@login_required
def logout_user():
    session.pop("logged") 
    flash("Logout successful", "alert-success")
    return redirect(url_for("main.view_welcome_page"))


@admin.route("/logoutahoj/", methods=["POST"])
@login_required1
def logout_user_ahoj():
    session.pop("ahoj") 
    flash("Logout successful", "alert-success")
    return redirect(url_for("main.view_welcome_page"))




#jednotlive odkazy na edit na hlavnej admin stranke



@admin.route("/viewarticles")
@login_required
def view_article():
    page=request.args.get("page", 1, type=int)
    paginate = Article.query.order_by(Article.id.desc()).paginate(
            page, 10, False)
    return render_template("mod_admin/view_article.jinja",
            articles=paginate.items,
            paginate=paginate)


@admin.route("/viewlocations")
@login_required
def view_location():
    page=request.args.get("page", 1, type=int)
    paginate = Location.query.order_by(Location.id.desc()).paginate(
            page, 10, False)
    return render_template("mod_admin/view_location.jinja",
            locations=paginate.items,
            paginate=paginate)

    
@admin.route("/vysledky/")
@login_required
def view_google_sheets():
    return render_template("mod_admin/google_sheets.jinja")
    




#LOCATION

@admin.route("/locations/new/", methods=["GET"])
@login_required
def view_add_location():
    form = LocationForm()
    return render_template("mod_admin/location_editor.jinja", form=form)

@admin.route("/locations/", methods=["POST"])
@login_required
def add_location():
    add_form = LocationForm(request.form)
    if add_form.validate():
        new_location = Location(
                title = add_form.title.data,
                content = add_form.content.data,
                html_render = add_form.html_render.data)
        db.session.add(new_location)
        db.session.commit()
        flash("Location was saved", "alert-success")


        return redirect(url_for("blog.view_locations"))
    else:
        for error in add_form.errors:
            flash("{} is required".format(error), "alert-danger")
        return render_template("mod_admin/location_editor.jinja", form=add_form)


@admin.route("/locations/<int:loc_id>/edit/", methods=["GET"])
@login_required
def view_location_editor(loc_id):
    location = Location.query.filter_by(id=loc_id).first()
    if location:
        form = LocationForm()
        form.title.data = location.title
        form.content.data = location.content
        return render_template("mod_admin/location_editor.jinja", form=form, location=location)
    return render_template("mod_blog/location_not_found.jinja", loc_id=loc_id)


@admin.route("/locations/<int:loc_id>/", methods=["POST"])
@login_required
def edit_location(loc_id):
    location = Location.query.filter_by(id=loc_id).first()
    if location:
        edit_form = LocationForm(request.form)
        if edit_form.validate():
            location.title = edit_form.title.data
            location.content = edit_form.content.data
            location.html_render = edit_form.html_render.data
            db.session.add(location)
            db.session.commit()
            flash("Edit saved", "alert-success")
            return redirect(url_for("blog.view_location", loc_id=loc_id))
        else:
            for error in login_form.errors:
                flash("{} is missing".format(error), "alert-danger")
            return redirect(url_for("admin.view_login"))




#delete button



@admin.route("/deletelocation/<int:loc_id>/")
@login_required
def delete_location(loc_id):
    location = Location.query.filter_by(id=loc_id).first()
    try:
        db.session.delete(location)
        db.session.commit()
        flash("Location deleted", "alert-success")
        return redirect(url_for("admin.view_location"))
    
    except:
        return render_template("errors/500.jinja")




@admin.route("/deletearticle/<int:art_id>/")
@login_required
def delete_article(art_id):
    article = Article.query.filter_by(id=art_id).first()
    try:
        db.session.delete(article)
        db.session.commit()
        flash("Article deleted", "alert-success")
        return redirect(url_for("admin.view_article"))
    
    except:
        return render_template("errors/500.jinja")


