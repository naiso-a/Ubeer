import os
from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from .models import db
from .routes import bp as routes_bp
from dotenv import load_dotenv

load_dotenv()  # chargement du .env



def create_app():
    app = Flask(__name__)

    # Configuration de la base de données MySQL

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        'mysql+mysqlconnector://unlct7omaelffxqp:t85A4f3bCY3rsiC9VkGd@'
        'bbi9zrvl4akmfehwfapy-mysql.services.clever-cloud.com:3306/'
        'bbi9zrvl4akmfehwfapy'
    )

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    Swagger(app)

    front_url = os.getenv("FRONT_URL")

    CORS(app, origins=[front_url])

    app.register_blueprint(routes_bp)

    return app
