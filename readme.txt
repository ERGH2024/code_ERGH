# Projet de gestion officinal - Version enrichie

## Structure du projet
Ce projet est un logiciel de gestion officinal développé en FastAPI avec PostgreSQL pour la gestion des données. Il inclut des fonctionnalités comme la gestion des patients, médicaments, ordonnances, facturations, stocks, utilisateurs, et journal des activités.

### Technologies utilisées :
- **Backend** : FastAPI
- **Base de données** : PostgreSQL
- **ORM** : SQLAlchemy
- **Gestion des utilisateurs et des sessions**
- **CRUD complet** sur les entités principales du projet

### Décisions clés du projet
1. **Base de données** :
    - Nous avons décidé d'utiliser PostgreSQL pour sa robustesse et sa capacité à gérer de grandes bases de données.
    - Les tables principales incluent : Patient, Mutuelle, PatientMutuelle, TVA_Marges, Medicament, Ordonnance, Facturation, Stock, Utilisateur, JournalActivites, SessionsUtilisateur.
    - Chaque table est bien liée via des clés étrangères, par exemple : `PatientMutuelle` lie les patients avec leurs mutuelles.

2. **Logique métier** :
    - Nous avons choisi d'intégrer POSOS pour gérer l'interaction médicamenteuse. Cependant, nous prévoyons de créer une solution propre à long terme pour remplacer cette dépendance.
    - Les ordonnances sont suivies par des statuts et des validations automatiques pour gérer des cas spécifiques comme les délivrances de longue durée (ex : 6 mois de traitement à facturer en deux fois).

3. **Sécurité et gestion des permissions** :
    - Nous avons mis en place plusieurs rôles utilisateurs (Pharmacien titulaire, adjoint, préparateur, étudiant) et chaque rôle aura des permissions spécifiques dans le logiciel.
    - La gestion des sessions utilisateurs et un journal d'activités permettent de suivre précisément les actions faites dans le logiciel.

4. **Automatisation prévue** :
    - Automatisation des tâches répétitives pour réduire le temps d'utilisation du logiciel (ex : scannage des ordonnances, gestion du stock après délivrance de médicaments).
    - Génération de rapports automatiques à la fin de chaque journée sur l'état des stocks et les recommandations de réapprovisionnement.

5. **Gestion des erreurs et support** :
    - Mise en place d'une solution de secours pour garantir que la pharmacie ne soit jamais bloquée en cas de problème avec le logiciel. Un support sera disponible 24/7.

## Ce qui reste à faire
- **Automatisation complète** des processus (ordonnances, facturations, stock).
- **Amélioration de la sécurité** avec des systèmes d'authentification plus robustes et une gestion des sessions utilisateur plus fine.
- **Déploiement** du logiciel sur une infrastructure cloud (AWS, DigitalOcean) pour une utilisation multi-pharmacies.
- **Tests unitaires** pour valider toutes les fonctionnalités CRUD et éviter les bugs futurs.

## Historique des décisions importantes
- Nous avons remplacé `nom_scientifique` par `DCI` dans la table médicament pour coller à la norme.
- Ajout de la `TVA` pour chaque médicament pour calculer les prix de vente.
- Gestion des ordonnances longues via un système de statut pour mettre des facturations "en attente".
- Plusieurs discussions ont été menées sur l'optimisation des performances pour gérer une base de données massive.

## Commandes principales :
- Lancer le projet FastAPI : `uvicorn app.main:app --reload`
- Se connecter à la base de données PostgreSQL : `psql -U gad -d bdd_gestion_officinal`

## Collaboration via Git :
- Utilisation de branches dédiées pour chaque fonctionnalité (ex : `feature/ordonnances`, `feature/stock`).
- Création de Pull Requests pour révision avant fusion dans la branche principale (`master` ou `main`).
