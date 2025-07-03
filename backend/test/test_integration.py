import pytest
import json
from app2.models import Brasserie, Beer, db


@pytest.mark.integration
class TestBrasserieIntegration:
    """Tests d'intégration pour les brasseries."""

    def test_complete_brasserie_workflow(self, client, fake_redis):
        # 1. Créer une brasserie
        brasserie_data = {
            'name': 'Brasserie Intégration',
            'description': 'Test intégration complète',
            'image_url': 'http://example.com/integration.jpg',
            'latitude': 47.2184,
            'longitude': -1.5536
        }

        create_response = client.post('/api/brasseries',
                                      data=json.dumps(brasserie_data),
                                      content_type='application/json')

        assert create_response.status_code == 201
        created_brasserie = create_response.json
        brasserie_id = created_brasserie['id']


        get_response = client.get(f'/api/brasseries/{brasserie_id}')
        assert get_response.status_code == 200
        assert get_response.json['name'] == brasserie_data['name']


        list_response = client.get('/api/brasseries')
        assert list_response.status_code == 200
        assert len(list_response.json) == 1
        assert list_response.json[0]['name'] == brasserie_data['name']


        update_data = {
            'name': 'Brasserie Modifiée',
            'description': 'Description mise à jour'
        }

        update_response = client.put(f'/api/brasseries/{brasserie_id}',
                                     data=json.dumps(update_data),
                                     content_type='application/json')

        assert update_response.status_code == 200
        assert update_response.json['name'] == 'Brasserie Modifiée'


        get_updated_response = client.get(f'/api/brasseries/{brasserie_id}')
        assert get_updated_response.status_code == 200
        assert get_updated_response.json['name'] == 'Brasserie Modifiée'


        delete_response = client.delete(f'/api/brasseries/{brasserie_id}')
        assert delete_response.status_code == 200


        get_deleted_response = client.get(f'/api/brasseries/{brasserie_id}')
        assert get_deleted_response.status_code == 404


        final_list_response = client.get('/api/brasseries')
        assert final_list_response.status_code == 200
        assert len(final_list_response.json) == 0


@pytest.mark.integration
class TestBeerIntegration:
    """Tests d'intégration pour les bières."""

    def test_complete_beer_workflow(self, client, fake_redis, sample_brasserie):
        """Test complet du workflow d'une bière."""

        # 1. Créer une bière
        beer_data = {
            'name': 'Bière Intégration',
            'description': 'Test intégration bière',
            'price': 5.99,
            'degree': 6.5,
            'id_brasserie': sample_brasserie.id_brasserie,
            'image_url': 'http://example.com/beer_integration.jpg'
        }

        create_response = client.post('/api/beers',
                                      data=json.dumps(beer_data),
                                      content_type='application/json')

        assert create_response.status_code == 201
        created_beer = create_response.json
        beer_id = created_beer['id']

        get_response = client.get(f'/api/beers/{beer_id}')
        assert get_response.status_code == 200
        assert get_response.json['name'] == beer_data['name']
        assert get_response.json['price'] == beer_data['price']

        list_response = client.get('/api/beers')
        assert list_response.status_code == 200
        assert len(list_response.json) == 1

        update_data = {
            'name': 'Bière Modifiée',
            'price': 7.50
        }

        update_response = client.put(f'/api/beers/{beer_id}',
                                     data=json.dumps(update_data),
                                     content_type='application/json')

        assert update_response.status_code == 200
        assert update_response.json['name'] == 'Bière Modifiée'
        assert update_response.json['price'] == 7.50

        delete_response = client.delete(f'/api/beers/{beer_id}')
        assert delete_response.status_code == 200

        get_deleted_response = client.get(f'/api/beers/{beer_id}')
        assert get_deleted_response.status_code == 404

    def test_beer_brasserie_relationship(self, client, fake_redis):
        """Test de la relation entre bières et brasseries."""

        # 1. Créer une brasserie
        brasserie_data = {
            'name': 'Brasserie Relation',
            'description': 'Test relation',
            'image_url': 'http://example.com/relation.jpg',
            'latitude': 47.2184,
            'longitude': -1.5536
        }

        brasserie_response = client.post('/api/brasseries',
                                         data=json.dumps(brasserie_data),
                                         content_type='application/json')
        brasserie_id = brasserie_response.json['id']

        # 2. Créer plusieurs bières pour cette brasserie
        beers_data = [
            {
                'name': 'Bière 1',
                'description': 'Première bière',
                'price': 4.50,
                'degree': 5.0,
                'id_brasserie': brasserie_id,
                'image_url': 'http://example.com/beer1.jpg'
            },
            {
                'name': 'Bière 2',
                'description': 'Deuxième bière',
                'price': 5.50,
                'degree': 6.0,
                'id_brasserie': brasserie_id,
                'image_url': 'http://example.com/beer2.jpg'
            }
        ]

        beer_ids = []
        for beer_data in beers_data:
            response = client.post('/api/beers',
                                   data=json.dumps(beer_data),
                                   content_type='application/json')
            assert response.status_code == 201
            beer_ids.append(response.json['id'])

        beers_response = client.get('/api/beers')
        beers_list = beers_response.json

        assert len(beers_list) == 2
        for beer in beers_list:
            assert beer['id_brasserie'] == brasserie_id

        invalid_beer_data = {
            'name': 'Bière Invalide',
            'description': 'Bière avec brasserie inexistante',
            'price': 4.50,
            'degree': 5.0,
            'id_brasserie': 999999,  # ID inexistant
            'image_url': 'http://example.com/invalid.jpg'
        }

        invalid_response = client.post('/api/beers',
                                       data=json.dumps(invalid_beer_data),
                                       content_type='application/json')

        assert invalid_response.status_code == 400


@pytest.mark.integration
class TestErrorHandlingIntegration:
    """Tests d'intégration pour la gestion d'erreurs."""

    def test_cascading_deletes_and_errors(self, client, fake_redis):
        """Test des erreurs en cascade et de la gestion des contraintes."""

        # 1. Créer une brasserie
        brasserie_data = {
            'name': 'Brasserie Erreur',
            'description': 'Test gestion erreurs',
            'image_url': 'http://example.com/error.jpg',
            'latitude': 47.2184,
            'longitude': -1.5536
        }

        brasserie_response = client.post('/api/brasseries',
                                         data=json.dumps(brasserie_data),
                                         content_type='application/json')
        brasserie_id = brasserie_response.json['id']

        # 2. Créer une bière liée à cette brasserie
        beer_data = {
            'name': 'Bière Liée',
            'description': 'Bière liée à la brasserie',
            'price': 5.00,
            'degree': 5.5,
            'id_brasserie': brasserie_id,
            'image_url': 'http://example.com/linked_beer.jpg'
        }

        beer_response = client.post('/api/beers',
                                    data=json.dumps(beer_data),
                                    content_type='application/json')
        beer_id = beer_response.json['id']

        delete_response = client.delete(f'/api/brasseries/{brasserie_id}')


        assert delete_response.status_code in [200, 400]

        if delete_response.status_code == 200:
            beer_check = client.get(f'/api/beers/{beer_id}')
            assert beer_check.status_code == 404
        else:
            brasserie_check = client.get(f'/api/brasseries/{brasserie_id}')
            assert brasserie_check.status_code == 200

    def test_invalid_data_handling(self, client, fake_redis):

        invalid_json = "{'invalid': json}"
        response = client.post('/api/brasseries',
                               data=invalid_json,
                               content_type='application/json')
        assert response.status_code == 400

        # Test avec des types de données incorrects
        invalid_data = {
            'name': 'Test',
            'description': 'Test',
            'image_url': 'test.jpg',
            'latitude': 'not_a_number',
            'longitude': 'not_a_number'
        }

        response = client.post('/api/brasseries',
                               data=json.dumps(invalid_data),
                               content_type='application/json')
        assert response.status_code == 400