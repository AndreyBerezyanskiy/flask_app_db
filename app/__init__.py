import os
from dotenv import load_dotenv

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


load_dotenv()


app = Flask(__name__)


login_manager = LoginManager()
db = SQLAlchemy()
migration = Migrate()


def create_app(environment="development"):
    from config import config
    from app.views import auth_blueprint, home_blueprint, user_blueprint, todo_blueprint
    from app.models import User, AnonymousUser

    app = Flask(__name__)

    # Set app config
    env = os.environ.get("APP_ENV", environment)
    configuration = config(env)
    app.config.from_object(configuration)

    db.init_app(app)
    migration.init_app(app, db)
    login_manager.init_app(app)

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(home_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(todo_blueprint)

    @login_manager.user_loader
    def get_user(id):
        return User.query.get(int(id))

    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"
    login_manager.anonymous_user = AnonymousUser

    return app
