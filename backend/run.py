import app

from app import create_app
import redis
from app.redis_client import redis_client
from flask_cors import CORS


app = create_app()
CORS(app)


# Connexion à Redis
try:
    # Test simple
    #redis_client.set("test_key", "Hello Redis!")
    redis_client.set('foo', 'bar')
    print(redis_client.get('foo'))

    print("Valeur récupérée depuis Redis:", value.decode())
except Exception as e:  
    print("Erreur lors de la connexion à Redis :", e)
# Test de la connexion à la base de données


if __name__ == "__main__":
    app.run(debug=True)
