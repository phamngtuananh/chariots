import os

from dotenv import load_dotenv
from flask import Flask

from app.database import setup_database
from app.routes import setup_routes

load_dotenv()


def create_app():
    new_app = Flask(__name__)

    # Load configuration settings
    app_env = os.environ['ENVIRONMENT']
    if app_env == 'production':
        new_app.config.from_object('app.config.ProductionConfig')
    elif app_env == 'development':
        new_app.config.from_object('app.config.DevelopmentConfig')
    else:
        print('Unknown ENVIRONMENT variable, loading development configurations.')
        new_app.config.from_object('app.config.DevelopmentConfig')

    # Setup database
    setup_database(new_app)

    # Setup routes
    setup_routes(new_app)

    return new_app
