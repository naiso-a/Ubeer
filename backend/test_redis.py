import redis

try:
    # Connexion à Redis
    r = redis.Redis(host='localhost', port=6379, db=0)

    # Test simple
    r.set("test_key", "Hello Redis!")
    value = r.get("test_key")

    print("Valeur récupérée depuis Redis:", value.decode())

except Exception as e:
    print("Erreur lors de la connexion à Redis :", e)
