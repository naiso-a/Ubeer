from flask import Blueprint, jsonify
from .models import Brasserie

bp = Blueprint('routes', __name__)

@bp.route('/brasseries', methods=['GET'])
def get_brasseries():
    """
    Get all brasseries.
    ---
    tags:
      - Brasseries
    responses:
      200:
        description: A list of brasseries
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    description: The brasserie ID
                    example: 1
                  name:
                    type: string
                    description: The name of the brasserie
                    example: "Brasserie Du Nord"
                  description:
                    type: string
                    description: The description of the brasserie
                    example: "A traditional Belgian brewery"
                  image_url:
                    type: string
                    description: The image URL of the brasserie
                    example: "http://example.com/image.jpg"
    """
    # Récupérer toutes les brasseries de la base de données
    brasseries = Brasserie.query.all()

    # Créer une liste de dictionnaires avec les données des brasseries
    result = []
    for brasserie in brasseries:
        result.append({
            'id': brasserie.id_brasserie,
            'name': brasserie.name,
            'description': brasserie.description,
            'image_url': brasserie.image_url
        })

    # Retourner les données sous forme de JSON
    return jsonify(result)