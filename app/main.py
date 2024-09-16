from fastapi import FastAPI

from app.routers.utilisateur import roles_router, utilisateurs_router
from app.routers.fidelite import programme_fidelite_router
from app.routers.stock import objet_cond_router, poids_router, vignette_router
from app.routers.commande import commande_router, detail_objet_router, detail_router
from app.routers.client import clients_router, commune_router, departement_router, enseigne_router
from app.database import init_db

app = FastAPI()

app.include_router(commande_router.router, prefix="/commandes", tags=["commandes"])
app.include_router(detail_router.router, prefix="/details", tags=["details"])
app.include_router(detail_objet_router.router, prefix="/detail_objets", tags=["DetailObjets"])
app.include_router(utilisateurs_router.router, prefix="/utilisateurs", tags=["Utilisateurs"])
app.include_router(roles_router.router, prefix="/roles", tags=["Roles"])
app.include_router(vignette_router.router, prefix="/vignettes", tags=["Vignettes"])
app.include_router(poids_router.router, prefix="/poids", tags=["Poids"])
app.include_router(objet_cond_router.router, prefix="/objet-cond", tags=["ObjetCond"])
app.include_router(programme_fidelite_router.router, prefix="/fidelite", tags=["Fidelite"])
app.include_router(clients_router.router, prefix="/client", tags=["Clients"])
app.include_router(commune_router.router, prefix="/commune", tags=["Communes"])
app.include_router(departement_router.router, prefix="/department", tags=["Departments"])
app.include_router(enseigne_router.router, prefix="/enseigne", tags=["Enseignes"])

@app.get("/")
def read_root():
    return {"Bienvenue dans Digicheese !"}
init_db()