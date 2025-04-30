from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db, User

# Créer l'application Flask
app = Flask(__name__)

# Charger la config depuis le fichier config.py
app.config.from_object(Config)

# Initialiser la base de données
db.init_app(app)

# Route pour créer un utilisateur
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    # Assure-toi que les données existent
    if not data or not data.get("email") or not data.get("role"):
        return jsonify({"message": "Données manquantes"}), 400

    new_user = User(email=data["email"], role=data["role"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Utilisateur créé"}), 201

# Route pour lister tous les utilisateurs
@app.route("/users", methods=["GET"])
def list_users():
    users = User.query.all()
    # Créer une liste d'utilisateurs à partir des résultats de la base de données
    return jsonify([{"email": u.email, "role": u.role} for u in users])

# Lancer le serveur
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Crée les tables si elles n'existent pas
    app.run(host="0.0.0.0", port=5000)

