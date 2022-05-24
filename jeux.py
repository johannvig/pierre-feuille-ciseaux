import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import pyttsx3
from multiprocessing import Process
from time import sleep
import random
import time
import json




win, partie, lose, nul = 0, 0, 0, 0


def loop_a():
    sleep(15)
    i = 0
    while i < 6:
        # Initialize the engine
        engine = pyttsx3.init()

        # Set properties before adding
        # Things to say

        # Use female voice
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)

        # Sets speed percent
        # Can be more than 100
        engine.setProperty('rate', 120)

        # Set volume 0-1
        engine.setProperty('volume', 0.9)
        engine.say(str(i))
        engine.runAndWait()
        engine.stop()
        i = i + 1




def loop_b():

    global win
    global lose
    global nul
    global partie

    cap = cv.VideoCapture(0)

    detector = HandDetector(detectionCon=0.8, maxHands=2)

    # Initialize the engine
    engine = pyttsx3.init()

    # Set properties before adding
    # Things to say

    # Use female voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    # Sets speed percent
    # Can be more than 100
    engine.setProperty('rate', 120)

    # Set volume 0-1
    engine.setProperty('volume', 0.9)

    # say method on the engine that passing input text to be spoken
    engine.say(
        "Montrer votre main et choississez entre ciseaux, papier et feuille. Vous avez 5 secondes pour faire votre choix")

    # run and wait method, it processes the voice commands
    engine.runAndWait()
    engine.stop()

    fin=time.time() + 17

    while time.time()<fin:

        ret, img = cap.read()
        hands, img = detector.findHands(img)

        if len(hands) == 1:

            if detector.fingersUp(hands[0]) == [0, 1, 1, 0, 0] or detector.fingersUp(hands[0]) == [0, 0, 0, 0,
                                                                                                   1] or detector.fingersUp(
                    hands[0]) == [0, 0, 1, 1, 0] or detector.fingersUp(hands[0]) == [1, 1, 1, 0, 0]:
                cv.putText(img, "ciseaux", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 211), 12)
                choix_utilisateur = "ciseaux"


            elif detector.fingersUp(hands[0]) == [0, 0, 0, 0, 0] or detector.fingersUp(hands[0]) == [1, 0, 0, 0, 0]:
                cv.putText(img, "pierre", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 211), 12)
                choix_utilisateur = "pierre"

            elif detector.fingersUp(hands[0]) == [1, 1, 1, 1, 1] or detector.fingersUp(hands[0]) == [0, 1, 1, 1, 1]:
                cv.putText(img, "feuille", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 211), 12)
                choix_utilisateur = "feuille"

            else:
                cv.putText(img, "nothing", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 211), 12)
                choix_utilisateur = "nothing"

        cv.imshow("Hand detector", img)

        if cv.waitKey(1) and 0xFF == ord('c'):
            break


    cap.release()
    cv.destroyAllWindows()

    engine = pyttsx3.init()

    # Set properties before adding
    # Things to say

    # Use female voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    # Sets speed percent
    # Can be more than 100
    engine.setProperty('rate', 120)

    # Set volume 0-1
    engine.setProperty('volume', 0.9)

    engine.say("Vous avez choisis" + str(choix_utilisateur))

    choix_ordinateur = ["pierre", "feuille", "ciseaux"]
    choix_ordinateur2 = random.choice(choix_ordinateur)

    engine.say("L'ordinateur a choisis" + str(choix_ordinateur2))

    if choix_utilisateur == "feuille" and choix_ordinateur2 == "pierre":
        print("utilisateur:feuille vs ordinateur: pierre")
        engine.say("Tu as gagné")
        win = +1
    elif choix_utilisateur == "ciseaux" and choix_ordinateur2 == "feuille":
        print("utilisateur:ciseaux vs ordinateur: feuille")
        engine.say("Tu as gagné")
        win = +1
    elif choix_utilisateur == "pierre" and choix_ordinateur2 == "ciseaux":
        print("utilisateur:pierre vs ordinateur: ciseaux")
        engine.say("Tu as gagné")
        win = +1


    elif choix_utilisateur == "feuille" and choix_ordinateur2 == "ciseaux":
        print("utilisateur: feuille vs ordinateur: ciseaux")
        engine.say("Tu as perdu")
        lose = +1
    elif choix_utilisateur == "ciseaux" and choix_ordinateur2 == "pierre":
        print("utilisateur: feuille vs ordinateur: ciseaux")
        engine.say("Tu as perdu")
        lose = +1
    elif choix_utilisateur == "pierre" and choix_ordinateur2 == "feuille":
        print("utilisateur: pierre vs ordinateur: feuille")
        engine.say("Tu as perdu")
        lose = +1
    else:
        print(str(choix_utilisateur) + " vs " + str(choix_ordinateur2))
        engine.say("Partie nulle")
        nul = +1

    partie = +1

    # run and wait method, it processes the voice commands
    engine.runAndWait()
    engine.stop()

    fileObject = open("pierre-feuille-ciseaux.json", "r")
    jsonContent = fileObject.read()
    List = json.loads(jsonContent)

    partie2,win2,lose2,nul2= List['partie'],List['win'],List['lose'],List['nul']

    total_partie=partie+int(partie2)
    total_win = win+int(win2)
    total_lose = lose+int(lose2)
    total_nul = nul+int(nul2)


    print(f"nombre de partie:{total_partie}")
    print(f"nombre de win:{total_win}")
    print(f"nombre de lose:{total_lose}")
    print(f"nombre de nul:{total_nul}")

    score_actualiser = {
        "partie": int(total_partie),
        "win": int(total_win),
        "lose": int(total_lose),
        "nul": int(total_nul)
    }

    with open('pierre-feuille-ciseaux.json', 'w') as mon_fichier:
        json.dump(score_actualiser, mon_fichier)





if __name__ == '__main__':



    initialisation = {
        "partie": 0,
        "win": 0,
        "lose": 0,
        "nul": 0
    }

    with open('pierre-feuille-ciseaux.json', 'w') as mon_fichier:
        json.dump(initialisation, mon_fichier)


    continuer=int(input("Combien de parties voulez-vous faire?"))
    i=0
    while int(i)<int(continuer):
        loop1 = Process(target=loop_a)
        loop2 = Process(target=loop_b)
        loop1.start()
        loop2.start()
        loop1.join()
        loop2.join()

        i=i+1



    fileObject = open("pierre-feuille-ciseaux.json", "r")
    jsonContent = fileObject.read()
    List = json.loads(jsonContent)

    print("score total")
    print(f"nombre de partie:{List['partie']}")
    print(f"nombre de win:{List['win']}")
    print(f"nombre de lose:{List['lose']}")
    print(f"nombre de nul:{List['nul']}")

