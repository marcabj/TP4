import os

# Remplace ces deux valeurs par tes vrais hashes
bad_hash = "c1a4be04b972b6c17db242fc37752ad517c29402"
good_hash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"

# Lancer git bisect
os.system(f"git bisect start {bad_hash} {good_hash}")

# Exécuter le script qui teste le bug à chaque commit
os.system("git bisect run python manage.py test")
