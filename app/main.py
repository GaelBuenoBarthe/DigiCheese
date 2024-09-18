import os

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from starlette.staticfiles import StaticFiles

from app.routers.utilisateur import roles_router, utilisateurs_router
from app.routers.fidelite import programme_fidelite_router
from app.routers.stock import objet_cond_router, poids_router, vignette_router, conditionnement_router
from app.routers.commande import commande_router, detail_objet_router, detail_router
from app.routers.client import clients_router, commune_router, departement_router, enseigne_router
from app.database import init_db

app = FastAPI()

#Chemins pour les fichiers statiques
static_dir = os.path.join(os.path.dirname(__file__), '..', 'static')
app.mount("/static", StaticFiles(directory=static_dir), name="static")

templates = Jinja2Templates(directory="templates")

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
app.include_router(conditionnement_router.router, prefix="/conditionnement", tags=["Conditionnements"])

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/docs", include_in_schema=False, response_class=HTMLResponse)
async def custom_swagger_ui_html(request: Request):
    print("Custom Swagger UI endpoint called")
    return templates.TemplateResponse("swagger_custom.html", {"request": request})

init_db()