import os
from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from .models import db
from .routes import bp as routes_bp
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)

    # Configuration de la base de données MySQL
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://unlct7omaelffxqp:t85A4f3bCY3rsiC9VkGd@bbi9zrvl4akmfehwfapy-mysql.services.clever-cloud.com:3306/bbi9zrvl4akmfehwfapy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialisation de la base de données
    db.init_app(app)

    # Swagger configuration
    Swagger(app)

    # Ajout d'une valeur par défaut pour FRONT_URL
    front_url = os.getenv("FRONT_URL", "http://localhost:3000")
    print(f"FRONT_URL: {front_url}")  # Facultatif : utilise pour diagnostiquer les problèmes potentiels

    # Configuration CORS
    CORS(app, origins=[front_url])

    # Enregistrement du Blueprint contenant les routes
    app.register_blueprint(routes_bp)

    return app
