from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from .models import db  # Importer db depuis models.py
from .routes import bp as routes_bp

def create_app():
    app = Flask(__name__)

    # Configuration de la base de données MySQL (ajustez votre URI ici)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://unlct7omaelffxqp:PPI2yf7xoWJNIOoQA1K3@bbi9zrvl4akmfehwfapy-mysql.services.clever-cloud.com/bbi9zrvl4akmfehwfapy'    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialisation de l'extension db avec l'application Flask
    db.init_app(app)

    Swagger(app)

    CORS(app, origins=["http://localhost:3000"])

    # Enregistrement du Blueprint contenant les routes
    app.register_blueprint(routes_bp)

    return app
