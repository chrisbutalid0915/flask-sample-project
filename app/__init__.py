
import logging
import os
from flask import Flask
from flask_migrate import Migrate
from pathlib import Path
from .extensions import api, db, jwt
from flask_jwt_extended import JWTManager


# Create a folder for logs if it doesn't exist
log_folder = "logs"
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# Configure logging settings
log_file_path = os.path.join(log_folder, "app.log")
logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format="%(asctime)s - %(levelname)s - %(message)s",  # Define log message format
    filename=log_file_path,  # Specify the log file
    filemode="a",  # Append mode for the log file
)

# CONSTANT
BASE_DIR = Path(__file__).resolve().parent.parent
migrate = Migrate()


def create_app():
    """Construct the core application."""
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    api.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    with app.app_context():
        from app.routes import address as address_namespace
        from app.routes import user as user_namespace
        from app.routes import auth as auth_namespace

        # add api namespace for swagger docs
        api.add_namespace(address_namespace.ns)
        api.add_namespace(user_namespace.ns)
        api.add_namespace(auth_namespace.ns)

        return app