import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import pyttsx3
from multiprocessing import Process
from time import sleep
import random
import sys



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
        engine.setProperty('voice', voices[1].id)

        # Sets speed percent
        # Can be more than 100
        engine.setProperty('rate', 120)

        # Set volume 0-1
        engine.setProperty('volume', 0.9)
        engine.say(str(i))
        engine.runAndWait()
        engine.stop()
        i = i + 1

    print(choix_utilisateur)
    Process(target=loop_c).start()


def loop_b():
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
        "Please show your hand and choose ciseau, papier or feuille. Vous avez 5 secondes pour faire votre choix")

    # run and wait method, it processes the voice commands
    engine.runAndWait()
    engine.stop()

    while True:

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


def loop_c():
    global choix_utilisateur
    global win
    global lose
    global nul
    global partie

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

    engine.say("Vous avez choisis" + str(choix_utilisateur))

    choix_ordinateur = ["pierre", "feuille", "ciseaux"]
    choix_ordinateur2 = random.choice(choix_ordinateur)

    if choix_utilisateur == "feuille" and choix_ordinateur2 == "pierre":
        print("feuille vs pierre")
        engine.say("You win")
        win = +1
    elif choix_utilisateur == "ciseaux" and choix_ordinateur2 == "feuille":
        print("ciseaux vs feuille")
        engine.say("You win")
        win = +1
    elif choix_utilisateur == "pierre" and choix_ordinateur2 == "ciseaux":
        print("pierre vs ciseaux")
        engine.say("You win")
        win = +1


    elif choix_utilisateur == "feuille" and choix_ordinateur2 == "ciseaux":
        print("pierre vs feuille")
        engine.say("You lose")
        lose = +1
    elif choix_utilisateur == "ciseaux" and choix_ordinateur2 == "pierre":
        print("feuille vs ciseaux")
        engine.say("You lose")
        lose = +1
    elif choix_utilisateur == "feuille" and choix_ordinateur2 == "ciseaux":
        print("ciseaux vs pierre")
        engine.say("You lose")
        lose = +1
    else:
        print(str(choix_utilisateur) + " vs " + str(choix_ordinateur2))
        engine.say("Nul")
        nul = +1

    partie = +1

    # run and wait method, it processes the voice commands
    engine.runAndWait()
    engine.stop()

    print(str(nom_utilisateur))
    print("nombre de parties:" + str(partie))
    print("nombre de win:" + str(win))
    print("nombre de lose:" + str(lose))
    print("nombre de nul:" + str(nul))

    continuer = str(input("Voulez-vous continuer à jouer? oui/non"))

    if continuer == "oui":
        Process(target=loop_a).start()
    else:
        sys.exit()


if __name__ == '__main__':
    nom_utilisateur = input("Entrer votre nom:")
    win = 0
    lose = 0
    nul = 0
    partie = 0

    loop_a = Process(target=loop_a)
    loop_b = Process(target=loop_b)
    loop_a.start()
    loop_b.start()
