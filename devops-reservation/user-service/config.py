import os

class Config:
    # URL de connexion à la base de données PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/user_db")
    
    # Désactiver le suivi des modifications pour éviter les avertissements inutiles
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Clé secrète pour sécuriser les sessions Flask
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")

