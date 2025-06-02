# UBeer

## Jused Adinsi et MArtin Khyari B3 C2

## url de la prod : https://ubeer-seven.vercel.app/

### Description

UBeer est une application web permettant de consulter, commander et gérer des bières artisanales ainsi que leurs brasseries. Elle est composée d'un frontend en React, d’un backend en Flask (Python), d'une base de données MySQL et d’un système de cache Redis. Le tout est déployé sur Vercel et Clever Cloud.

## Fonctionnalités principales

### Pour les utilisateurs
- Visualisation d’une liste de bières avec leurs détails
- Ajout de bières au panier
- Accès à une liste de brasseries
- Carte interactive affichant les brasseries via Leaflet.js

### Pour les administrateurs
- Connexion sécurisée via OAuth 2.0
- Ajout, modification et suppression de bières
- Ajout, modification et suppression de brasseries

### Performance
- Mise en cache des données avec Redis
- Invalidation automatique du cache après modification des données

## Stack technique

| Composant     | Technologie               |
|---------------|---------------------------|
| Frontend      | React.js (Vite)           |
| Backend       | Flask (Python)            |
| Authentification | OAuth 2.0              |
| Base de données | MySQL (Clever Cloud)    |
| Cache         | Redis (Materia KV)        |
| Carte         | Leaflet.js                |
| Hébergement   | Vercel (frontend + backend) |

## Structure du projet

ubeer/
├── frontend/ # Application React
├── backend/ # Application Flask
│ ├── models.py # Modèles SQLAlchemy
│ ├── routes.py # API REST
│ ├── redis_client.py # Connexion Redis
│ └── ...
├── .env # Fichier d’environnement
└── README.md



## Démarrage local

### Prérequis
- Python 3.10+
- Node.js
- Accès à une base MySQL
- Accès à un serveur Redis

### Installation

#### Backend
cd backend
pip install -r requirements.txt

#### Frontend
cd frontend
npm install


### Variables d’environnement (backend)
Créer un fichier .env dans le dossier backend avec le contenu suivant :
     REACT_APP_API_URL=


### Cache Redis
Le backend utilise Redis pour mettre en cache les réponses des routes /api/brasseries et /api/beers.

#### Test manuel
Appeler /api/brasseries une première fois : données issues de la base de données

Appeler une seconde fois : données issues de Redis

Ajouter ou modifier une brasserie : le cache est automatiquement invalidé

Réappeler /api/brasseries : données issues de la base, et nouveau cache généré

#### Carte interactive
La page "Carte" utilise Leaflet.js pour afficher dynamiquement les brasseries sur une carte. Chaque brasserie dispose d’une latitude et d’une longitude stockées dans la base de données.

#### Authentification administrateur
Authentification OAuth 2.0 (ex : Google, GitHub)

Accès restreint à certaines fonctionnalités via session ou jeton

Seuls les administrateurs peuvent gérer les bières et brasseries

#### Déploiement
Vercel
Service	URL (exemple)
Frontend	https://ubeer-frontend.vercel.app
Backend	https://ubeer-backend.vercel.app

Clever Cloud
Service	Usage
Redis KV	Mise en cache
MySQL	Base de données principale

#### Roadmap
Intégration du paiement (Stripe ou autre)

Ajout d’un moteur de recherche de bières

Gestion des rôles administrateurs

Téléversement d’images pour les produits

Pour le frontend voici la liste des installations requise : 
npm install @mui/material @emotion/react @emotion/styled
npm install @mui/material @mui/styled-engine-sc styled-components
npm install react-router-dom
