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
            utilisateur1.prenom_utilisateur = "Toto"
            utilisateur1.username = "Totoweb"
            utilisateur1.couleur_fond_utilisateur = 1
            utilisateur1.date_insc_utilisateur = "2024-01-01"

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
            utilisateur2.prenom_utilisateur = "Tata"
            utilisateur2.username = "Tataweb"
            utilisateur2.couleur_fond_utilisateur = 2
            utilisateur2.date_insc_utilisateur = "2024-01-02"
        session.commit()

        role1 = session.query(Role).filter_by(librole="Role 1").first()
        if not role1:
            role1 = Role(librole="Role 1")
            session.add(role1)
        role2 = session.query(Role).filter_by(librole="Role 2").first()
        if not role2:
            role2 = Role(librole="Role 2")
            session.add(role2)
        session.commit()

        utilisateur_role1 = session.query(RoleUtilisateur).filter_by(utilisateur_id=2, role_id=1).first()
        if not utilisateur_role1:
            utilisateur_role1 = RoleUtilisateur(utilisateur_id=2, role_id=1)
            session.add(utilisateur_role1)
        utilisateur_role2 = session.query(RoleUtilisateur).filter_by(utilisateur_id=1, role_id=2).first()
        if not utilisateur_role2:
            utilisateur_role2 = RoleUtilisateur(utilisateur_id=1, role_id=2)
            session.add(utilisateur_role2)
        session.commit()

        conditionnement1 = session.query(Conditionnement).filter_by(libcondit="Conditionnement 1").first()
        if not conditionnement1:
            conditionnement1 = Conditionnement(libcondit="Conditionnement 1", poidscondit=1, prixcond=10.0, ordreimp=1)
            session.add(conditionnement1)
        conditionnement2 = session.query(Conditionnement).filter_by(libcondit="Conditionnement 2").first()
        if not conditionnement2:
            conditionnement2 = Conditionnement(libcondit="Conditionnement 2", poidscondit=2, prixcond=20.0, ordreimp=2)
            session.add(conditionnement2)
        session.commit()

        objet1 = session.query(Objet).filter_by(libobj="Objet 1").first()
        if objet1:
            objet1.tailleobj = "Taille 1"
            objet1.puobj = 10.0000
            objet1.poidsobj = 1.0000
            objet1.indispobj = 0
            objet1.o_imp = 1
            objet1.o_aff = 1
            objet1.o_cartp = 1
            objet1.points = 10
            objet1.o_ordre_aff = 1
            objet1.conditionnement_id = conditionnement1.idcondit
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
            objet2.tailleobj = "Taille 2"
            objet2.puobj = 20.0000
            objet2.poidsobj = 2.0000
            objet2.indispobj = 0
            objet2.o_imp = 2
            objet2.o_aff = 2
            objet2.o_cartp = 2
            objet2.points = 20
            objet2.o_ordre_aff = 2
            objet2.conditionnement_id = conditionnement2.idcondit
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

        objet_cond1 = session.query(ObjetCond).filter_by(codobj=objet1.codobj, codcond=conditionnement1.idcondit).first()
        if not objet_cond1:
            objet_cond1 = ObjetCond(qteobjdeb=10, qteobjfin=20, codobj=objet1.codobj, codcond=conditionnement1.idcondit)
            session.add(objet_cond1)
        objet_cond2 = session.query(ObjetCond).filter_by(codobj=objet2.codobj, codcond=conditionnement2.idcondit).first()
        if not objet_cond2:
            objet_cond2 = ObjetCond(qteobjdeb=15, qteobjfin=25, codobj=objet2.codobj, codcond=conditionnement2.idcondit)
            session.add(objet_cond2)
        session.commit()

        poids1 = session.query(Poids).filter_by(valmin=10, valtimbre=20).first()
        if not poids1:
            poids1 = Poids(valmin=10, valtimbre=20)
            session.add(poids1)
        poids2 = session.query(Poids).filter_by(valmin=15, valtimbre=25).first()
        if not poids2:
            poids2 = Poids(valmin=15, valtimbre=25)
            session.add(poids2)
        session.commit()

        vignette1 = session.query(Vignette).filter_by(valmin=10, valtimbre=20).first()
        if not vignette1:
            vignette1 = Vignette(valmin=10, valtimbre=20)
            session.add(vignette1)
        vignette2 = session.query(Vignette).filter_by(valmin=15, valtimbre=25).first()
        if not vignette2:
            vignette2 = Vignette(valmin=15, valtimbre=25)
            session.add(vignette2)
        session.commit()

        programme_fidelite1 = session.query(ProgrammeFidelite).filter_by(client_id=1).first()
        if not programme_fidelite1:
            programme_fidelite1 = ProgrammeFidelite(client_id=1, points=100.0, level="Silver")
            session.add(programme_fidelite1)
        programme_fidelite2 = session.query(ProgrammeFidelite).filter_by(client_id=2).first()
        if not programme_fidelite2:
            programme_fidelite2 = ProgrammeFidelite(client_id=2, points=200.0, level="Gold")
            session.add(programme_fidelite2)
        session.commit()

        bonus1 = session.query(Bonus).filter_by(user_id=1, bonus_type="WELCOME").first()
        if not bonus1:
            bonus1 = Bonus(user_id=1, bonus_type="WELCOME", points=10.0, name="Bonus 1")
            session.add(bonus1)
        bonus2 = session.query(Bonus).filter_by(user_id=2, bonus_type="ANNIVERSARY").first()
        if not bonus2:
            bonus2 = Bonus(user_id=2, bonus_type="ANNIVERSARY", points=20.0, name="Bonus 2")
            session.add(bonus2)
        session.commit()

        transaction1 = session.query(Transaction).filter_by(user_id=1, name="Transaction 1").first()
        if not transaction1:
            transaction1 = Transaction(user_id=1, amount_spent=100.0, points_earned=10.0, name="Transaction 1")
            session.add(transaction1)
        transaction2 = session.query(Transaction).filter_by(user_id=2, name="Transaction 2").first()
        if not transaction2:
            transaction2 = Transaction(user_id=2, amount_spent=200.0, points_earned=20.0, name="Transaction 2")
            session.add(transaction2)
        session.commit()

        commande1 = session.query(Commande).filter_by(name="Commande 1").first()
        if not commande1:
            commande1 = Commande(datcde="2023-01-01", codcli=1, timbrecli=1.0, timbre_cde=1.0, nbcolis=1,
                                cheqcli=1.0, idcondit=1, cdeComt="Commentaire 1", barchive=0, bstock=0, name="Commande 1")
            session.add(commande1)
        commande2 = session.query(Commande).filter_by(name="Commande 2").first()
        if not commande2:
            commande2 = Commande(datcde="2023-01-02", codcli=2, timbrecli=2.0, timbre_cde=2.0, nbcolis=2,
                                cheqcli=2.0, idcondit=2, cdeComt="Commentaire 2", barchive=0, bstock=0, name="Commande 2")
            session.add(commande2)
        session.commit()

        detail1 = session.query(Detail).filter_by(name="Detail 1").first()
        if not detail1:
            detail1 = Detail(codcde=1, qte=1, colis=1, commentaire="Commentaire 1", name="Detail 1")
            session.add(detail1)
        detail2 = session.query(Detail).filter_by(name="Detail 2").first()
        if not detail2:
            detail2 = Detail(codcde=2, qte=2, colis=2, commentaire="Commentaire 2", name="Detail 2")
            session.add(detail2)
        session.commit()

        detail_objet1 = session.query(DetailObjet).filter_by(name="DetailObjet 1").first()
        if not detail_objet1:
            detail_objet1 = DetailObjet(detail_id=1, objet_id=objet1.codobj, name="DetailObjet 1")
            session.add(detail_objet1)
        detail_objet2 = session.query(DetailObjet).filter_by(name="DetailObjet 2").first()
        if not detail_objet2:
            detail_objet2 = DetailObjet(detail_id=2, objet_id=objet2.codobj, name="DetailObjet 2")
            session.add(detail_objet2)
        session.commit()

        promo1 = session.query(Promo).filter_by(name="Promo 1").first()
        if promo1:
            promo1.discount_percentage = 10.0
            promo1.points_required = 100.0
        else:
            promo1 = Promo(name="Promo 1", discount_percentage=10.0, points_required=100.0)
            session.add(promo1)

        promo2 = session.query(Promo).filter_by(name="Promo 2").first()
        if promo2:
            promo2.discount_percentage = 20.0
            promo2.points_required = 200.0
        else:
            promo2 = Promo(name="Promo 2", discount_percentage=20.0, points_required=200.0)
            session.add(promo2)

        enseigne1 = session.query(Enseigne).filter_by(libelle="Enseigne 1").first()
        if not enseigne1:
            enseigne1 = Enseigne(libelle="Enseigne 1", ville="Ville 1", departement_id=1)
            session.add(enseigne1)
        else:
            enseigne1.departement_id = departement1.id

        enseigne2 = session.query(Enseigne).filter_by(libelle="Enseigne 2").first()
        if not enseigne2:
            enseigne2 = Enseigne(libelle="Enseigne 2", ville="Ville 2", departement_id=2)
            session.add(enseigne2)
        else:
            enseigne2.departement_id = departement2.id
        session.commit()

        session.commit()

        print("Base de données remplie avec succès!")
    except Exception as e:
        session.rollback()
        print(f"Une erreur est survenue: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    populate_db()