from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Numeric
from sqlalchemy.orm import relationship
db = SQLAlchemy()


class Brasserie(db.Model):
    __tablename__ = 'brasserie'

    id_brasserie = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    image_url = db.Column(db.String(100))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    # Relation avec Beer
    beers = db.relationship('Beer', backref='brasserie', lazy=True)

    def __repr__(self):
        return f"<Brasserie {self.name}>"


class Beer(db.Model):
    __tablename__ = 'beer'

    id_beer = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=True)  # Changé de Numeric à Float
    degree = db.Column(db.Float, nullable=True)  # Changé de Numeric à Float
    id_brasserie = db.Column(
        db.Integer,
        db.ForeignKey('brasserie.id_brasserie'),
        nullable=False
    )
    image_url = db.Column(db.String(255))

    def __repr__(self):
        return f"<Beer {self.name}>"