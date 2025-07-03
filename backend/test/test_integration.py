import pytest
import json
from app2.models import Brasserie, Beer, db


@pytest.mark.integration
class TestBrasserieIntegration:
    """Tests d'intégration pour les brasseries."""

    def test_complete_brasserie_workflow(self, client, fake_redis):
        """Test complet du workflow d'une brasserie : création, lecture, modification, suppression."""

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

        # 2. Vérifier la création en récupérant la brasserie
        get_response = client.get(f'/api/brasseries/{brasserie_id}')
        assert get_response.status_code == 200
        assert get_response.json['name'] == brasserie_data['name']

        # 3. Vérifier qu'elle apparaît dans la liste
        list_response = client.get('/api/brasseries')
        assert list_response.status_code == 200
        assert len(list_response.json) == 1
        assert list_response.json[0]['name'] == brasserie_data['name']

        # 4. Modifier la brasserie
        update_data = {
            'name': 'Brasserie Modifiée',
            'description': 'Description mise à jour'
        }

        update_response = client.put(f'/api/brasseries/{brasserie_id}',
                                     data=json.dumps(update_data),
                                     content_type='application/json')

        assert update_response.status_code == 200
        assert update_response.json['name'] == 'Brasserie Modifiée'

        # 5. Vérifier la modification
        get_updated_response = client.get(f'/api/brasseries/{brasserie_id}')
        assert get_updated_response.status_code == 200
        assert get_updated_response.json['name'] == 'Brasserie Modifiée'

        # 6. Supprimer la brasserie
        delete_response = client.delete(f'/api/brasseries/{brasserie_id}')
        assert delete_response.status_code == 200

        # 7. Vérifier la suppression
        get_deleted_response = client.get(f'/api/brasseries/{brasserie_id}')
        assert get_deleted_response.status_code == 404

        # 8. Vérifier qu'elle n'apparaît plus dans la liste
        final_list_response = client.get('/api/brasseries')
        assert final_list_response.status_code == 200
        assert len(final_list_response.json) == 0

    def test_brasserie_cache_invalidation(self, client, fake_redis):
        """Test que le cache est bien invalidé lors des modifications."""

        # Créer une brasserie
        brasserie_data = {
            'name': 'Test Cache',
            'description': 'Test cache invalidation',
            'image_url': 'http://example.com/cache.jpg',
            'latitude': 47.2184,
            'longitude': -1.5536
        }

        create_response = client.post('/api/brasseries',
                                      data=json.dumps(brasserie_data),
                                      content_type='application/json')
        brasserie_id = create_response.json['id']

        # Premier appel GET pour mettre en cache
        client.get('/api/brasseries')
        assert fake_redis.get('brasseries_all') is not None

        # Modifier la brasserie (devrait invalider le cache)
        update_data = {'name': 'Cache Invalidé'}
        client.put(f'/api/brasseries/{brasserie_id}',
                   data=json.dumps(update_data),
                   content_type='application/json')

        # Vérifier que le cache a été invalidé
        assert fake_redis.get('brasseries_all') is None

        # Supprimer la brasserie (devrait aussi invalider le cache)
        client.get('/api/brasseries')  # Remettre en cache
        assert fake_redis.get('brasseries_all') is not None

        client.delete(f'/api/brasseries/{brasserie_id}')
        assert fake_redis.get('brasseries_all') is None


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

        # 2. Vérifier la création
        get_response = client.get(f'/api/beers/{beer_id}')
        assert get_response.status_code == 200
        assert get_response.json['name'] == beer_data['name']
        assert get_response.json['price'] == beer_data['price']

        # 3. Vérifier dans la liste
        list_response = client.get('/api/beers')
        assert list_response.status_code == 200
        assert len(list_response.json) == 1

        # 4. Modifier la bière
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

        # 5. Supprimer la bière
        delete_response = client.delete(f'/api/beers/{beer_id}')
        assert delete_response.status_code == 200

        # 6. Vérifier la suppression
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

        # 3. Vérifier que les bières sont bien liées à la brasserie
        beers_response = client.get('/api/beers')
        beers_list = beers_response.json

        assert len(beers_list) == 2
        for beer in beers_list:
            assert beer['id_brasserie'] == brasserie_id

        # 4. Essayer de créer une bière avec une brasserie inexistante
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

        # Devrait échouer car la brasserie n'existe pas
        assert invalid_response.status_code == 400


@pytest.mark.integration
class TestCacheIntegration:
    """Tests d'intégration pour le système de cache."""

    def test_cache_consistency_across_operations(self, client, fake_redis):
        """Test que le cache reste cohérent lors de multiples opérations."""

        # 1. Créer plusieurs brasseries
        brasseries_data = [
            {
                'name': f'Brasserie {i}',
                'description': f'Description {i}',
                'image_url': f'http://example.com/brasserie{i}.jpg',
                'latitude': 47.2184 + i * 0.01,
                'longitude': -1.5536 + i * 0.01
            }
            for i in range(3)
        ]

        created_ids = []
        for brasserie_data in brasseries_data:
            response = client.post('/api/brasseries',
                                   data=json.dumps(brasserie_data),
                                   content_type='application/json')
            created_ids.append(response.json['id'])

        # 2. Récupérer la liste (mise en cache)
        response1 = client.get('/api/brasseries')
        assert len(response1.json) == 3

        # 3. Modifier une brasserie (invalidation cache)
        update_data = {'name': 'Brasserie Modifiée'}
        client.put(f'/api/brasseries/{created_ids[0]}',
                   data=json.dumps(update_data),
                   content_type='application/json')

        # 4. Récupérer la liste à nouveau (depuis la DB)
        response2 = client.get('/api/brasseries')
        assert len(response2.json) == 3

        # Vérifier que la modification est bien présente
        modified_brasserie = next(
            (b for b in response2.json if b['id'] == created_ids[0]),
            None
        )
        assert modified_brasserie is not None
        assert modified_brasserie['name'] == 'Brasserie Modifiée'

        # 5. Supprimer une brasserie (invalidation cache)
        client.delete(f'/api/brasseries/{created_ids[1]}')

        # 6. Vérifier que la liste est mise à jour
        response3 = client.get('/api/brasseries')
        assert len(response3.json) == 2

        # Vérifier que la brasserie supprimée n'est plus présente
        deleted_brasserie = next(
            (b for b in response3.json if b['id'] == created_ids[1]),
            None
        )
        assert deleted_brasserie is None

    def test_beer_cache_consistency(self, client, fake_redis, sample_brasserie):
        """Test de cohérence du cache pour les bières."""

        # Créer des bières
        beers_data = [
            {
                'name': f'Bière {i}',
                'description': f'Description {i}',
                'price': 4.50 + i,
                'degree': 5.0 + i,
                'id_brasserie': sample_brasserie.id_brasserie,
                'image_url': f'http://example.com/beer{i}.jpg'
            }
            for i in range(2)
        ]

        created_beer_ids = []
        for beer_data in beers_data:
            response = client.post('/api/beers',
                                   data=json.dumps(beer_data),
                                   content_type='application/json')
            created_beer_ids.append(response.json['id'])

        # Récupérer la liste (mise en cache)
        response1 = client.get('/api/beers')
        assert len(response1.json) == 2

        # Modifier une bière
        update_data = {'price': 9.99}
        client.put(f'/api/beers/{created_beer_ids[0]}',
                   data=json.dumps(update_data),
                   content_type='application/json')

        # Vérifier que la modification est reflétée
        response2 = client.get('/api/beers')
        modified_beer = next(
            (b for b in response2.json if b['id'] == created_beer_ids[0]),
            None
        )
        assert modified_beer['price'] == 9.99


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

        # 3. Essayer de supprimer la brasserie (devrait échouer ou supprimer en cascade)
        delete_response = client.delete(f'/api/brasseries/{brasserie_id}')

        # Selon votre configuration de contraintes, cela peut soit :
        # - Échouer (contrainte de clé étrangère) - status 400
        # - Réussir (suppression en cascade) - status 200
        assert delete_response.status_code in [200, 400]

        if delete_response.status_code == 200:
            # Si suppression en cascade, vérifier que la bière est aussi supprimée
            beer_check = client.get(f'/api/beers/{beer_id}')
            assert beer_check.status_code == 404
        else:
            # Si échec, vérifier que la brasserie existe toujours
            brasserie_check = client.get(f'/api/brasseries/{brasserie_id}')
            assert brasserie_check.status_code == 200

    def test_invalid_data_handling(self, client, fake_redis):
        """Test de gestion des données invalides."""

        # Test avec des données JSON malformées
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
            'latitude': 'not_a_number',  # Devrait être un float
            'longitude': 'not_a_number'  # Devrait être un float
        }

        response = client.post('/api/brasseries',
                               data=json.dumps(invalid_data),
                               content_type='application/json')
        assert response.status_code == 400