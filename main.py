from fastapi import FastAPI
from app.routers import commande, detail, detail_objet, utilisateurs, roles

app = FastAPI()

app.include_router(commande.router, prefix="/api", tags=["commandes"])
app.include_router(detail.router, prefix="/api", tags=["details"])
app.include_router(detail_objet.router, prefix="/api", tags=["detail_objets"])

app.include_router(utilisateurs.router, prefix="/utilisateurs", tags=["Utilisateurs"])

app.include_router(roles.router, prefix="/roles", tags=["Roles"])
@app.get("/")
def read_root():
    return {"Bienvenue dans Digicheese !"}