from flask import Flask
from .routes.home import home_bp
from .routes.about import about_bp
from .routes.litters import litters_bp
from .routes.contact import contact_bp
import os

def create_app():
    app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))

    #incarca blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(litters_bp)
    app.register_blueprint(contact_bp)

    return app

