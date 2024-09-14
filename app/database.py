from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Base class to create models
Base = declarative_base()

# Database connection URL
SQLALCHEMY_DATABASE_URL =  "mysql://dev:12345@localhost/fromagerie_com"

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables (Ensure this is called at some point)
def init_db():
    importmodels()  # Ensure models are imported
    Base.metadata.create_all(bind=engine)

# Dependency function to provide a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Import models to ensure they are registered
def importmodels():
    from app.models.commande.commande import Commande
    from app.models.commande.detail import Detail
    from app.models.commande.detail_objet import DetailObjet
    from app.models.utilisateur.utilisateur import Utilisateur
    from app.models.utilisateur.role import Role
    from app.models.stock.objet_cond import ObjetCond
    from app.models.stock.poids import Poids
    from app.models.stock.vignette import Vignette
   # from app.models.stock.Conditionnement import Conditionnement
    from app.models.stock.objet import Objet
    from app.models.fidelite.programme_fidelite import ProgrammeFidelite
    from app.models.fidelite.promo import Promo
    from app.models.fidelite.bonus import Bonus
    from app.models.fidelite.transaction import Transaction
    from app.models.client.departement import Departement
    from app.models.client.commune import Commune
    from app.models.client.client import Client
    from app.models.client.enseigne import Enseigne

