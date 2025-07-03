import app2

from app2 import create_app
import redis
from app2.redis_client import redis_client
from flask_cors import CORS


app = create_app()
CORS(app)


# Connexion à Redis
try:
    # Test simple
    redis_client.set('foo', 'bar')
    value = redis_client.get('foo')  # Variable manquante ajoutée
    print(f"Valeur récupérée: {value}")

    print("Valeur récupérée depuis Redis:", value.decode())
except Exception as e:
    print("Erreur lors de la connexion à Redis :", e)


if __name__ == "__main__":
    app.run(debug=True)