from . import db

class Brasserie(db.Model):
    __tablename__ = 'brasserie'  # Nom de la table dans la base de données

    id = db.Column(db.Integer, primary_key=True)  # Clé primaire (ajustez les champs selon votre table)
    nom = db.Column(db.String(100), nullable=False)  # Exemple de champ "nom"
    adresse = db.Column(db.String(255))  # Exemple de champ "adresse"
    ville = db.Column(db.String(100))  # Exemple de champ "ville"

    def __repr__(self):
        return f"<Brasserie {self.nom}>"
