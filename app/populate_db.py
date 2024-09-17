from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.models.client.client import Client
from app.models.client.commune import Commune
from app.models.client.departement import Departement
from app.models.client.enseigne import Enseigne
from app.models.utilisateur.utilisateur import Utilisateur
from app.models.utilisateur.role import Role
from app.models.stock.objet import Objet
from app.models.stock.objet_cond import ObjetCond
from app.models.stock.poids import Poids
from app.models.stock.vignette import Vignette
from app.models.stock.conditionnement import Conditionnement
from app.models.fidelite.programme_fidelite import ProgrammeFidelite
from app.models.fidelite.bonus import Bonus
from app.models.fidelite.transaction import Transaction
from app.models.commande.commande import Commande
from app.models.commande.detail import Detail
from app.models.commande.detail_objet import DetailObjet

# Configuration de la base de données
DATABASE_URL = "mysql://dev:12345@localhost:3306/fromagerie_com"

# Création du moteur SQLAlchemy
engine = create_engine(DATABASE_URL)

# Création de la classe de session configurée
Session = sessionmaker(bind=engine)

# Création de la session
session = Session()

# Exemple de fonction pour peupler la base de données
def populate_db():
    try:
        # Ajout de clients
        client1 = Client(genre="M", nom="Client 1")
        client2 = Client(genre="F", nom="Client 2")
        session.add_all([client1, client2])
        session.commit()  # Commit the session to save the clients to the database

        # Ajout de communes
        commune1 = Commune(nom="Commune 1")
        commune2 = Commune(nom="Commune 2")
        session.add_all([commune1, commune2])

        # Ajout de départements
        departement1 = Departement(nom="Département 1")
        departement2 = Departement(nom="Département 2")
        session.add_all([departement1, departement2])

        # Ajout d'enseignes
        enseigne1 = Enseigne(libelle="Enseigne 1", ville="Ville 1", departement_id=departement1.id)
        enseigne2 = Enseigne(libelle="Enseigne 2", ville="Ville 2", departement_id=departement2.id)
        session.add_all([enseigne1, enseigne2])

        # Ajout d'utilisateurs
        utilisateur1 = Utilisateur(nom_utilisateur="Utilisateur 1")
        utilisateur2 = Utilisateur(nom_utilisateur="Utilisateur 2")
        session.add_all([utilisateur1, utilisateur2])

        # Ajout de rôles
        role1 = Role(librole="Role 1")
        role2 = Role(librole="Role 2")
        session.add_all([role1, role2])

        # Ajout de conditionnements
        conditionnement1 = Conditionnement(libcondit="Conditionnement 1", poidscondit=1, prixcond=10.0, ordreimp=1)
        conditionnement2 = Conditionnement(libcondit="Conditionnement 2", poidscondit=2, prixcond=20.0, ordreimp=2)
        session.add_all([conditionnement1, conditionnement2])
        session.commit()

        # Ajout d'objets
        objet1 = Objet(libobj="Objet 1", conditionnement_id=conditionnement1.idcondit)
        objet2 = Objet(libobj="Objet 2", conditionnement_id=conditionnement2.idcondit)
        session.add_all([objet1, objet2])
        session.commit()  # Commit objets before adding objet_cond and detail_objet

        # Ajout d'objets conditionnés
        objet_cond1 = ObjetCond(qteobjdeb=10, qteobjfin=20, codobj=objet1.codobj, codcond=conditionnement1.idcondit)
        objet_cond2 = ObjetCond(qteobjdeb=15, qteobjfin=25, codobj=objet2.codobj, codcond=conditionnement2.idcondit)
        session.add_all([objet_cond1, objet_cond2])

        # Ajout de poids
        poids1 = Poids(valmin=10, valtimbre=20)
        poids2 = Poids(valmin=15, valtimbre=25)
        session.add_all([poids1, poids2])

        # Ajout de vignettes
        vignette1 = Vignette(valmin=10, valtimbre=20)
        vignette2 = Vignette(valmin=15, valtimbre=25)
        session.add_all([vignette1, vignette2])

        # Ajout de programmes de fidélité
        programme_fidelite1 = ProgrammeFidelite(client_id=1, points=100.0, level="Silver")
        programme_fidelite2 = ProgrammeFidelite(client_id=2, points=200.0, level="Gold")
        session.add_all([programme_fidelite1, programme_fidelite2])

        # Ajout de bonus
        bonus1 = Bonus(user_id=1, bonus_type="WELCOME", points=10.0, name="Bonus 1")
        bonus2 = Bonus(user_id=2, bonus_type="ANNIVERSARY", points=20.0, name="Bonus 2")
        session.add_all([bonus1, bonus2])

        # Ajout de transactions
        transaction1 = Transaction(user_id=1, amount_spent=100.0, points_earned=10.0, name="Transaction 1")
        transaction2 = Transaction(user_id=2, amount_spent=200.0, points_earned=20.0, name="Transaction 2")
        session.add_all([transaction1, transaction2])

        # Ajout de commandes
        commande1 = Commande(codcde=1, datcde="2023-01-01", codcli=1, timbrecli=1.0, timbre_cde=1.0, nbcolis=1,
                            cheqcli=1.0, idcondit=1, cdeComt="Commentaire 1", barchive=0, bstock=0, name="Commande 1")
        commande2 = Commande(codcde=2, datcde="2023-01-02", codcli=2, timbrecli=2.0, timbre_cde=2.0, nbcolis=2,
                            cheqcli=2.0, idcondit=2, cdeComt="Commentaire 2", barchive=0, bstock=0, name="Commande 2")
        session.add_all([commande1, commande2])

        # Ajout de détails
        detail1 = Detail(codcde=1, qte=1, colis=1, commentaire="Commentaire 1", name="Detail 1")
        detail2 = Detail(codcde=2, qte=2, colis=2, commentaire="Commentaire 2", name="Detail 2")
        session.add_all([detail1, detail2])

        # Ajout de détails d'objets
        detail_objet1 = DetailObjet(detail_id=1, objet_id=objet1.codobj, name="DetailObjet 1")
        detail_objet2 = DetailObjet(detail_id=2, objet_id=objet2.codobj, name="DetailObjet 2")
        session.add_all([detail_objet1, detail_objet2])

        # Envoi des modifications à la base de données
        session.commit()
        print("Base de données remplie avec succès!")
    except Exception as e:
        session.rollback()
        print(f"Une erreur est survenue: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    populate_db()