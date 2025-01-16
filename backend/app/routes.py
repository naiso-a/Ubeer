from flask import Blueprint, jsonify, request
from .models import Brasserie, Beer, db

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

@bp.route('/beers', methods=['GET'])
def get_beers():
    """
    Get all beers.
    ---
    tags:
      - Beers
    responses:
      200:
        description: A list of beers
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    description: The beer ID
                    example: 1
                  name:
                    type: string
                    description: The name of the beer
                    example: "Blonde de la Brasserie"
                  description:
                    type: string
                    description: The description of the beer
                    example: "A light and refreshing beer."
                  price:
                    type: number
                    format: float
                    description: The price of the beer
                    example: 5.0
                  degree:
                    type: number
                    format: float
                    description: The alcohol percentage of the beer
                    example: 4.5
                  image_url:
                    type: string
                    description: The image URL of the beer
                    example: "http://example.com/beer.jpg"
                  id_brasserie:
                    type: integer
                    description: The brasserie ID
                    example: 1
    """
    # Récupérer toutes les bières de la base de données
    beers = Beer.query.all()

    # Créer une liste de dictionnaires avec les données des bières
    result = [
        {
            'id': beer.id_beer,
            'name': beer.name,
            'description': beer.description,
            'price': float(beer.price),  # Convertir en float si nécessaire
            'degree': float(beer.degree),  # Convertir en float si nécessaire
            'image_url': beer.image_url,
            'id_brasserie': beer.id_brasserie
        }
        for beer in beers
    ]

    # Retourner les données sous forme de JSON
    return jsonify(result)


@bp.route('/beers', methods=['POST'])
def add_beer():
    """
    Add a new beer to the database.
    ---
    tags:
      - Beers
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              name:
                type: string
                description: The name of the beer
                example: "Blonde de la Brasserie"
              description:
                type: string
                description: The description of the beer
                example: "A light and refreshing beer."
              price:
                type: number
                format: float
                description: The price of the beer
                example: 5.0
              degree:
                type: number
                format: float
                description: The alcohol percentage of the beer
                example: 4.5
              image_url:
                type: string
                description: The image URL of the beer
                example: "http://example.com/beer.jpg"
              id_brasserie:
                type: integer
                description: The brasserie ID the beer belongs to
                example: 1
    responses:
      201:
        description: Beer successfully created
      400:
        description: Invalid input
    """
    # Récupérer les données de la requête
    data = request.json

    # Valider les données reçues
    required_fields = ['name', 'price', 'degree', 'id_brasserie']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400

    try:
        # Créer une nouvelle bière
        new_beer = Beer(
            name=data['name'],
            description=data.get('description', ''),  # Champ facultatif
            price=data['price'],
            degree=data['degree'],
            id_brasserie=data['id_brasserie'],
            image_url=data.get('image_url', '')  # Champ facultatif
        )

        # Ajouter à la base de données
        db.session.add(new_beer)
        db.session.commit()

        # Retourner la réponse avec le statut 201 (Created)
        return jsonify({
            'id': new_beer.id_beer,
            'name': new_beer.name,
            'description': new_beer.description,
            'price': float(new_beer.price),
            'degree': float(new_beer.degree),
            'id_brasserie': new_beer.id_brasserie,
            'image_url': new_beer.image_url
        }), 201

    except Exception as e:
        # Gérer les erreurs (exemple : clé étrangère invalide)
        db.session.rollback()
        return jsonify({'error': str(e)}), 400