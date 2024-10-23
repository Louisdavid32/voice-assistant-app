# voice-assistant-app
Voice Assistant App is a Python application that uses tkinter and customtkinter to provide an interactive voice interface. It allows users to control applications, perform web searches, and manage system settings through voice commands. Designed for Linux (Ubuntu), it offers visual feedback and enhanced audio integration.

# Voice Assistant App

Voice Assistant App est une application simple qui utilise la reconnaissance vocale pour permettre aux utilisateurs de contrôler leur système via des commandes vocales. L'application peut ouvrir des applications, effectuer des recherches web, gérer des paramètres système comme le volume, et plus encore. 

## Fonctionnalités

- **Reconnaissance vocale** : L'utilisateur peut émettre des commandes vocales pour interagir avec son ordinateur.
- **Contrôle des applications** : L'assistant peut ouvrir des applications comme le terminal, Spotify, ou VLC.
- **Recherche Web** : L'assistant peut lancer une recherche Google depuis l'interface.
- **Contrôle du système** : Commandes pour gérer le volume, régler une alarme, ou éteindre l'ordinateur.
- **Interface utilisateur** : Une interface graphique interactive avec du feedback visuel.

## Prérequis

Avant d'installer et d'exécuter l'application, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- **Python 3.10 ou supérieur**
- **pip** pour installer les dépendances
- **Modules Python** :
      import tkinter
      import speech_recognition as sr
      import pyttsx3
      import webbrowser
      import os
      import subprocess
      import customtkinter as ctk
      from youtube_search import YoutubeSearc
## Installation

1. Clonez ce dépôt sur votre machine locale :
    ```bash
    git clone https://github.com/Louisdavid32/voice-assistant-app.git
    ```

2. Accédez au dossier du projet :
    ```bash
    cd voice-assistant-app
    ```

3. Installez les dépendances requises :
    ```bash
    pip install -r requirements.txt
    ```

## Utilisation

1. Lancez l'application :
    ```bash
    python3 voice-assistant-app.py
    ```

2. Utilisez la commande vocale pour interagir avec votre système.

3. Quelques exemples de commandes :
    - **"Ouvre le terminal"** : ouvre le terminal sur votre système.
    - **"Joue de la musique"** : ouvre Spotify ou un lecteur de musique.
    - **"Recherche Google pour [terme]"** : lance une recherche sur Google.

## Problèmes fréquents

Si vous rencontrez des erreurs liées à ALSA ou à JACK, cela peut être dû à des problèmes de configuration audio sur votre système Linux. Voici quelques commandes pour résoudre ces problèmes :

- Vérifiez les configurations d'ALSA :
    ```bash
    sudo alsactl init
    ```

- Si le serveur JACK ne démarre pas :
    ```bash
    sudo apt install jackd2
    jackd -d alsa
    ```

## Contribution

Les contributions sont les bienvenues ! Si vous souhaitez améliorer cette application, vous pouvez faire un fork de ce dépôt, créer une nouvelle branche, et soumettre une pull request.

## License

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.


