# Digicheese - API de Gestion de Fidélité

## Vue d’ensemble

**Digicheese** est une API RESTful développée avec **FastAPI**, permettant de gérer des programmes de fidélité, des commandes clients, ainsi que des informations sur les clients. Elle s’intègre avec une base de données **MySQL** via **SQLAlchemy**, offrant des fonctionnalités CRUD complètes pour diverses entités telles que les programmes de fidélité, les bonus, les promotions, les commandes et les clients.

## Fonctionnalités Principales

- **Gestion des Programmes de Fidélité** : Suivi des points de fidélité et des niveaux des clients.
- **Gestion des Commandes** : Création, récupération et gestion des commandes clients.
- **Gestion des Clients** : Ajout, mise à jour et récupération des informations clients.
- **Gestion des Bonus et Promotions** : Attribution de bonus et vérification des promotions.
- **Support CRUD Complet** : Pour toutes les entités principales (clients, commandes, programmes de fidélité).

---

## Prérequis

- **Python** : 3.12+
- **FastAPI** : Dernière version
- **SQLAlchemy** : ORM pour les interactions avec la base de données
- **MySQL** : Système de gestion de base de données
- **Pydantic** : Validation des données

---

## Installation

1. Clonez le dépôt GitHub :  

    ```bash
    git clone https://github.com/GaelBuenoBarthe/DigiCheese.git
    cd digicheese
    ```

2. Créez un fichier `.env` avec les informations de connexion à la base de données :  

    ```env
    DATABASE_URL="mysql://dev:12345@localhost:3306/fromagerie_com"
    ```

3. Installez les dépendances requises :  

    ```bash
    pip install -r requirements.txt
    ```

---
4.Le code est dans la branche Develop

## Création de la Base de Données

### Utilisation du Dump SQL

1. Connectez-vous à MySQL via PowerShell ou votre terminal :

    ```bash
    mysql -u root -p
    ```

2. Créez la base de données et l’utilisateur :

    ```sql
    CREATE DATABASE nom_de_la_base;
    CREATE USER 'dev'@'localhost' IDENTIFIED BY '12345';
    GRANT ALL PRIVILEGES ON nom_de_la_base.* TO 'dev'@'localhost';
    FLUSH PRIVILEGES;
    ```

3. Importez le dump SQL :

    ```bash
    mysql -u dev -p nom_de_la_base < ressource/db_dump.sql
    ```

### Création des Tables via `main.py`

1. Exécutez le script principal pour générer les tables :  

    ```bash
    python main.py
    ```

### Remplissage de la Base de Données

1. Exécutez le script de remplissage de la base :  

    ```bash
    python populate.py
    ```

---

## Lancement du Serveur

1. Démarrez le serveur avec **Uvicorn** :  

    ```bash
    uvicorn app.main:app --reload
    ```

2. L'API sera disponible à l'adresse : [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Routes Disponibles

### Programme de Fidélité

1. **Récupérer le programme de fidélité d’un client**  
   - **Route** : `GET /fidelite/fidelite/{client_id}`  
   - **Exemple de Réponse** :  
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
   - **Route** : `POST /commandes/`  
   - **Exemple de Requête** :  
     ```json
     {
       "datcde": "2024-09-18",
       "codcli": 1,
       "nbcolis": 1,
       "cdeComt": "Exemple commentaire",
       "barchive": 0,
       "bstock": 1
     }
     ```
   - **Exemple de Réponse** :  
     ```json
     {
       "datcde": "2024-09-18",
       "codcli": 1,
       "nbcolis": 1,
       "cdeComt": "Exemple commentaire",
       "codcde": 1
     }
     ```

2. **Récupérer les commandes**  
   - **Route** : `GET /commandes`  
   - **Exemple de Réponse** :  
     ```json
     [
       {
         "datcde": "2024-01-01",
         "codcli": 1,
         "nbcolis": 1,
         "cdeComt": "Commentaire exemple 1",
         "codcde": 1
       },
       {
         "datcde": "2024-01-02",
         "codcli": 2,
         "nbcolis": 2,
         "cdeComt": "Commentaire exemple 2",
         "codcde": 2
       }
     ]
     ```

### Gestion des Clients

1. **Récupérer tous les clients**  
   - **Route** : `GET /clients/`  
   - **Exemple de Réponse** :  
     ```json
     [
       {
         "codcli": 1,
         "genre": "M",
         "nom": "Durand",
         "prenom": "Pierre",
         "telephone": "0102030405",
         "email": "pierre.durand@example.com"
       },
       {
         "codcli": 2,
         "genre": "F",
         "nom": "Dupont",
         "prenom": "Marie",
         "telephone": "0607080910",
         "email": "marie.dupont@example.com"
       }
     ]
     ```

2. **Créer un client**  
   - **Route** : `POST /clients/`  
   - **Exemple de Requête** :  
     ```json
     {
       "genre": "F",
       "nom": "Dupont",
       "prenom": "Marie",
       "adresse1": "Rue de Paris",
       "ville_id": 1,
       "telephone": "0607080910",
       "email": "marie.dupont@example.com",
       "portable": "0612345678",
       "newsletter": true
     }
     ```
   - **Exemple de Réponse** :  
     ```json
     {
       "codcli": 3,
       "genre": "F",
       "nom": "Dupont",
       "prenom": "Marie",
       "email": "marie.dupont@example.com"
     }
     ```

3. **Supprimer un client**  
   - **Route** : `DELETE /clients/{id}`  
   - **Exemple de Réponse** :  
     ```json
     {
       "message": "Client supprimé avec succès"
     }
     ```

---

## Schémas et Modèles

Le projet utilise **SQLAlchemy** pour la gestion des interactions avec la base de données et **Pydantic** pour la validation des données.

### Exemple de Modèle : Programme de Fidélité

```python
class ProgrammeFidelite(Base):
    __tablename__ = "programme_fidelite"

    id = Column(Integer, primary_key=True, index=True)
    points = Column(Numeric(precision=10, scale=2), default=0)
    level = Column(String(50))  # Silver, Gold, etc.

    clients = relationship("Client", secondary=client_programme_fidelite, back_populates="programmes_fidelite")
```

---

## Tests

Pour exécuter les tests unitaires, utilisez **pytest** :

```bash
pytest
```

---

## Contributeurs

- **Bernardo Estacio Abreu**
- **Gaël Bueno-Barthe**
- **Fabrice Bellin**
- **Filip Dabrowski**
- **Marwa Benyahia**

---

## Licence

Ce projet est sous licence [insérer licence].

---

