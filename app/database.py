from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# connexion a la base de donnée et déclaration de la base avec sql alchemy

#Importation des modèles
from app.models.commande.commande import Commande
from app.models.commande.detail import Detail
from app.models.commande.detail_objet import DetailObjet
from app.models.utilisateur.utilisateur import Utilisateur
from app.models.utilisateur.role import Role
from app.models.stock.objet_cond import ObjetCond
from app.models.stock.poids import Poids
from app.models.stock.vignette import Vignette
from app.models.stock.conditionnement import Conditionnement
from app.models.stock.objet import Objet

# url de connexion de la base
SQLALCHEMY_DATABASE_URL = "mysql://dev:12345@localhost/fromagerie_com"


# permet de définir les paramètre de connexion à la base
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# déclaration d'une base qui permet après de créer un modele et de mapper avec sql alchemy
Base = declarative_base()

# creation d'une session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Création des tables dans la base de données
Base.metadata.create_all(bind=engine)
