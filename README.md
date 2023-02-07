# Git de l'examen de l'API Banque Python conteneurisée pour la 5e année d'études au sein de l'école Sup de Vinci

## Intro
Le but de ce mini-projet est d'implémenter une API en python permettant la gestion des clients d'une banque fictive.

Un client est représenté par son nom, prénom, email, id.

Les opérations que l'API doit pouvoir réaliser :
- ajouter un client
- voir tous les clients
- voir un client en particulier

Il nous est demandé de rendre ce projet avec deux conteneurs docker :
 - Un conteneur avec la base de données, non accessible depuis l'extérieur
 - Un conteneur avec l'API, accessible depuis l'extérieur et communiquant avec la base de données en local
Tout doit être fonctionnel avec un docker-compose up.

Nous avons un peu moins de 6h pour réaliser ce projet.

La notation est partagée entre la réussite de la conteneurisation, la propreté du code produit et ce readme.

## Pré-requis :
1. Installer docker-compose
2. Avoir 2Go de disponible pour les images qui seront téléchargées (python/debian, postgres/alpine)

## Instructions
1. docker-compose up
2. Envoyer les requêtes GET/POST via wget/curl/postman pour interagir avec l'API

## Requêtes GET/POST pour communiquer avec l'API
L'API renvoie les résultats sous format JSON.
Si la requête s'est bien passée, le code retour 200 est envoyé, sinon 400/404/500

Deux requêtes GET différentes peuvent être réalisées :
 1. 127.0.0.1:80/api/v1/clients -> renvoie tous les clients
 2. 127.0.0.1:80/api/v1/clients/1 -> renvoie le client ayant l'id 1

Une requête POST peut être réalisée :
 1. 127.0.0.1:80/api/v1/clients -> permet d'ajouter des clients
avec comme body de la requête :
{
    "firstName": "FirstName",
    "lastame": "LastName",
    "emailId": "testemail@test.fr"
}


## Explication des différents dossiers/fichiers :
- api.py : le script principal permettant de lancer l'API, fait le lien entre les points d'arrivées de l'API et les fonctions à exécuter. Renvoie le résultat demandé si ok avec le code 200, sinon un message d'erreur avec le code approprié (400, 404)
- init.sql : le script permettant d'intialiser la base de données une fois le conteneur démarré
- Dockerfile : permet de créer l'image docker qui contiendra l'API
- docker-compose.yml : crée un conteneur pour la base de données, un autre pour l'API, en vérifiant la sanité de la base de données avant de démarrer l'API
- metier : dossier contenant les sources de l'API
- metier/client.py : la classe représentant le client, avec tous les tests vérifiant si le nom prénom et email sont OK avant de le créer.
- metier/databaseFactory : contient les foncitons de base pour communiquer avec une base de données en facilitant l'ajout de nouvelles base de données dans le futur.


si besoin de me contacter :
tel : 06 01 43 55 31
mail : marticmarkos86@gmail
