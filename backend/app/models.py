<<<<<<< HEAD
from flask_sqlalchemy import SQLAlchemy  # type: ignore

=======
from flask_sqlalchemy import SQLAlchemy # type: ignore
from sqlalchemy import Column, Integer, String, Float, ForeignKey  # Make sure sqlalchemy is installed: pip install sqlalchemy
from sqlalchemy.orm import relationship
>>>>>>> 3e21aee3982861f65a531e4ff40008318434286d
# Initialisation de l'instance db
db = SQLAlchemy()


class Brasserie(db.Model):
    __tablename__ = 'brasserie'  # Nom de la table dans la base de données

<<<<<<< HEAD
    id_brasserie = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    image_url = db.Column(db.String(100))
=======
    id_brasserie = db.Column(db.Integer, primary_key=True)  # Clé primaire (ajustez les champs selon votre table)
    name = db.Column(db.String(100), nullable=False)  # Exemple de champ "nom"
    description = db.Column(db.String(255))  # Exemple de champ "adresse"
    image_url = db.Column(db.String(100))  # Exemple de champ "ville"
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
>>>>>>> 3e21aee3982861f65a531e4ff40008318434286d

    def __repr__(self):
        return f"<Brasserie {self.name}>"


class Beer(db.Model):
    __tablename__ = 'beer'  # Nom de la table dans la base de données

    id_beer = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Numeric(10, 2), nullable=True)
    degree = db.Column(db.Numeric(10, 2), nullable=True)
    id_brasserie = db.Column(
        db.Integer,
        db.ForeignKey('brasserie.id_brasserie'),
        nullable=False
    )
    image_url = db.Column(db.String(255))

    def __repr__(self):
        return f"<Beer {self.name}>"
