TaskFlow API
Une API de gestion de tâches construite avec FastAPI, faite dans le cadre de mon apprentissage du développement backend en Python.
Le but du projet, c'est simple : pouvoir créer des projets, y ajouter des tâches, gérer des utilisateurs, et sécuriser tout ça avec de l'authentification. Rien de révolutionnaire, mais c'est un bon terrain d'entraînement pour comprendre comment une vraie API REST est structurée.
Pourquoi ce projet
J'apprends Python et je voulais sortir des tutoriels classiques pour construire quelque chose qui ressemble à ce qu'on trouve en entreprise : une architecture propre, séparée en modules, avec des tests et une vraie base de données. TaskFlow API est le résultat de ça.
Ce que ça fait
Créer, modifier, lister et supprimer des tâches
Organiser les tâches par projets
Gestion des utilisateurs avec authentification
Documentation interactive générée automatiquement (Swagger)
Base de données persistante en SQLite
Stack technique
Python 3.13
FastAPI — le framework web
SQLAlchemy — pour parler à la base de données
SQLite — base de données locale, simple pour un projet de cette taille
Pydantic — validation des données
Uvicorn — serveur ASGI
Pytest — pour les tests
Structure du projet
taskflow-api/
├── app/
│   ├── main.py           # point d'entrée de l'application
│   ├── database.py        # connexion et config de la base de données
│   ├── models.py           # modèles SQLAlchemy
│   ├── schemas.py          # schémas Pydantic (validation)
│   ├── auth.py              # authentification
│   └── routers/
│       ├── tasks.py         # endpoints liés aux tâches
│       ├── projects.py      # endpoints liés aux projets
│       └── users.py         # endpoints liés aux utilisateurs
├── tests/
│   └── test_tasks.py
├── requirements.txt
└── taskflow.db
Installation
Clone le repo, puis installe les dépendances dans un environnement virtuel :
bash
git clone https://github.com/CodeBertrand/taskflow-api.git
cd taskflow-api
python3 -m venv venv
source venv/bin/activate      # sur Windows : venv\Scripts\activate
pip install -r requirements.txt
Lancer le projet
Important : la commande se lance depuis la racine du projet (taskflow-api), pas depuis le dossier app.
bash
python3 -m uvicorn app.main:app --reload
Le serveur démarre sur http://127.0.0.1:8000.
Documentation de l'API
Une fois le serveur lancé, la doc interactive est disponible ici :
Swagger UI : http://127.0.0.1:8000/docs
ReDoc : http://127.0.0.1:8000/redoc
Tu peux tester tous les endpoints directement depuis le navigateur, pas besoin de Postman.
Tests
bash
pytest
Ce que j'ai appris en faisant ce projet
Comment structurer une API en modules plutôt que de tout mettre dans un seul fichier
La différence entre les modèles SQLAlchemy et les schémas Pydantic, et pourquoi on sépare les deux
Comment fonctionne l'authentification dans une API REST
L'importance de tester son code, même sur un petit projet
Que le dossier depuis lequel on lance une commande, ça compte (véridique, j'ai perdu du temps là-dessus)
Pistes d'amélioration
