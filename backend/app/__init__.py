import os
from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
<<<<<<< HEAD
from dotenv import load_dotenv

from .models import db
from .routes import bp as routes_bp


load_dotenv()  # chargement du .env

=======
from .models import db
from .routes import bp as routes_bp
from dotenv import load_dotenv

>>>>>>> 3e21aee3982861f65a531e4ff40008318434286d

def create_app():
    app = Flask(__name__)

    # Configuration de la base de données MySQL
<<<<<<< HEAD
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        'mysql+mysqlconnector://unlct7omaelffxqp:t85A4f3bCY3rsiC9VkGd@'
        'bbi9zrvl4akmfehwfapy-mysql.services.clever-cloud.com:3306/'
        'bbi9zrvl4akmfehwfapy'
    )
=======
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://unlct7omaelffxqp:t85A4f3bCY3rsiC9VkGd@bbi9zrvl4akmfehwfapy-mysql.services.clever-cloud.com:3306/bbi9zrvl4akmfehwfapy'
>>>>>>> 3e21aee3982861f65a531e4ff40008318434286d
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
<<<<<<< HEAD
    Swagger(app)

    front_url = os.getenv("FRONT_URL")
=======

    # Swagger configuration
    Swagger(app)

    # Ajout d'une valeur par défaut pour FRONT_URL
    front_url = os.getenv("FRONT_URL", "http://localhost:3000")
    print(f"FRONT_URL: {front_url}")  # Facultatif : utilise pour diagnostiquer les problèmes potentiels

    # Configuration CORS
>>>>>>> 3e21aee3982861f65a531e4ff40008318434286d
    CORS(app, origins=[front_url])

    app.register_blueprint(routes_bp)

    return app
