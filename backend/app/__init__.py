from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes import bp as routes_bp

# Initialiser l'instance de SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuration de la base de données (à adapter à votre configuration MySQL)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://unlct7omaelffxqp:PPI2yf7xoWJNIOoQA1K3@bbi9zrvl4akmfehwfapy-mysql.services.clever-cloud.com/bbi9zrvl4akmfehwfapy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(routes_bp)

    return app
