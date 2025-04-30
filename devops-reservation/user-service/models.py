from flask_sqlalchemy import SQLAlchemy

# Initialisation de la base de données
db = SQLAlchemy()

# Définir la classe User pour la table des utilisateurs
class User(db.Model):
    __tablename__ = 'users'  # Nom de la table dans la base de données

    id = db.Column(db.Integer, primary_key=True)  # Identifiant unique pour chaque utilisateur
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email de l'utilisateur
    role = db.Column(db.String(50), nullable=False)  # Rôle de l'utilisateur (ex: admin, user)

    def __repr__(self):
        return f"<User {self.email}>"
