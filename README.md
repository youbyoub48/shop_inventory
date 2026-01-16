# Shop Inventory

Un gestionnaire d'inventaire minimaliste sous Django qui stocke les données dans des fichiers JSON (inventory.json et log.json) au lieu d'une base de données.

🚀 **Démarrage rapide**

*   **Installer :**
    ```bash
    pip install django requests
    ```

*   **Lancer :** Depuis le dossier `src` :
    ```bash
    python manage.py runserver
    ```

    L'API sera active sur `http://127.0.0.1:8000/api/`.

📡 **Liste des commandes API**

Toutes les actions se font via des requêtes POST.

*   `api/register`: Créer un produit.
*   `api/add`: Ajouter du stock (+1).
*   `api/remove`: Retirer du stock (-1).
*   `api/delete`: Supprimer un produit.
*   `api/modify`: Modifier un produit.
*   `api/get`: Voir un produit.
*   `api/list`: Voir tout l'inventaire.

📂 **Fichiers clés**

*   `src/API.py`: Logique de gestion du stock.
*   `req.py`: Script d'exemple pour tester les requêtes.
