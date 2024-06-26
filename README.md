# app-django-multilang

# Site Multilingue avec Chatbot 

Ce projet est une application web multilingue en Python avec Django intégrant un chatbot GPT Assistant et une alternantive Tidio afin de discuter de toute l'actualité concernant l'Euro 2024.

## Prérequis

Assurez-vous d'avoir les éléments suivants installés sur votre machine :

- Python 3.8 ou supérieur
- Git

## Installation

1. **Clonez le dépôt GitHub**

   ```sh
   git clone https://github.com/JonathanMbaya/app-django-multilang.git

   ```

2. **Créez et activez un environnement virtuel**

   - Sur macOS et Linux :

     ```sh
     python3 -m venv venv
     source venv/bin/activate
     ```

   - Sur Windows :

     ```sh
     python -m venv venv
     .\venv\Scripts\activate
     ```

3. **Installez les dépendances**

   ```sh
   pip install -r requirements.txt
   ```

5. **Appliquez les migrations de la base de données**

   ```sh
   python manage.py migrate
   ```

6. **Collectez les fichiers statiques**

   ```sh
   python manage.py collectstatic --noinput
   ```

7. **Créez un superutilisateur pour accéder à l'admin Django**

   ```sh
   python manage.py createsuperuser
   ```

## Utilisation

1. **Lancez le serveur de développement**

   ```sh
   python manage.py runserver
   ```

2. Ouvrez votre navigateur et accédez à `http://127.0.0.1:8000` pour voir l'application en action.

3. Accédez à l'interface d'administration à `http://127.0.0.1:8000/admin` pour gérer les articles et les configurations du chatbot.

## Déploiement

Pour déployer ce projet sur Render, suivez ces étapes :

`https://site-multilang.onrender.com/`

Render détectera automatiquement le projet Django et appliquera les configurations nécessaires pour le déploiement.

## Fonctionnalités

- Chatbot Tidio
- Interface d'administration pour gérer les articles
- Design responsive pour une utilisation sur mobile et tablette

## License

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

MIT License

Copyright (c) [2024] [JonathanMbaya]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
