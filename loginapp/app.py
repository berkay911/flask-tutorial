from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./testdb.db"
    app.secret_key = "supersecretkey"

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
    @login_manager.unauthorized_handler
    def unauthorized_callback():
        return "You must be logged in to view this page."

    bcrypt = Bcrypt(app)


    from routes import register_routes
    register_routes(app, db, bcrypt)

    migrate = Migrate(app, db)

    return app

