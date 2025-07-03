# Mise à jour du fichier conftest.py pour améliorer les tests d'intégration

import pytest
import fakeredis
import os
from app2 import create_app
from app2.models import db, Brasserie, Beer
from unittest.mock import patch


@pytest.fixture
def app():
    os.environ['FLASK_ENV'] = 'testing'

    app = create_app()

    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture
def client(app):
    """Client de test Flask."""
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


@pytest.fixture
def fake_redis():
    fake_redis_instance = fakeredis.FakeRedis()
    with patch('app2.routes.r', fake_redis_instance):
        yield fake_redis_instance


@pytest.fixture
def sample_brasserie(app):
    with app.app_context():
        brasserie = Brasserie(
            name="Test Brasserie",
            description="Une brasserie de test",
            image_url="http://example.com/image.jpg",
            latitude=47.2184,
            longitude=-1.5536
        )
        db.session.add(brasserie)
        db.session.commit()
        yield brasserie


@pytest.fixture
def sample_beer(app, sample_brasserie):
    """Crée une bière d'exemple pour les tests."""
    with app.app_context():
        beer = Beer(
            name="Test Beer",
            description="Une bière de test",
            price=4.50,
            degree=5.5,
            id_brasserie=sample_brasserie.id_brasserie,
            image_url="http://example.com/beer.jpg"
        )
        db.session.add(beer)
        db.session.commit()
        yield beer


@pytest.fixture
def multiple_brasseries(app):
    with app.app_context():
        brasseries = []
        for i in range(3):
            brasserie = Brasserie(
                name=f"Brasserie {i+1}",
                description=f"Description brasserie {i+1}",
                image_url=f"http://example.com/brasserie{i+1}.jpg",
                latitude=47.2184 + i * 0.01,
                longitude=-1.5536 + i * 0.01
            )
            db.session.add(brasserie)
            brasseries.append(brasserie)

        db.session.commit()
        yield brasseries


@pytest.fixture
def multiple_beers(app, sample_brasserie):
    with app.app_context():
        beers = []
        for i in range(3):
            beer = Beer(
                name=f"Beer {i+1}",
                description=f"Description beer {i+1}",
                price=4.50 + i,
                degree=5.0 + i * 0.5,
                id_brasserie=sample_brasserie.id_brasserie,
                image_url=f"http://example.com/beer{i+1}.jpg"
            )
            db.session.add(beer)
            beers.append(beer)

        db.session.commit()
        yield beers


@pytest.fixture(scope="session")
def integration_test_database():
    pass


# Hooks pytest pour les tests d'intégration
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "unit: marks tests as unit tests"
    )
    config.addinivalue_line(
        "markers", "slow: marks tests as slow tests"
    )


def pytest_collection_modifyitems(config, items):
    for item in items:
        if "test_integration" in item.nodeid:
            item.add_marker(pytest.mark.integration)

        elif "test_" in item.nodeid and "integration" not in item.nodeid:
            item.add_marker(pytest.mark.unit)