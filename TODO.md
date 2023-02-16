# TODO-App-Django

# Bug to fix
- [x]  Sign up form
    - [x] Return alert if email not unique
    - [x] Return alert if username not unique
    - [x] return alert if missing infos
    - [x] write in field user entries if error

## Models

- [x] Profil
    - [x] name
    - [x] password
    - [x] email

- [x] Catégories
    - [x] name
    - [x] slug
    - [x] user-fk

- [x] Taches
    - [x] name
    - [x] description
    - [x] collection-fk
    - [x] user-fk

## Fonctionalités
- [x] Utilisateur
    - [x] Sign up
    - [x] Connection
    - [x] Déconnection
    - [x] Récuperation des catégories/taches de l'utilisateur
- [x] Taches
    - [x] Ajouter une tache à une catégorie
    - [x] Supprimer une tache
- [x] Catégorie
    - [x] Ajouter une catégorie
        - [x] Impossible si catégorie éxiste déja
    - [x] Supprimer une catégorie
- [x] Affichage
    - [x] Afficher la liste des catégories
    - [x] Sélectionner une catégorie
        - [x] Afficher la liste de taches dans la catégorie 