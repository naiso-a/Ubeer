from flask import Blueprint, jsonify, request
from .models import Brasserie, Beer, db


bp = Blueprint('routes', __name__, url_prefix='/api')


@bp.route('/brasseries', methods=['POST'])
def add_brasserie():
    """
    Add a new brasserie to the database.
    """
    data = request.json
<<<<<<< HEAD

    required_fields = ['name', 'description', 'image_url']
=======
    
    required_fields = ['name', 'description', 'image_url','latitude','longitude']
>>>>>>> 3e21aee3982861f65a531e4ff40008318434286d
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400

    try:
        new_brasserie = Brasserie(
            name=data['name'],
            description=data['description'],
            image_url=data['image_url'],
            latitude=data['latitude'],
            longitude=data['longitude']


        )
        db.session.add(new_brasserie)
        db.session.commit()

        return jsonify({
            'id': new_brasserie.id_brasserie,
            'name': new_brasserie.name,
            'description': new_brasserie.description,
            'image_url': new_brasserie.image_url,
            'latitude': new_brasserie.latitude,
            'longitude': new_brasserie.longitude,
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@bp.route('/brasseries/<int:brasserie_id>', methods=['PUT'])
def update_brasserie(brasserie_id):
    """
    Update an existing brasserie.
    """
    data = request.json
    brasserie = Brasserie.query.get(brasserie_id)

    if not brasserie:
        return jsonify({'error': 'Brasserie not found'}), 404

    if 'name' in data:
        brasserie.name = data['name']
    if 'description' in data:
        brasserie.description = data['description']
    if 'image_url' in data:
        brasserie.image_url = data['image_url']
<<<<<<< HEAD

=======
    if 'latitude' in data:
        brasserie.latitude = data['latitude']
    if 'longitude' in data:
        brasserie.longitude = data['longitude']
    
>>>>>>> 3e21aee3982861f65a531e4ff40008318434286d
    try:
        db.session.commit()
        return jsonify({
            'id': brasserie.id_brasserie,
            'name': brasserie.name,
            'description': brasserie.description,
            'image_url': brasserie.image_url,
            'latitude': brasserie.latitude,
            'longitude': brasserie.longitude,
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@bp.route('/brasseries/<int:brasserie_id>', methods=['DELETE'])
def delete_brasserie(brasserie_id):
    """
    Delete a brasserie by ID.
    """
    brasserie = Brasserie.query.get(brasserie_id)

    if not brasserie:
        return jsonify({'error': 'Brasserie not found'}), 404

    try:
        db.session.delete(brasserie)
        db.session.commit()
        return jsonify({'message': 'Brasserie successfully deleted'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@bp.route('/brasseries', methods=['GET'])
def get_brasseries():
    """
    Get all brasseries.
    """
    brasseries = Brasserie.query.all()
<<<<<<< HEAD
    result = [{
        'id': brasserie.id_brasserie,
        'name': brasserie.name,
        'description': brasserie.description,
        'image_url': brasserie.image_url
    } for brasserie in brasseries]
=======

    # Créer une liste de dictionnaires avec les données des brasseries
    result = []
    for brasserie in brasseries:
        result.append({
            'id': brasserie.id_brasserie,
            'name': brasserie.name,
            'description': brasserie.description,
            'image_url': brasserie.image_url,
            'latitude': brasserie.latitude,
            'longitude': brasserie.longitude,
        })

    # Retourner les données sous forme de JSON
>>>>>>> 3e21aee3982861f65a531e4ff40008318434286d
    return jsonify(result)


@bp.route('/beers', methods=['GET'])
def get_beers():
    """
    Get all beers.
    """
    beers = Beer.query.all()
    result = [{
        'id': beer.id_beer,
        'name': beer.name,
        'description': beer.description,
        'price': float(beer.price) if beer.price else None,
        'degree': float(beer.degree) if beer.degree else None,
        'image_url': beer.image_url,
        'id_brasserie': beer.id_brasserie
    } for beer in beers]
    return jsonify(result)


@bp.route('/beers', methods=['POST'])
def add_beer():
    """
    Add a new beer to the database.
    """
    data = request.json

    required_fields = ['name', 'price', 'degree', 'id_brasserie']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400

    try:
        new_beer = Beer(
            name=data['name'],
            description=data.get('description', ''),
            price=data['price'],
            degree=data['degree'],
            id_brasserie=data['id_brasserie'],
            image_url=data.get('image_url', '')
        )
        db.session.add(new_beer)
        db.session.commit()

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
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@bp.route('/beers/<int:beer_id>', methods=['PUT'])
def update_beer(beer_id):
    """
    Update an existing beer.
    """
    data = request.json
    beer = Beer.query.get(beer_id)

    if not beer:
        return jsonify({"error": "Beer not found"}), 404

    if "name" in data:
        beer.name = data["name"]
    if "description" in data:
        beer.description = data["description"]
    if "price" in data:
        beer.price = data["price"]
    if "degree" in data:
        beer.degree = data["degree"]
    if "image_url" in data:
        beer.image_url = data["image_url"]
    if "id_brasserie" in data:
        beer.id_brasserie = data["id_brasserie"]

    try:
        db.session.commit()
        return jsonify({
            "id": beer.id_beer,
            "name": beer.name,
            "description": beer.description,
            "price": float(beer.price),
            "degree": float(beer.degree),
            "id_brasserie": beer.id_brasserie,
            "image_url": beer.image_url
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


@bp.route('/beers/<int:beer_id>', methods=['DELETE'])
def delete_beer(beer_id):
    """
    Delete a beer by ID.
    """
    beer = Beer.query.get(beer_id)

    if not beer:
        return jsonify({"error": "Beer not found"}), 404

    try:
        db.session.delete(beer)
        db.session.commit()
        return jsonify({"message": "Beer successfully deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


@bp.route('/beers/<int:beer_id>', methods=['GET'])
def get_beer(beer_id):
    """
    Get a single beer by ID.
    """
    beer = Beer.query.get(beer_id)

    if not beer:
        return jsonify({"error": "Beer not found"}), 404

    return jsonify({
        "id": beer.id_beer,
        "name": beer.name,
        "description": beer.description,
        "price": float(beer.price),
        "degree": float(beer.degree),
        "id_brasserie": beer.id_brasserie,
        "image_url": beer.image_url
    }), 200


@bp.route('/brasseries/<int:brasserie_id>', methods=['GET'])
def get_brasserie(brasserie_id):
    """
    Get a single brasserie by ID.
    """
    brasserie = Brasserie.query.get(brasserie_id)

    if not brasserie:
        return jsonify({"error": "Brasserie not found"}), 404

    return jsonify({
        "id": brasserie.id_brasserie,
        "name": brasserie.name,
        "description": brasserie.description,
        "image_url": brasserie.image_url
    }), 200
