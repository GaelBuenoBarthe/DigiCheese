from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Connexion à la base de données et déclaration de la base avec SQLAlchemy

# URL de connexion de la base
SQLALCHEMY_DATABASE_URL = "mysql://dev:12345@localhost/fromagerie_com"

# Permet de définir les paramètres de connexion à la base
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Déclaration d'une base qui permet après de créer un modèle et de mapper avec SQLAlchemy
Base = declarative_base()

# Création d'une session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Importation des modèles
def import_models():
    from app.models.commande.commande import Commande
    from app.models.commande.detail import Detail
    from app.models.commande.detail_objet import DetailObjet
    from app.models.client.client import Client
    from app.models.client.commune import Commune
    from app.models.client.departement import Departement
    from app.models.client.enseigne import Enseigne
    from app.models.utilisateur.utilisateur import Utilisateur
    from app.models.utilisateur.role import Role
    from app.models.utilisateur.role_utilisateur import RoleUtilisateur

import_models()

# Création des tables dans la base de données
Base.metadata.create_all(bind=engine)

