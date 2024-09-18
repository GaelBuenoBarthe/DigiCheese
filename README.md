# Projet de Gestion de Fidélité Digicheese

## Description

Ce projet est une API développée avec FastAPI qui fournit des fonctionnalités de gestion de programmes de fidélité pour des utilisateurs ainsi que la gestion des commandes et des clients. Il s'intègre avec une base de données SQLAlchemy et offre une série de points de terminaison pour gérer ces entités, y compris des promotions et des bonus dans le cadre des programmes de fidélité.

## Fonctionnalités principales

- Gestion des programmes de fidélité
- Gestion des commandes
- Gestion des clients
- Calcul des points de fidélité
- Attribution de bonus et vérification des promotions
- Mécanismes CRUD pour la plupart des entités

## Prérequis

- Python 3.12+
- FastAPI
- SQLAlchemy
- MySQL
- Pydantic

## Installation

1. Clonez le dépôt :

    ```bash
    git clone https://github.com/GaelBuenoBarthe/DigiCheese.git
    cd digicheese
    ```

2. Créez et configurez un fichier `.env` avec les informations de votre base de données :

    ```env
    DATABASE_URL="mysql://dev:12345@localhost:3306/fromagerie_com"
    ```

3. Installez les dépendances en exécutant :

    ```bash
    pip install -r requirements.txt
    ```

## Création de la Base de Données

### Utilisation du Dump SQL

1. Ouvrez PowerShell et connectez-vous à MySQL :

    ```bash
    mysql -u root -p
    ```

2. Créez la base de données et l'utilisateur :

    ```sql
    CREATE DATABASE nom_de_la_base;
    CREATE USER 'dev'@'localhost' IDENTIFIED BY '12345';
    GRANT ALL PRIVILEGES ON nom_de_la_base.* TO 'dev'@'localhost';
    FLUSH PRIVILEGES;
    ```

3. Importez le dump SQL :

    ```bash
    mysql -u username -p fromagerie_com < ressource/db_dump.sql
    ```

### Utilisation de `main.py` pour Créer les Tables

1. Exécutez le script `main.py` pour créer les tables :

    ```bash
    python main.py
    ```

### Remplissage de la Base de Données

1. Exécutez le script `populate.py` pour remplir la base de données :

    ```bash
    python populate.py
    ```

## Démarrage du Projet

1. Lancez le serveur :

    ```bash
    uvicorn app.main:app --reload
    ```

2. Le serveur sera accessible à l'adresse [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Routes Disponibles

### Programme de Fidélité

1. **Voir le programme de fidélité d 'un client**
   - **Route:** `GET/fidelite/fidelite/{client_id}`
   - **Description:** Récupére le programme de fidélité d'un client.
   - **Corps de la requête:**
     ```json
     {
       "user_id": 1,
     }
     ```
   - **Réponse:**
     ```json
  {
    "id": 1,
    "user_id": 1,
    "points": 100,
    "level": "Silver"
  }
     ```

### Gestion des Commandes

1. **Créer une commande**
   - **Route:** `POST /commandes/`
   - **Description:** Crée une nouvelle commande.
   - **Corps de la requête:**
     ```json
    {
      "datcde": "2024-09-18",
      "codcli": 0,
      "timbrecli": 0,
      "timbre_cde": 0,
      "nbcolis": 1,
      "cheqcli": 0,
      "idcondit": 0,
      "cdeComt": "string",
      "barchive": 0,
      "bstock": 0
    }
     ```
   - **Réponse:**
     ```json
    {
      "datcde": "2024-09-18",
      "codcli": 0,
      "timbrecli": 0,
      "timbre_cde": 0,
      "nbcolis": 1,
      "cheqcli": 0,
      "idcondit": 0,
      "cdeComt": "string",
      "barchive": 0,
      "bstock": 0,
     "codcde": 0
    }
     ```

2. **Récupérer les commandes**
   - **Route:** `GET /commandes`
   - **Description:** Récupère les détails des commandes.
   - **Réponse:**
     ```json
 {
    "datcde": "2023-01-01",
    "codcli": 1,
    "timbrecli": 1,
    "timbre_cde": 1,
    "nbcolis": 1,
    "cheqcli": 1,
    "idcondit": 1,
    "cdeComt": "Commentaire 1",
    "barchive": 0,
    "bstock": 0,
    "codcde": 1
  },
  {
    "datcde": "2023-01-02",
    "codcli": 2,
    "timbrecli": 2,
    "timbre_cde": 2,
    "nbcolis": 2,
    "cheqcli": 2,
    "idcondit": 2,
    "cdeComt": "Commentaire 2",
    "barchive": 0,
    "bstock": 0,
    "codcde": 2
  }
     ```


### Gestion des Clients

1. **Récupérer tous les clients**
   - **Route:** `GET /clients/`
   - **Description:** Récupère une liste paginée de tous les clients.
   - **Réponse:**
     ```json
     [
{
    "codcli": 1,
    "genre": "M",
    "nom": "Client 1",
    "prenom": "Toto",
    "adresse1": "Adresse 1",
    "adresse2": "Adresse 2",
    "adresse3": "Adresse 3",
    "ville_id": 1,
    "telephone": "0102030405",
    "email": "client1@example.com",
    "portable": "0607080910",
    "newsletter": true
  },
  {
    "codcli": 2,
    "genre": "F",
    "nom": "Client 2",
    "prenom": "Prenom 2",
    "adresse1": "Adresse 1",
    "adresse2": "Adresse 2",
    "adresse3": "Adresse 3",
    "ville_id": 2,
    "telephone": "0102030406",
    "email": "client2@example.com",
    "portable": "0607080911",
    "newsletter": false
  },
     ]
     ```

2. **Créer un client**
   - **Route:** `POST /clients/`
   - **Description:** Crée un nouveau client.
   - **Corps de la requête:**
     ```json
{
  "genre": "string",
  "nom": "string",
  "prenom": "string",
  "adresse1": "string",
  "adresse2": "string",
  "adresse3": "string",
  "ville_id": 0,
  "telephone": "string",
  "email": "user@example.com",
  "portable": "string",
  "newsletter": true
}
     ```
   - **Réponse:**
     ```json
{
  "codcli": 0,
  "genre": "string",
  "nom": "string",
  "prenom": "string",
  "adresse1": "string",
  "adresse2": "string",
  "adresse3": "string",
  "ville_id": 0,
  "telephone": "string",
  "email": "user@example.com",
  "portable": "string",
  "newsletter": true
}
     ```



4. **Supprimer un client**
   - **Route:** `DELETE /clients/{id}`
   - **Description:** Supprime un client existant par son ID.
   - **Réponse:**
     ```json
     {
       "message": "Client supprimé avec succès"
     }
     ```

## Schémas et Modèles

Le projet utilise des modèles SQLAlchemy pour gérer les interactions avec la base de données, ainsi que des schémas Pydantic pour la validation des données d'entrée/sortie dans les routes FastAPI.

### Exemple de Modèle : ProgrammeFidelite

```python
class ProgrammeFidelite(Base):
    __tablename__ = "programme_fidelite"

    id = Column(Integer, primary_key=True, index=True)
    points = Column(Numeric(precision=10, scale=2), default=0)
    level = Column(String(50))  # Silver, Gold, etc.

    clients = relationship("Client", secondary=client_programme_fidelite, back_populates="programmes_fidelite")

```

uvicorn app.main:app --reload
Le serveur sera accessible à l'adresse http://127.0.0.1:8000.

Tests
Pour exécuter les tests, utilisez pytest :

bash
Copy code
pytest
Contributeurs
Bernardo Estacio Abreu
Gaël Bueno-Barthe
Fabrice Bellin
Filip Dabrowski
Marwa Benyahia
Licence


Cela récapitule tout ce qui a été fait, y compris la gestion des commandes, clients, programmes de fidélité, bonus et promotions, ainsi que la configuration nécessaire pour démarrer le projet.