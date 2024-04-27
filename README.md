# Pierre-Feuille-Ciseaux avec Détection de la Main

## Description
Ce projet est une implémentation interactive du jeu classique Pierre-Feuille-Ciseaux. Utilisant la détection de la main via la webcam et la bibliothèque OpenCV, les joueurs peuvent jouer contre l'ordinateur en montrant leur choix avec des gestes de la main. Le projet utilise également la synthèse vocale pour améliorer l'interaction en annonçant les choix et les résultats du jeu.

## Fonctionnalités
- **Détection de la main** : Utilise OpenCV et cvzone pour détecter les gestes de la main à partir d'une webcam en temps réel.
- **Synthèse vocale** : Annonce les résultats et les choix des joueurs via pyttsx3.
- **Interaction en temps réel** : Permet aux joueurs de faire leur choix en utilisant des gestes de main.
- **Sauvegarde des résultats** : Les scores sont enregistrés dans un fichier JSON pour garder un historique des parties.

## Technologies utilisées
- Python 3.8 ou supérieur
- OpenCV
- cvzone
- pyttsx3
- Multiprocessing
