from fastapi import FastAPI

from app.models.fidelite.programme_fidelite import ProgrammeFidelite
from app.routers import commande, detail, detail_objet, utilisateurs, roles, vignette, poids, objet_cond, clients, \
    communes, departement, programme_fidelite, enseigne
from app.schemas.commune import Commune
from app.schemas.departement import Departement
from app.schemas.enseigne import Enseigne
from app.infrastructure.api.client import client_controller, commune_controller, departement_controller, enseigne_controller
from app.infrastructure.api.commande import commandes_controller, details_controller, details_objet_controller
from app.infrastructure.api.fidelite import programmes_fidelite_controller
from app.infrastructure.api.stock import objet_conds_controller, objets_controller, poids_controller, vignettes_controller
from app.infrastructure.api.utilisateur import roles_controller, utilisateurs_controller

app = FastAPI()

app.include_router(commande.router, prefix="/commandes", tags=["commandes"])
app.include_router(detail.router, prefix="/details", tags=["details"])
app.include_router(detail_objet.router, prefix="/detail_objets", tags=["DetailObjets"])
app.include_router(utilisateurs.router, prefix="/utilisateurs", tags=["Utilisateurs"])
app.include_router(roles.router, prefix="/roles", tags=["Roles"])
app.include_router(vignette.router, prefix="/vignettes", tags=["Vignettes"])
app.include_router(poids.router, prefix="/poids", tags=["Poids"])
app.include_router(objet_cond.router, prefix="/objet-cond", tags=["ObjetCond"])
app.include_router(programme_fidelite.router, prefix="/fidelite", tags=["Fidelite"])
app.include_router(clients.router, prefix="/Clients", tags=["Clients"])
app.include_router(communes.router, prefix="/commune", tags=["Commune"])
app.include_router(departement.router, prefix="/department", tags=["Department"])
app.include_router(enseigne.router, prefix="/enseigne", tags=["Enseigne"])
@app.get("/")
def read_root():
    return {"Bienvenue dans Digicheese !"}