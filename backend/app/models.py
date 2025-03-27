from flask_sqlalchemy import SQLAlchemy  # type: ignore

# Initialisation de l'instance db
db = SQLAlchemy()


class Brasserie(db.Model):
    __tablename__ = 'brasserie'  # Nom de la table dans la base de données

    id_brasserie = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    image_url = db.Column(db.String(100))

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
