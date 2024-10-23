"""import tkinter
import speech_recognition as sr
import pyttsx3
import webbrowser
import customtkinter as ctk
from youtube_search import YoutubeSearch

# Système vocal
recognizer = sr.Recognizer()
engine = pyttsx3.init()





# Fonction pour parler
def speack(text):
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'fr-fr' in voice.languages:
            engine.setProperty('voice', voice.id)

    # Ajuster la vitesse et le volume si nécessaire
    engine.setProperty('rate', 147)  # Ajuste la vitesse
    engine.setProperty('volume', 1.0)  # Ajuste le volume
    engine.say(text)
    engine.runAndWait()

# Fonction pour écouter la commande
def r_speech():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print('Parlez maintenant!')
        try:
            audio = recognizer.listen(source)
            cmd = recognizer.recognize_google(audio, language='fr-FR')
            print(f"Vous avez dit : {cmd}")
            return cmd.lower()
        except sr.UnknownValueError:
            speack('Je n\'ai rien compris.')
            return ''

        except sr.RequestError:
            speack('Erreur de connexion.')
            return ''

# Exécution de la commande
def exe_cmd():
    cmd = r_speech()

    if 'joue' in cmd or 'musique' in cmd:
        songname = cmd.replace('joue', '').strip()
        speack(f'Recherche de {songname} sur YouTube')
        # Recherche YouTube
        result = YoutubeSearch(songname, max_results=1).to_dict()
        if result:
            videourl = f"https://www.youtube.com/watch?v={result[0]['id']}"
            speack(f"Lecture de {result[0]['title']} en cours.")
            webbrowser.open(videourl)  # Ouvre la vidéo
        else:
            speack("Aucune musique trouvée.")
    elif 'ouvre youtube' in cmd:
        speack('Ouverture de YouTube.')
        webbrowser.open('https://www.youtube.com/')
    elif 'ferme' in cmd:
        speack('Au revoir !')
        app.quit()
    else:
        speack('Je ne reconnais pas cette commande.')

# ------------------ Initialisation de l'application ----------------- #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.title("Mon Assistant Vocal")
app.geometry("500x400")

# Label titre
label = ctk.CTkLabel(app, text="Cliquez sur le bouton bleu pour lancer une commande", font=("Helvetica", 14))
label.pack(pady=30)

# Bouton pour activer la commande vocale
cmdbouton = ctk.CTkButton(app, text='Cliquez-moi', command=exe_cmd, font=("Helvetica", 14), height=50, width=200)
cmdbouton.pack(pady=20)

# Bouton pour quitter l'application
quitterbouton = ctk.CTkButton(app, text='Au revoir !', command=app.quit, font=("Helvetica", 14), height=50, width=200, fg_color='red')
quitterbouton.pack(pady=40)

app.mainloop()"""

import tkinter
import speech_recognition as sr OUAdal__372
import pyttsx3
import webbrowser
import os
import subprocess
import customtkinter as ctk
from youtube_search import YoutubeSearch

# Système vocal
recognizer = sr.Recognizer()
engine = pyttsx3.init()


# Fonction pour parler
def speack(text):
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'fr-fr' in voice.languages:
            engine.setProperty('voice', voice.id)

    # Ajuster la vitesse et le volume si nécessaire
    engine.setProperty('rate', 147)  # Ajuste la vitesse
    engine.setProperty('volume', 1.0)  # Ajuste le volume
    engine.say(text)
    engine.runAndWait()


# Fonction pour écouter la commande
def r_speech():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        update_indicator("listening")  # Change l'indicateur en vert (écoute en cours)
        feedback_label.configure(text="Écoute en cours...")  # Utilise configure() au lieu de config()
        print('Parlez maintenant!')
        try:
            audio = recognizer.listen(source)
            cmd = recognizer.recognize_google(audio, language='fr-FR')
            print(f"Vous avez dit : {cmd}")
            feedback_label.configure(text=f"Vous avez dit : {cmd}")  # Utilise configure() au lieu de config()
            update_indicator("waiting")  # Remet l'indicateur à l'état d'attente (bleu)
            return cmd.lower()
        except sr.UnknownValueError:
            speack('Je n\'ai rien compris.')
            feedback_label.configure(text="Erreur : Je n'ai rien compris.")  # Utilise configure() au lieu de config()
            update_indicator("error")  # Change l'indicateur en rouge (erreur)
            return ''
        except sr.RequestError:
            speack('Erreur de connexion.')
            feedback_label.configure(text="Erreur de connexion.")  # Utilise configure() au lieu de config()
            update_indicator("error")  # Change l'indicateur en rouge (erreur)
            return ''


# Exécution de la commande
def exe_cmd():
    cmd = r_speech()

    if 'joue' in cmd or 'musique' in cmd:
        songname = cmd.replace('joue', '').strip()
        speack(f'Recherche de {songname} sur YouTube')
        feedback_label.configure(text=f"Recherche de {songname} sur YouTube")  # Utilise configure() au lieu de config()
        # Recherche YouTube
        result = YoutubeSearch(songname, max_results=1).to_dict()
        if result:
            videourl = f"https://www.youtube.com/watch?v={result[0]['id']}"
            speack(f"Lecture de {result[0]['title']} en cours.")
            webbrowser.open(videourl)  # Ouvre la vidéo
        else:
            speack("Aucune musique trouvée.")
            feedback_label.configure(text="Aucune musique trouvée.")  # Utilise configure() au lieu de config()

    elif 'ouvre youtube' in cmd:
        speack('Ouverture de YouTube.')
        feedback_label.configure(text="Ouverture de YouTube.")  # Utilise configure() au lieu de config()
        webbrowser.open('https://www.youtube.com/')

    elif 'ouvre vlc' in cmd:
        speack('Ouverture de VLC.')
        feedback_label.configure(text="Ouverture de VLC.")
        subprocess.Popen(['vlc'])  # Ouvre VLC sur Linux

    elif 'ouvre le terminal' in cmd:
        speack('Ouverture du terminal.')
        feedback_label.configure(text="Ouverture du terminal.")
        subprocess.Popen(['gnome-terminal'])  # Ouvre le terminal gnome


    elif 'recherche' in cmd:
        query = cmd.replace('recherche', '').strip()
        speack(f'Recherche de {query} sur Google.')
        feedback_label.configure(text=f'Recherche de {query} sur Google.')
        webbrowser.open(f'https://www.google.com/search?q={query}')  # Recherche Google

    elif 'volume' in cmd:
        if 'augmente' in cmd:
            speack('Augmentation du volume.')
            feedback_label.configure(text="Augmentation du volume.")
            os.system("pactl set-sink-volume @DEFAULT_SINK@ +10%")  # Augmente le volume
        elif 'diminue' in cmd:
            speack('Diminution du volume.')
            feedback_label.configure(text="Diminution du volume.")
            os.system("pactl set-sink-volume @DEFAULT_SINK@ -10%")  # Diminue le volume
        else:
            speack('Commande de volume non reconnue.')
            feedback_label.configure(text="Commande de volume non reconnue.")

    elif 'éteindre' in cmd:
        speack('Extinction de l\'ordinateur dans 5 secondes.')
        feedback_label.configure(text="Extinction de l'ordinateur dans 5 secondes.")
        os.system("shutdown now")  # Éteindre l'ordinateur

    elif 'réveil' in cmd:
        import time
        delay = 5  # Par exemple, 5 secondes pour le réveil
        speack(f'Réveil réglé pour dans {delay} secondes.')
        feedback_label.configure(text=f'Réveil réglé pour dans {delay} secondes.')
        time.sleep(delay)  # Attendre le délai
        speack('Réveil !')  # Annonce du réveil

    elif 'ferme' in cmd:
        speack('Au revoir !')
        app.quit()
    else:
        speack('Je ne reconnais pas cette commande.')
        feedback_label.configure(text="Commande non reconnue.")  # Utilise configure() au lieu de config()


# Fonction pour mettre à jour l'indicateur visuel
def update_indicator(status):
    if status == "waiting":
        canvas.itemconfig(indicator, fill="blue")  # En attente (bleu)
    elif status == "listening":
        canvas.itemconfig(indicator, fill="green")  # Écoute en cours (vert)
    elif status == "error":
        canvas.itemconfig(indicator, fill="red")  # Erreur (rouge)


# ------------------ Initialisation de l'application ----------------- #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.title("Mon Assistant Vocal")
app.geometry("500x400")

# Label titre
label = ctk.CTkLabel(app, text="Cliquez sur le bouton bleu pour lancer une commande", font=("Helvetica", 14))
label.pack(pady=30)

# Indicateur visuel (cercle)
canvas = tkinter.Canvas(app, width=50, height=50, highlightthickness=0)
indicator = canvas.create_oval(10, 10, 40, 40, fill="blue")  # Cercle initial en bleu (attente)
canvas.pack(pady=20)

# Bouton pour activer la commande vocale
cmdbouton = ctk.CTkButton(app, text='Cliquez-moi', command=exe_cmd, font=("Helvetica", 14), height=50, width=200)
cmdbouton.pack(pady=20)

# Label pour le feedback de la commande vocale
feedback_label = ctk.CTkLabel(app, text="En attente de commande...", font=("Helvetica", 12))
feedback_label.pack(pady=10)

# Bouton pour quitter l'application
quitterbouton = ctk.CTkButton(app, text='Au revoir !', command=app.quit, font=("Helvetica", 14), height=50, width=200,
                              fg_color='red')
quitterbouton.pack(pady=20)

app.mainloop()

