from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.models.client.client import Client
from app.models.client.commune import Commune
from app.models.client.departement import Departement
from app.models.client.enseigne import Enseigne
from app.models.utilisateur.utilisateur import Utilisateur
from app.models.utilisateur.role import Role
from app.models.utilisateur.role_utilisateur import RoleUtilisateur
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
from app.models.fidelite.promo import Promo

DATABASE_URL = "mysql://dev:12345@localhost:3306/fromagerie_com"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def populate_db():
    try:
        # Creation de Departements
        departement1 = session.query(Departement).filter_by(nom="Hérault").first()
        if not departement1:
            departement1 = Departement(nom="Hérault", code="34")
            session.add(departement1)
        else:
            departement1.code = "34"

        departement2 = session.query(Departement).filter_by(nom="Haute-Garonne").first()
        if not departement2:
            departement2 = Departement(nom="Haute-Garonne", code="31")
            session.add(departement2)
        else:
            departement2.code = "31"
        session.commit()

        # Creation de Communes
        commune1 = session.query(Commune).filter_by(nom="Montpellier").first()
        if not commune1:
            commune1 = Commune(nom="Montpellier", code_postal="34000", departement_id=departement1.id)
            session.add(commune1)
        else:
            commune1.code_postal = "34000"
            commune1.departement_id = departement1.id

        commune2 = session.query(Commune).filter_by(nom="Toulouse").first()
        if not commune2:
            commune2 = Commune(nom="Toulouse", code_postal="31000", departement_id=departement2.id)
            session.add(commune2)
        else:
            commune2.code_postal = "31000"
            commune2.departement_id = departement2.id
        session.commit()

        # Creation de ProgrammeFidelite
        programme_fidelite1 = session.query(ProgrammeFidelite).filter_by(client_id=1).first()
        if not programme_fidelite1:
            programme_fidelite1 = ProgrammeFidelite(points=100.0, level="Silver")
            session.add(programme_fidelite1)
        else:
            programme_fidelite1.points = 100.0
            programme_fidelite1.level = "Silver"

        programme_fidelite2 = session.query(ProgrammeFidelite).filter_by(client_id=2).first()
        if not programme_fidelite2:
            programme_fidelite2 = ProgrammeFidelite(points=200.0, level="Gold")
            session.add(programme_fidelite2)
        else:
            programme_fidelite2.points = 200.0
            programme_fidelite2.level = "Gold"
        session.commit()

        # Creation de Clients
        client1 = session.query(Client).filter_by(nom="Client 1").first()
        if not client1:
            client1 = Client(
                genre="M",
                nom="Client 1",
                prenom="Toto",
                adresse1="Adresse 1",
                adresse2="Adresse 2",
                adresse3="Adresse 3",
                ville_id=1,
                telephone="0102030405",
                email="client1@example.com",
                portable="0607080910",
                newsletter=True,
                fidelite=programme_fidelite1.id
            )
            session.add(client1)
        else:
            client1.genre = client1.genre or "M"
            client1.prenom = client1.prenom or "Toto"
            client1.adresse1 = client1.adresse1 or "Adresse 1"
            client1.adresse2 = client1.adresse2 or "Adresse 2"
            client1.adresse3 = client1.adresse3 or "Adresse 3"
            client1.ville_id = 1
            client1.telephone = client1.telephone or "0102030405"
            client1.email = client1.email or "client1@example.com"
            client1.portable = client1.portable or "0607080910"
            client1.newsletter = client1.newsletter or True
            client1.fidelite = programme_fidelite1.id

        client2 = session.query(Client).filter_by(nom="Client 2").first()
        if not client2:
            client2 = Client(
                genre="F",
                nom="Client 2",
                prenom="Prenom 2",
                adresse1="Adresse 1",
                adresse2="Adresse 2",
                adresse3="Adresse 3",
                ville_id=2,
                telephone="0102030406",
                email="client2@example.com",
                portable="0607080911",
                newsletter=False,
                fidelite=programme_fidelite2.id
            )
            session.add(client2)
        else:
            client2.genre = client2.genre or "F"
            client2.prenom = client2.prenom or "Prenom 2"
            client2.adresse1 = client2.adresse1 or "Adresse 1"
            client2.adresse2 = client2.adresse2 or "Adresse 2"
            client2.adresse3 = client2.adresse3 or "Adresse 3"
            client2.ville_id = 2
            client2.telephone = client2.telephone or "0102030406"
            client2.email = client2.email or "client2@example.com"
            client2.portable = client2.portable or "0607080911"
            client2.newsletter = client2.newsletter or False
            client2.fidelite = programme_fidelite2.id
        session.commit()


        # Creation d'Utilisateurs
        utilisateur1 = session.query(Utilisateur).filter_by(nom_utilisateur="Utilisateur 1").first()
        if not utilisateur1:
            utilisateur1 = Utilisateur(
                nom_utilisateur="Utilisateur 1",
                prenom_utilisateur="Toto",
                username="Totoweb",
                couleur_fond_utilisateur=1,
                date_insc_utilisateur="2024-01-01"
            )
            session.add(utilisateur1)
        else:
            utilisateur1.prenom_utilisateur = utilisateur1.prenom_utilisateur or "Toto"
            utilisateur1.username = utilisateur1.username or "Totoweb"
            utilisateur1.couleur_fond_utilisateur = utilisateur1.couleur_fond_utilisateur or 1
            utilisateur1.date_insc_utilisateur = utilisateur1.date_insc_utilisateur or "2024-01-01"

        utilisateur2 = session.query(Utilisateur).filter_by(nom_utilisateur="Utilisateur 2").first()
        if not utilisateur2:
            utilisateur2 = Utilisateur(
                nom_utilisateur="Utilisateur 2",
                prenom_utilisateur="Tata",
                username="Tataweb",
                couleur_fond_utilisateur=2,
                date_insc_utilisateur="2024-01-02"
            )
            session.add(utilisateur2)
        else:
            utilisateur2.prenom_utilisateur = utilisateur2.prenom_utilisateur or "Tata"
            utilisateur2.username = utilisateur2.username or "Tataweb"
            utilisateur2.couleur_fond_utilisateur = utilisateur2.couleur_fond_utilisateur or 2
            utilisateur2.date_insc_utilisateur = utilisateur2.date_insc_utilisateur or "2024-01-02"
        session.commit()

        # Creation de Roles
        role1 = session.query(Role).filter_by(librole="Role 1").first()
        if not role1:
            role1 = Role(librole="Role 1")
            session.add(role1)
        role2 = session.query(Role).filter_by(librole="Role 2").first()
        if not role2:
            role2 = Role(librole="Role 2")
            session.add(role2)
        session.commit()

        # Creation de RoleUtilisateur
        utilisateur_role1 = session.query(RoleUtilisateur).filter_by(utilisateur_id=2, role_id=1).first()
        if not utilisateur_role1:
            utilisateur_role1 = RoleUtilisateur(utilisateur_id=2, role_id=1)
            session.add(utilisateur_role1)
        utilisateur_role2 = session.query(RoleUtilisateur).filter_by(utilisateur_id=1, role_id=2).first()
        if not utilisateur_role2:
            utilisateur_role2 = RoleUtilisateur(utilisateur_id=1, role_id=2)
            session.add(utilisateur_role2)
        session.commit()

        # Creation de Conditionnements
        conditionnement1 = session.query(Conditionnement).filter_by(libcondit="Conditionnement 1").first()
        if not conditionnement1:
            conditionnement1 = Conditionnement(libcondit="Conditionnement 1", poidscondit=1, prixcond=10.0, ordreimp=1)
            session.add(conditionnement1)
        else:
            conditionnement1.poidscondit = conditionnement1.poidscondit or 1
            conditionnement1.prixcond = conditionnement1.prixcond or 10.0
            conditionnement1.ordreimp = conditionnement1.ordreimp or 1

        conditionnement2 = session.query(Conditionnement).filter_by(libcondit="Conditionnement 2").first()
        if not conditionnement2:
            conditionnement2 = Conditionnement(libcondit="Conditionnement 2", poidscondit=2, prixcond=20.0, ordreimp=2)
            session.add(conditionnement2)
        else:
            conditionnement2.poidscondit = conditionnement2.poidscondit or 2
            conditionnement2.prixcond = conditionnement2.prixcond or 20.0
            conditionnement2.ordreimp = conditionnement2.ordreimp or 2
        session.commit()

        # Creation d'Objets
        objet1 = session.query(Objet).filter_by(libobj="Objet 1").first()
        if objet1:
            objet1.tailleobj = objet1.tailleobj or "Taille 1"
            objet1.puobj = objet1.puobj or 10.0000
            objet1.poidsobj = objet1.poidsobj or 1.0000
            objet1.indispobj = objet1.indispobj or 0
            objet1.o_imp = objet1.o_imp or 1
            objet1.o_aff = objet1.o_aff or 1
            objet1.o_cartp = objet1.o_cartp or 1
            objet1.points = objet1.points or 10
            objet1.o_ordre_aff = objet1.o_ordre_aff or 1
            objet1.conditionnement_id = objet1.conditionnement_id or conditionnement1.idcondit
        else:
            objet1 = Objet(
                libobj="Objet 1",
                tailleobj="Taille 1",
                puobj=10.0000,
                poidsobj=1.0000,
                indispobj=0,
                o_imp=1,
                o_aff=1,
                o_cartp=1,
                points=10,
                o_ordre_aff=1,
                conditionnement_id=conditionnement1.idcondit
            )
            session.add(objet1)

        objet2 = session.query(Objet).filter_by(libobj="Objet 2").first()
        if objet2:
            objet2.tailleobj = objet2.tailleobj or "Taille 2"
            objet2.puobj = objet2.puobj or 20.0000
            objet2.poidsobj = objet2.poidsobj or 2.0000
            objet2.indispobj = objet2.indispobj or 0
            objet2.o_imp = objet2.o_imp or 2
            objet2.o_aff = objet2.o_aff or 2
            objet2.o_cartp = objet2.o_cartp or 2
            objet2.points = objet2.points or 20
            objet2.o_ordre_aff = objet2.o_ordre_aff or 2
            objet2.conditionnement_id = objet2.conditionnement_id or conditionnement2.idcondit
        else:
            objet2 = Objet(
                libobj="Objet 2",
                tailleobj="Taille 2",
                puobj=20.0000,
                poidsobj=2.0000,
                indispobj=0,
                o_imp=2,
                o_aff=2,
                o_cartp=2,
                points=20,
                o_ordre_aff=2,
                conditionnement_id=conditionnement2.idcondit
            )
            session.add(objet2)
        session.commit()

        # Creation de ObjetCond
        objet_cond1 = session.query(ObjetCond).filter_by(codobj=objet1.codobj, codcond=conditionnement1.idcondit).first()
        if not objet_cond1:
            objet_cond1 = ObjetCond(qteobjdeb=10, qteobjfin=20, codobj=objet1.codobj, codcond=conditionnement1.idcondit)
            session.add(objet_cond1)
        else:
            objet_cond1.qteobjdeb = objet_cond1.qteobjdeb or 10
            objet_cond1.qteobjfin = objet_cond1.qteobjfin or 20

        objet_cond2 = session.query(ObjetCond).filter_by(codobj=objet2.codobj, codcond=conditionnement2.idcondit).first()
        if not objet_cond2:
            objet_cond2 = ObjetCond(qteobjdeb=15, qteobjfin=25, codobj=objet2.codobj, codcond=conditionnement2.idcondit)
            session.add(objet_cond2)
        else:
            objet_cond2.qteobjdeb = objet_cond2.qteobjdeb or 15
            objet_cond2.qteobjfin = objet_cond2.qteobjfin or 25
        session.commit()

        # Creation de Poids
        poids1 = session.query(Poids).filter_by(valmin=10, valtimbre=20).first()
        if not poids1:
            poids1 = Poids(valmin=10, valtimbre=20)
            session.add(poids1)
        else:
            poids1.valmin = poids1.valmin or 10
            poids1.valtimbre = poids1.valtimbre or 20

        poids2 = session.query(Poids).filter_by(valmin=15, valtimbre=25).first()
        if not poids2:
            poids2 = Poids(valmin=15, valtimbre=25)
            session.add(poids2)
        else:
            poids2.valmin = poids2.valmin or 15
            poids2.valtimbre = poids2.valtimbre or 25
        session.commit()

        # Creation de Vignettes
        vignette1 = session.query(Vignette).filter_by(valmin=10, valtimbre=20).first()
        if not vignette1:
            vignette1 = Vignette(valmin=10, valtimbre=20)
            session.add(vignette1)
        else:
            vignette1.valmin = vignette1.valmin or 10
            vignette1.valtimbre = vignette1.valtimbre or 20

        vignette2 = session.query(Vignette).filter_by(valmin=15, valtimbre=25).first()
        if not vignette2:
            vignette2 = Vignette(valmin=15, valtimbre=25)
            session.add(vignette2)
        else:
            vignette2.valmin = vignette2.valmin or 15
            vignette2.valtimbre = vignette2.valtimbre or 25
        session.commit()

        # Creation de Transactions
        transaction1 = session.query(Transaction).filter_by(name="Transaction 1").first()
        if not transaction1:
            transaction1 = Transaction(
                user_id=client1.codcli,
                amount_spent=100.0,
                points_earned=10.0,
                name="Transaction 1"
            )
            session.add(transaction1)
        else:
            transaction1.user_id = client1.codcli
            transaction1.amount_spent = 100.0
            transaction1.points_earned = 10.0

        transaction2 = session.query(Transaction).filter_by(name="Transaction 2").first()
        if not transaction2:
            transaction2 = Transaction(
                user_id=client2.codcli,
                amount_spent=200.0,
                points_earned=20.0,
                name="Transaction 2"
            )
            session.add(transaction2)
        else:
            transaction2.user_id = client2.codcli
            transaction2.amount_spent = 200.0
            transaction2.points_earned = 20.0
        session.commit()

        # Creation de Commandes
        commande1 = session.query(Commande).filter_by(name="Commande 1").first()
        if not commande1:
            commande1 = Commande(
                datcde="2023-01-01",
                codcli=client1.codcli,
                timbrecli=1.0,
                timbre_cde=1.0,
                nbcolis=1,
                cheqcli=1.0,
                idcondit=conditionnement1.idcondit,
                cdeComt="Commentaire 1",
                barchive=0,
                bstock=0,
                name="Commande 1"
            )
            session.add(commande1)
        else:
            commande1.datcde = "2023-01-01"
            commande1.codcli = client1.codcli
            commande1.timbrecli = 1.0
            commande1.timbre_cde = 1.0
            commande1.nbcolis = 1
            commande1.cheqcli = 1.0
            commande1.idcondit = conditionnement1.idcondit
            commande1.cdeComt = "Commentaire 1"
            commande1.barchive = 0
            commande1.bstock = 0

        commande2 = session.query(Commande).filter_by(name="Commande 2").first()
        if not commande2:
            commande2 = Commande(
                datcde="2023-01-02",
                codcli=client2.codcli,
                timbrecli=2.0,
                timbre_cde=2.0,
                nbcolis=2,
                cheqcli=2.0,
                idcondit=conditionnement2.idcondit,
                cdeComt="Commentaire 2",
                barchive=0,
                bstock=0,
                name="Commande 2"
            )
            session.add(commande2)
        else:
            commande2.datcde = "2023-01-02"
            commande2.codcli = client2.codcli
            commande2.timbrecli = 2.0
            commande2.timbre_cde = 2.0
            commande2.nbcolis = 2
            commande2.cheqcli = 2.0
            commande2.idcondit = conditionnement2.idcondit
            commande2.cdeComt = "Commentaire 2"
            commande2.barchive = 0
            commande2.bstock = 0
        session.commit()

        # Creation de  Details
        detail1 = session.query(Detail).filter_by(name="Detail 1").first()
        if not detail1:
            detail1 = Detail(
                codcde=commande1.codcde,
                qte=1,
                colis=1,
                commentaire="Commentaire 1",
                name="Detail 1"
            )
            session.add(detail1)
        else:
            detail1.codcde = commande1.codcde
            detail1.qte = 1
            detail1.colis = 1
            detail1.commentaire = "Commentaire 1"

        detail2 = session.query(Detail).filter_by(name="Detail 2").first()
        if not detail2:
            detail2 = Detail(
                codcde=commande2.codcde,
                qte=2,
                colis=2,
                commentaire="Commentaire 2",
                name="Detail 2"
            )
            session.add(detail2)
        else:
            detail2.codcde = commande2.codcde
            detail2.qte = 2
            detail2.colis = 2
            detail2.commentaire = "Commentaire 2"
        session.commit()

        # Creation de DetailObjet
        detail_objet1 = session.query(DetailObjet).filter_by(name="DetailObjet 1").first()
        if not detail_objet1:
            detail_objet1 = DetailObjet(
                detail_id=detail1.id,
                objet_id=objet1.codobj,
                name="DetailObjet 1"
            )
            session.add(detail_objet1)
        else:
            detail_objet1.detail_id = detail1.id
            detail_objet1.objet_id = objet1.codobj

        detail_objet2 = session.query(DetailObjet).filter_by(name="DetailObjet 2").first()
        if not detail_objet2:
            detail_objet2 = DetailObjet(
                detail_id=detail2.id,
                objet_id=objet2.codobj,
                name="DetailObjet 2"
            )
            session.add(detail_objet2)
        else:
            detail_objet2.detail_id = detail2.id
            detail_objet2.objet_id = objet2.codobj
        session.commit()

        # Creation d'enseignes
        enseigne1 = session.query(Enseigne).filter_by(libelle="Enseigne 1").first()
        if not enseigne1:
            enseigne1 = Enseigne(
                libelle="Enseigne 1",
                ville="Ville 1",
                departement_id=departement1.id
            )
            session.add(enseigne1)
        else:
            enseigne1.ville = "Ville 1"
            enseigne1.departement_id = departement1.id

        enseigne2 = session.query(Enseigne).filter_by(libelle="Enseigne 2").first()
        if not enseigne2:
            enseigne2 = Enseigne(
                libelle="Enseigne 2",
                ville="Ville 2",
                departement_id=departement2.id
            )
            session.add(enseigne2)
        else:
            enseigne2.ville = "Ville 2"
            enseigne2.departement_id = departement2.id
        session.commit()

        # Creation de Promo
        promo1 = session.query(Promo).filter_by(name="Promo 1").first()
        if promo1:
            promo1.discount_percentage = 10.0
            promo1.points_required = 100.0
        else:
            promo1 = Promo(
                name="Promo 1",
                discount_percentage=10.0,
                points_required=100.0
            )
            session.add(promo1)

        promo2 = session.query(Promo).filter_by(name="Promo 2").first()
        if promo2:
            promo2.discount_percentage = 20.0
            promo2.points_required = 200.0
        else:
            promo2 = Promo(
                name="Promo 2",
                discount_percentage=20.0,
                points_required=200.0
            )
            session.add(promo2)

        session.commit()

        # Creation de Bonus
        bonus1 = session.query(Bonus).filter_by(name="Bonus 1").first()
        if not bonus1:
            bonus1 = Bonus(
                user_id=utilisateur1.code_utilisateur,
                bonus_type="WELCOME",
                points=100.0,
                name="Bonus 1"
            )
            session.add(bonus1)
        else:
            bonus1.user_id = utilisateur1.code_utilisateur
            bonus1.bonus_type = "WELCOME"
            bonus1.points = 100.0

        bonus2 = session.query(Bonus).filter_by(name="Bonus 2").first()
        if not bonus2:
            bonus2 = Bonus(
                user_id=utilisateur2.code_utilisateur,
                bonus_type="ANNIVERSARY",
                points=200.0,
                name="Bonus 2"
            )
            session.add(bonus2)
        else:
            bonus2.user_id = utilisateur2.code_utilisateur
            bonus2.bonus_type = "ANNIVERSARY"
            bonus2.points = 200.0

        session.commit()

        print("Base de données remplie avec succès!")
    except Exception as e:
        session.rollback()
        print(f"Une erreur est survenue: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    populate_db()