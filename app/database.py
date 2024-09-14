from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# connexion a la base de donnée et déclaration de la base avec sql alchemy

#Importation des modèles
from app.models.commande.Commande import Commande
from app.models.commande.Detail import Detail
from app.models.commande.Detail_Objet import DetailObjet
from app.models.utilisateur.Utilisateur import Utilisateur
from app.models.utilisateur.Role import Role
from app.models.stock.Objet_Cond import ObjetCond
from app.models.stock.Poids import Poids
from app.models.stock.Vignette import Vignette
from app.models.stock.conditionnement import Conditionnement
from app.models.stock.Objet import Objet
from app.models.fidelite.ProgrammeFidelite import ProgrammeFidelite
from app.models.fidelite.Promo import Promo
from app.models.fidelite.Bonus import Bonus
from app.models.fidelite.Transaction import Transaction
from app.models.client.Departement import Departement
from app.models.client.Commune import Commune
from app.models.client.Client import Client
from app.models.client.Enseigne import Enseigne

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

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
