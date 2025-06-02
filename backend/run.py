import app

from app import create_app
<<<<<<< HEAD
import redis 

=======
from flask_cors import CORS
>>>>>>> 3e21aee3982861f65a531e4ff40008318434286d
app = create_app()
CORS(app)

# Connexion à Redis
try:
    r = redis.Redis(host='localhost', port=6379, db=0)

    # Test simple
    r.set("test_key", "Hello Redis!")
    value = r.get("test_key")

    print("Valeur récupérée depuis Redis:", value.decode())
except Exception as e:
    print("Erreur lors de la connexion à Redis :", e)
# Test de la connexion à la base de données


if __name__ == "__main__":
    app.run(debug=True)
