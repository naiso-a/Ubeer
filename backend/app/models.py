from flask_sqlalchemy import SQLAlchemy # type: ignore

# Initialisation de l'instance db
db = SQLAlchemy()

class Brasserie(db.Model):
    __tablename__ = 'brasserie'  # Nom de la table dans la base de données

    id_brasserie = db.Column(db.Integer, primary_key=True)  # Clé primaire (ajustez les champs selon votre table)
    name = db.Column(db.String(100), nullable=False)  # Exemple de champ "nom"
    description = db.Column(db.String(255))  # Exemple de champ "adresse"
    image_url = db.Column(db.String(100))  # Exemple de champ "ville"

    def __repr__(self):
        return f"<Brasserie {self.nom}>"
