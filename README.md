# TODO-App-Django


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
- [] Utilisateur
    - [] Sign up
    - [] Connection
    - [] Déconnection
    - [] Récuperation des catégories/taches de l'utilisateur
- [] Taches
    - [] Ajouter une tache à une catégorie
        - [] Impossible si doublon dans la catégorie
    - [] Modifier une tache
    - [] Supprimer une tache
- [] Catégorie
    - [] Ajouter une catégorie
        - [] Impossible si catégorie éxiste déja
    - [] Modifier une catégorie
    - [] Supprimer une catégorie
- [] Affichage
    - [] Afficher la liste des catégories
    - [] Sélectionner une catégorie
        - [] Afficher la liste de taches dans la catégorie 