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

1. **Ajouter une transaction**
   - **Route:** `POST /programmefidelite/transaction`
   - **Description:** Ajoute une transaction à un utilisateur et calcule les points de fidélité gagnés.
   - **Corps de la requête:**
     ```json
     {
       "user_id": 1,
       "amount_spent": 100
     }
     ```
   - **Réponse:**
     ```json
     {
       "user_id": 1,
       "points_earned": 10,
       "total_points": 110
     }
     ```

2. **Ajouter un bonus**
   - **Route:** `POST /programmefidelite/bonus`
   - **Description:** Ajoute un bonus de points à un utilisateur.
   - **Corps de la requête:**
     ```json
     {
       "user_id": 1,
       "bonus_type": "Anniversaire",
       "points": 50
     }
     ```
   - **Réponse:**
     ```json
     {
       "user_id": 1,
       "bonus_type": "Anniversaire",
       "points": 50,
       "total_points": 160
     }
     ```

3. **Vérification de l'éligibilité à une promotion**
   - **Route:** `GET /programmefidelite/promo/{user_id}/{promo_id}`
   - **Description:** Vérifie si un utilisateur est éligible à une promotion donnée selon ses points de fidélité.
   - **Réponse:**
     ```json
     {
       "eligible": true,
       "promo": {
         "id": 1,
         "description": "10% de réduction",
         "points_required": 100
       }
     }
     ```

### Gestion des Commandes

1. **Créer une commande**
   - **Route:** `POST /commandes/`
   - **Description:** Crée une nouvelle commande.
   - **Corps de la requête:**
     ```json
     {
       "client_id": 1,
       "produits": [
         {
           "produit_id": 101,
           "quantité": 2
         }
       ]
     }
     ```
   - **Réponse:**
     ```json
     {
       "id": 1,
       "client_id": 1,
       "produits": [
         {
           "produit_id": 101,
           "quantité": 2
         }
       ],
       "total": 50
     }
     ```

2. **Récupérer une commande par ID**
   - **Route:** `GET /commandes/{id}`
   - **Description:** Récupère les détails d'une commande à partir de son ID.
   - **Réponse:**
     ```json
     {
       "id": 1,
       "client_id": 1,
       "produits": [
         {
           "produit_id": 101,
           "quantité": 2
         }
       ],
       "total": 50
     }
     ```

3. **Mettre à jour une commande**
   - **Route:** `PUT /commandes/{id}`
   - **Description:** Met à jour une commande existante.
   - **Corps de la requête:**
     ```json
     {
       "client_id": 1,
       "produits": [
         {
           "produit_id": 101,
           "quantité": 3
         }
       ]
     }
     ```
   - **Réponse:**
     ```json
     {
       "id": 1,
       "client_id": 1,
       "produits": [
         {
           "produit_id": 101,
           "quantité": 3
         }
       ],
       "total": 75
     }
     ```

4. **Supprimer une commande**
   - **Route:** `DELETE /commandes/{id}`
   - **Description:** Supprime une commande existante par son ID.
   - **Réponse:**
     ```json
     {
       "message": "Commande supprimée avec succès"
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
         "id": 1,
         "nom": "Jean Dupont",
         "email": "jean.dupont@example.com"
       },
       {
         "id": 2,
         "nom": "Marie Curie",
         "email": "marie.curie@example.com"
       }
     ]
     ```

2. **Créer un client**
   - **Route:** `POST /clients/`
   - **Description:** Crée un nouveau client.
   - **Corps de la requête:**
     ```json
     {
       "nom": "Jean Dupont",
       "email": "jean.dupont@example.com"
     }
     ```
   - **Réponse:**
     ```json
     {
       "id": 1,
       "nom": "Jean Dupont",
       "email": "jean.dupont@example.com"
     }
     ```

3. **Mettre à jour un client**
   - **Route:** `PUT /clients/{id}`
   - **Description:** Met à jour les informations d'un client existant.
   - **Corps de la requête:**
     ```json
     {
       "nom": "Jean Dupont",
       "email": "jean.dupont@newdomain.com"
     }
     ```
   - **Réponse:**
     ```json
     {
       "id": 1,
       "nom": "Jean Dupont",
       "email": "jean.dupont@newdomain.com"
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
    __tablename__ = "programmefidelite"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    points = Column(Float, default=0.0)
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