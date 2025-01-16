from flask import Blueprint, jsonify
from .models import Brasserie

bp = Blueprint('routes', __name__)

@bp.route('/brasseries', methods=['GET'])
def get_brasseries():
    # Récupérer toutes les brasseries de la base de données
    brasseries = Brasserie.query.all()

    # Créer une liste de dictionnaires avec les données des brasseries
    result = []
    for brasserie in brasseries:
        result.append({
            'id': brasserie.id,
            'nom': brasserie.nom,
            'adresse': brasserie.adresse,
            'ville': brasserie.ville
        })

    # Retourner les données sous forme de JSON
    return jsonify(result)
