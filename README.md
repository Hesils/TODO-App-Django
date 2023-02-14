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
    - [x] Sign up
    - [x] Connection
    - [x] Déconnection
    - [x] Récuperation des catégories/taches de l'utilisateur
- [] Taches
    - [x] Ajouter une tache à une catégorie
    - [] Modifier une tache
    - [] Supprimer une tache
- [] Catégorie
    - [x] Ajouter une catégorie
        - [x] Impossible si catégorie éxiste déja
    - [] Modifier une catégorie
    - [] Supprimer une catégorie
- [] Affichage
    - [x] Afficher la liste des catégories
    - [x] Sélectionner une catégorie
        - [x] Afficher la liste de taches dans la catégorie 