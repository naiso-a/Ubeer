import os
from flask import Flask
from flasgger import Swagger
from .models import db  # Importer db depuis models.py
from .routes import bp as routes_bp
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)

    # Configuration de la base de données MySQL (ajustez votre URI ici)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://unlct7omaelffxqp:PPI2yf7xoWJNIOoQA1K3@bbi9zrvl4akmfehwfapy-mysql.services.clever-cloud.com:3306/bbi9zrvl4akmfehwfapy'    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialisation de la base de données
    db.init_app(app)

    Swagger(app)

    front_url = os.getenv("FRONT_URL")

    CORS(app, origins=[front_url])

    # Enregistrement du Blueprint contenant les routes
    app.register_blueprint(routes_bp)

    return app
