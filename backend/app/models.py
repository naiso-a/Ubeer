from flask_sqlalchemy import SQLAlchemy # type: ignore
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
# Initialisation de l'instance db
db = SQLAlchemy()

class Brasserie(db.Model):
    __tablename__ = 'brasserie'  # Nom de la table dans la base de données

    id_brasserie = db.Column(db.Integer, primary_key=True)  # Clé primaire (ajustez les champs selon votre table)
    name = db.Column(db.String(100), nullable=False)  # Exemple de champ "nom"
    description = db.Column(db.String(255))  # Exemple de champ "adresse"
    image_url = db.Column(db.String(100))  # Exemple de champ "ville"

    def __repr__(self):
        return f"<Brasserie {self.name}>"

class Beer(db.Model):
    __tablename__ = 'beer'  # Nom de la table dans la base de données

    id_beer = db.Column(db.Integer, primary_key=True)  # Clé primaire pour la bière
    name = db.Column(db.String(100), nullable=False)  # Nom de la bière (obligatoire)
    description = db.Column(db.String(255))  # Description de la bière (facultatif)
    price = db.Column(db.Numeric(10, 2), nullable=True)  # Prix avec précision décimale
    degree = db.Column(db.Numeric(10, 2), nullable=True)  # Taux d'alcool avec précision décimale
    id_brasserie = db.Column(db.Integer, db.ForeignKey('brasserie.id_brasserie'), nullable=False)  # Clé étrangère vers la table Brasserie
    image_url = db.Column(db.String(255))  # URL de l'image (facultatif)

    def __repr__(self):
        return f"<Beer {self.name}>"


