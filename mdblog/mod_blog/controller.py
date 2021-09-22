from flask import Blueprint
from flask import render_template
from flask import request

from mdblog.models import Article
from mdblog.models import Manual
from mdblog.models import Location

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
    page = request.args.get("page", 1, type=int)
    paginate = Manual.query.order_by(Manual.id.desc()).paginate(page, 5, False)
    return render_template("mod_blog/manuals.jinja",
            manuals=paginate.items,
            paginate=paginate)

@blog.route("/manuals/<int:man_id>/")
def view_manual(man_id):
    manual = Manual.query.filter_by(id=man_id).first()
    if manual:
        return render_template("mod_blog/manual.jinja", manual=manual)
    return render_template("mod_blog/manual_not_found.jinja", man_id=man_id)


@blog.route("/locations/", methods=["GET"])
def view_locations():
    page = request.args.get("page", 1, type=int)
    paginate = Location.query.order_by(Location.id.desc()).paginate(page, 5, False)
    return render_template("mod_blog/locations.jinja",
            locations=paginate.items,
            paginate=paginate)

@blog.route("/locations/<int:loc_id>/")
def view_location(loc_id):
    location = Location.query.filter_by(id=loc_id).first()
    if location:
        return render_template("mod_blog/location.jinja", location=location)
    return render_template("mod_blog/location_not_found.jinja", loc_id=loc_id)
    