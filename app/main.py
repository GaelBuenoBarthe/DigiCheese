from fastapi import FastAPI

from app.models.fidelite.ProgrammeFidelite import ProgrammeFidelite
from app.routers import Commande, Detail, DetailObjet, Utilisateurs, Roles, Vignette, Poids, ObjetCond, Client
from app.schemas.Commune import Commune
from app.schemas.Departement import Departement
from app.schemas.Enseigne import Enseigne

app = FastAPI()

app.include_router(Commande.router, prefix="/commande", tags=["commandes"])
app.include_router(Detail.router, prefix="/detail", tags=["details"])
app.include_router(DetailObjet.router, prefix="/detail_objets", tags=["DetailObjets"])
app.include_router(Utilisateurs.router, prefix="/utilisateurs", tags=["Utilisateurs"])
app.include_router(Roles.router, prefix="/roles", tags=["Roles"])
app.include_router(Vignette.router, prefix="/vignettes", tags=["Vignettes"])
app.include_router(Poids.router, prefix="/poids", tags=["Poids"])
app.include_router(ObjetCond.router, prefix="/objet-cond", tags=["ObjetCond"])
app.include_router(ProgrammeFidelite.router, prefix="/fidelite", tags=["Fidelite"])
app.include_router(Client.router, prefix="/client", tags=["Client"])
app.include_router(Commune.Router, prefix="/commune", tags=["Commune"])
app.include_router(Departement.router, prefix="/department", tags=["Department"])
app.include_router(Enseigne.router, prefix="/enseigne", tags=["Enseigne"])
@app.get("/")
def read_root():
    return {"Bienvenue dans Digicheese !"}