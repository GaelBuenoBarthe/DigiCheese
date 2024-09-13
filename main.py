from fastapi import FastAPI
from app.routers import commande, detail, detail_objet, client, commune, departement, enseigne

app = FastAPI()

app.include_router(commande.router, prefix="/api", tags=["commandes"])
app.include_router(detail.router, prefix="/api", tags=["details"])
app.include_router(detail_objet.router, prefix="/api", tags=["detail_objets"])
app.include_router(client.router, prefix="/api/v1", tags=["clients"])
app.include_router(commune.router, prefix="/api/v1", tags=["communes"])
app.include_router(departement.router, prefix="/api/v1", tags=["departements"])
app.include_router(enseigne.router, prefix="/api/v1", tags=["enseignes"])

@app.get("/")
def read_root():
    return {"Bienvenue dans Digicheese !"}