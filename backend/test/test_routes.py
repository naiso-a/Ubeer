import pytest
import json
from app2.models import Brasserie, Beer, db


class TestBrasserieRoutes:
    """Tests pour les routes des brasseries."""

    def test_get_brasseries_empty(self, client, fake_redis):
        """Test GET /api/brasseries avec une base vide."""
        response = client.get('/api/brasseries')
        assert response.status_code == 200
        assert response.json == []

    def test_get_brasseries_with_data(self, client, fake_redis, sample_brasserie):
        """Test GET /api/brasseries avec des données."""
        response = client.get('/api/brasseries')
        assert response.status_code == 200
        data = response.json
        assert len(data) == 1
        assert data[0]['name'] == "Test Brasserie"
        assert data[0]['description'] == "Une brasserie de test"

    def test_get_brasseries_from_cache(self, client, fake_redis, sample_brasserie):
        """Test que les données sont bien mises en cache."""
        # Premier appel - données depuis la DB
        response1 = client.get('/api/brasseries')
        assert response1.status_code == 200

        # Deuxième appel - données depuis le cache
        response2 = client.get('/api/brasseries')
        assert response2.status_code == 200
        assert response1.json == response2.json

        # Vérifier que les données sont en cache
        cached_data = fake_redis.get('brasseries_all')
        assert cached_data is not None

    def test_post_brasserie_success(self, client, fake_redis):
        """Test POST /api/brasseries avec des données valides."""
        data = {
            'name': 'Nouvelle Brasserie',
            'description': 'Une nouvelle brasserie',
            'image_url': 'http://example.com/new.jpg',
            'latitude': 48.8566,
            'longitude': 2.3522
        }

        response = client.post('/api/brasseries',
                               data=json.dumps(data),
                               content_type='application/json')

        assert response.status_code == 201
        response_data = response.json
        assert response_data['name'] == 'Nouvelle Brasserie'
        assert response_data['id'] is not None

        # Vérifier que le cache a été invalidé
        cached_data = fake_redis.get('brasseries_all')
        assert cached_data is None

    def test_post_brasserie_missing_fields(self, client, fake_redis):
        """Test POST /api/brasseries avec des champs manquants."""
        data = {
            'name': 'Brasserie incomplète'
            # Champs manquants : description, image_url, latitude, longitude
        }

        response = client.post('/api/brasseries',
                               data=json.dumps(data),
                               content_type='application/json')

        assert response.status_code == 400
        assert 'Missing field' in response.json['error']

    def test_get_brasserie_by_id(self, client, sample_brasserie):
        """Test GET /api/brasseries/<id>."""
        response = client.get(f'/api/brasseries/{sample_brasserie.id_brasserie}')
        assert response.status_code == 200
        data = response.json
        assert data['name'] == sample_brasserie.name
        assert data['id'] == sample_brasserie.id_brasserie

    def test_get_brasserie_not_found(self, client):
        """Test GET /api/brasseries/<id> avec un ID inexistant."""
        response = client.get('/api/brasseries/999')
        assert response.status_code == 404
        assert 'not found' in response.json['error']

    def test_put_brasserie_success(self, client, fake_redis, sample_brasserie):
        """Test PUT /api/brasseries/<id> avec des données valides."""
        data = {
            'name': 'Brasserie Modifiée',
            'description': 'Description modifiée'
        }

        response = client.put(f'/api/brasseries/{sample_brasserie.id_brasserie}',
                              data=json.dumps(data),
                              content_type='application/json')

        assert response.status_code == 200
        assert response.json['name'] == 'Brasserie Modifiée'
        assert response.json['description'] == 'Description modifiée'

    def test_delete_brasserie_success(self, client, fake_redis, sample_brasserie):
        """Test DELETE /api/brasseries/<id>."""
        response = client.delete(f'/api/brasseries/{sample_brasserie.id_brasserie}')
        assert response.status_code == 200
        assert 'successfully deleted' in response.json['message']

        # Vérifier que la brasserie a été supprimée
        get_response = client.get(f'/api/brasseries/{sample_brasserie.id_brasserie}')
        assert get_response.status_code == 404


class TestBeerRoutes:
    """Tests pour les routes des bières."""

    def test_get_beers_empty(self, client, fake_redis):
        """Test GET /api/beers avec une base vide."""
        response = client.get('/api/beers')
        assert response.status_code == 200
        assert response.json == []

    def test_get_beers_with_data(self, client, fake_redis, sample_beer):
        """Test GET /api/beers avec des données."""
        response = client.get('/api/beers')
        assert response.status_code == 200
        data = response.json
        assert len(data) == 1
        assert data[0]['name'] == "Test Beer"
        assert data[0]['price'] == 4.50
        assert data[0]['degree'] == 5.5

    def test_post_beer_success(self, client, fake_redis, sample_brasserie):
        """Test POST /api/beers avec des données valides."""
        data = {
            'name': 'Nouvelle Bière',
            'description': 'Une nouvelle bière',
            'price': 5.50,
            'degree': 6.5,
            'id_brasserie': sample_brasserie.id_brasserie,
            'image_url': 'http://example.com/beer.jpg'
        }

        response = client.post('/api/beers',
                               data=json.dumps(data),
                               content_type='application/json')

        assert response.status_code == 201
        response_data = response.json
        assert response_data['name'] == 'Nouvelle Bière'
        assert response_data['price'] == 5.50
        assert response_data['degree'] == 6.5

    def test_post_beer_missing_fields(self, client, fake_redis):
        """Test POST /api/beers avec des champs manquants."""
        data = {
            'name': 'Bière incomplète'
            # Champs manquants : price, degree, id_brasserie
        }

        response = client.post('/api/beers',
                               data=json.dumps(data),
                               content_type='application/json')

        assert response.status_code == 400
        assert 'Missing field' in response.json['error']

    def test_get_beer_by_id(self, client, sample_beer):
        """Test GET /api/beers/<id>."""
        response = client.get(f'/api/beers/{sample_beer.id_beer}')
        assert response.status_code == 200
        data = response.json
        assert data['name'] == sample_beer.name
        assert data['price'] == float(sample_beer.price)

    def test_put_beer_success(self, client, fake_redis, sample_beer):
        """Test PUT /api/beers/<id> avec des données valides."""
        data = {
            'name': 'Bière Modifiée',
            'price': 6.00
        }

        response = client.put(f'/api/beers/{sample_beer.id_beer}',
                              data=json.dumps(data),
                              content_type='application/json')

        assert response.status_code == 200
        assert response.json['name'] == 'Bière Modifiée'
        assert response.json['price'] == 6.00

    def test_delete_beer_success(self, client, fake_redis, sample_beer):
        """Test DELETE /api/beers/<id>."""
        response = client.delete(f'/api/beers/{sample_beer.id_beer}')
        assert response.status_code == 200
        assert 'successfully deleted' in response.json['message']

        # Vérifier que la bière a été supprimée
        get_response = client.get(f'/api/beers/{sample_beer.id_beer}')
        assert get_response.status_code == 404