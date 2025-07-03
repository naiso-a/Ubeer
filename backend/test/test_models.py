import pytest

from app2.models import Brasserie, Beer, db


class TestBrasserie:
    """Tests pour le modèle Brasserie."""

    def test_create_brasserie(self, app):
        """Test de création d'une brasserie."""
        with app.app_context():
            brasserie = Brasserie(
                name="Ma Brasserie",
                description="Description test",
                image_url="http://example.com/image.jpg",
                latitude=47.2184,
                longitude=-1.5536
            )
            db.session.add(brasserie)
            db.session.commit()

            assert brasserie.id_brasserie is not None
            assert brasserie.name == "Ma Brasserie"
            assert brasserie.description == "Description test"
            assert brasserie.latitude == 47.2184
            assert brasserie.longitude == -1.5536

class TestBeer:
    """Tests pour le modèle Beer."""

    def test_create_beer(self, app, sample_brasserie):
        """Test de création d'une bière."""
        with app.app_context():
            beer = Beer(
                name="Ma Bière",
                description="Description bière",
                price=4.50,
                degree=5.5,
                id_brasserie=sample_brasserie.id_brasserie,
                image_url="http://example.com/beer.jpg"
            )
            db.session.add(beer)
            db.session.commit()

            assert beer.id_beer is not None
            assert beer.name == "Ma Bière"
            assert beer.price == 4.50
            assert beer.degree == 5.5
            assert beer.id_brasserie == sample_brasserie.id_brasserie


    def test_beer_without_brasserie(self, app):
        with app.app_context():
            beer = Beer(
                name="Bière sans brasserie",
                price=4.50,
                degree=5.5
            )
            db.session.add(beer)

            with pytest.raises(Exception):
                db.session.commit()