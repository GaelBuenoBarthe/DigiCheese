from fastapi import FastAPI
from app.routers import commande, detail, detail_objet, utilisateurs, roles, vignette, poids, objet_cond

app = FastAPI()

app.include_router(commande.router, prefix="/api", tags=["commandes"])
app.include_router(detail.router, prefix="/api", tags=["details"])

app.include_router(detail_objet.router, prefix="/detail_objets", tags=["DetailObjets"])

app.include_router(utilisateurs.router, prefix="/utilisateurs", tags=["Utilisateurs"])

app.include_router(roles.router, prefix="/roles", tags=["Roles"])

app.include_router(vignette.router, prefix="/vignettes", tags=["Vignettes"])
app.include_router(poids.router, prefix="/poids", tags=["Poids"])
app.include_router(objet_cond.router, prefix="/objet-cond", tags=["ObjetCond"])
@app.get("/")
def read_root():
    return {"Bienvenue dans Digicheese !"}