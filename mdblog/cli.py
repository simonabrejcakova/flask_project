from mdblog.factory import create_flask_app
from mdblog.models import db
from mdblog.models import User

flask_app, celery_app = create_flask_app()

## CLI COMMAND
def init_db(app):
    with app.app_context():
        db.create_all()
        print("database inicialized")
