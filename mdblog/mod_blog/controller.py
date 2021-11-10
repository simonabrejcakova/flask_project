from flask import Blueprint
from flask import render_template
from flask import request


from mdblog.models import Article
from mdblog.models import Manual
from mdblog.models import Location
from mdblog.models import User




blog = Blueprint("blog", __name__)





@blog.route("/articles/", methods=["GET"])
def view_articles():
    page = request.args.get("page", 1, type=int)
    paginate = Article.query.order_by(Article.id.desc()).paginate(page, 5, False)
    return render_template("mod_blog/articles.jinja",
            articles=paginate.items,
            paginate=paginate)

@blog.route("/articles/<int:art_id>/")
def view_article(art_id):
    article = Article.query.filter_by(id=art_id).first()
    if article:
        return render_template("mod_blog/article.jinja", article=article)
    return render_template("mod_blog/article_not_found.jinja", art_id=art_id)
    

@blog.route("/manuals/", methods=["GET"])
def view_manuals():
    return render_template("mod_blog/manuals.jinja")

    
@blog.route("/manuals/barista/")
def view_manual_barista():
    return render_template("mod_blog/barista.jinja",)

@blog.route("/manuals/prisluha/")
def view_manual_prisluha():
    return render_template("mod_blog/prisluha.jinja",)

@blog.route("/manuals/flyboy/")
def view_manual_flyboy():
    return render_template("mod_blog/flyboy.jinja",)


@blog.route("/locations/", methods=["GET"])
def view_locations():
    page = request.args.get("page", 1, type=int)
    paginate = Location.query.order_by(Location.id.desc()).paginate(page, 10, False)
    return render_template("mod_blog/locations.jinja",
            locations=paginate.items,
            paginate=paginate)

@blog.route("/locations/<int:loc_id>/")
def view_location(loc_id):
    location = Location.query.filter_by(id=loc_id).first()
    if location:
        return render_template("mod_blog/location.jinja", location=location)
    return render_template("mod_blog/location_not_found.jinja", loc_id=loc_id)
    
@blog.route("/techsupport/")
def view_techsupport():
    return render_template("mod_blog/techsupport_form.jinja")
    
@blog.route("/mlynky/")
def view_mlynky():
    return render_template("mod_blog/mlynky.jinja")

@blog.route("/kontakty/")
def view_contact():
    return render_template("mod_blog/contact.jinja")

@blog.route("/kalendar/")
def view_calendar():
    return render_template("mod_blog/calendar.jinja")