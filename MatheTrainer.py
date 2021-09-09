#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from random import shuffle,randint
import time

def Input_Zahl(text):
    while True:
        try:
            Zahl= int(input(text))
            return Zahl
        except ValueError:
            print("Bitte eine Zahl eingeben")

def getSolution(text):
    while True:
        try:
            Zahl= int(input(text).split("=")[-1])
            return Zahl
        except ValueError:
            print("Bitte eine Zahl eingeben")

def geteinmaleins_liste():
    einmaleins_liste = []
    for i in range(0,11):
        for j in range(1,11):
            einmaleins_liste.append((i,j))
    return einmaleins_liste

#Main
print("Welche Rechenart?")
print("1 Plus")
print("2 Minus")
print("3 Einmaleins")
print("4 geteilt")
print("5 Plus und Minus")
print("6 Mal und Geteilt")
print("7 Alle")
print("8 Rechenketten")
print("9 Minus mit Uebertrag")
Aufgabenart = Input_Zahl("Wähle eine Ziffer? ")
GAnzahl = Input_Zahl("Wie viele Aufgaben? ")
Richtige = 0
Falsche = 0
gFehlVersuche = 0
if Aufgabenart in [3,4,6,7,8]:
    einmaleins_liste = []
    while len(einmaleins_liste) < GAnzahl:
        liste = geteinmaleins_liste()
        shuffle(liste)
        einmaleins_liste = einmaleins_liste + liste
    

if Aufgabenart == 5 or Aufgabenart == 6 or Aufgabenart == 7: #zufaellig
    Zufaellig = True
    AufgabenartListe = []
    if Aufgabenart == 5: #Plus und Minus
        for i in range(GAnzahl):
            AufgabenartListe.append(randint(1,2))
    elif Aufgabenart == 6: #Mal und geteilt
        for i in range(GAnzahl):
            AufgabenartListe.append(randint(3,4))
    elif Aufgabenart == 7: #Alle
        for i in range(GAnzahl):
            AufgabenartListe.append(randint(1,5)) # 5 entspricht 9 Minus mit Uebertrag
else:
    Zufaellig = False

Startzeit =time.time() 

for i in range(GAnzahl):
    print("\n\nAufgabe "+ str(Richtige+Falsche+1)+ "\n ")
    if Zufaellig: #Unterschiedliche Aufgabenarten
        Aufgabenart = AufgabenartListe[i]
        if Aufgabenart ==5 : # 5 ersetzen durch 9 für Minus mit Uebertrag
            Aufgabenart=9
    if Aufgabenart ==1 : #plus
        Zahl1 = randint(0,100)
        Zahl2 = randint(0,100-Zahl1)
        Aufgabe = str(Zahl1) + " + " + str(Zahl2) + " = "
        Loesung = Zahl1 + Zahl2
    elif Aufgabenart ==2 : #minus
        Zahl1 = randint(0,100)
        Zahl2 = randint(0,Zahl1)
        Aufgabe = str(Zahl1) + " - " + str(Zahl2) + " = "
        Loesung = Zahl1 - Zahl2
            
    elif Aufgabenart == 3: #mal
        (Faktor1,Faktor2) = einmaleins_liste[i]
        Aufgabe =  str(Faktor1) + " x " + str(Faktor2) + " = "
        Loesung = Faktor1*Faktor2
    elif Aufgabenart == 4: # geteilt
        (Faktor1,Faktor2) = einmaleins_liste[i]
        Aufgabe =  str(Faktor1*Faktor2) + " : " + str(Faktor2) + " = "
        Loesung = Faktor1
    elif Aufgabenart == 8: # Rechenketten
        (Faktor1,Faktor2) = einmaleins_liste[i]
        Zahl2 = randint(0,100-Faktor1*Faktor2)
        Zufallszahl = randint(0,3)
        if Zufallszahl == 0:
            Aufgabe = str(Faktor1) + " x " + str(Faktor2) + " + " + str(Zahl2) + " = "
            Loesung = Faktor1*Faktor2 + Zahl2
        elif Zufallszahl == 1:
            Aufgabe = str(Faktor1*Faktor2) + " : " + str(Faktor2) + " + " + str(Zahl2) + " = "
            Loesung = Faktor1 + Zahl2
        elif Zufallszahl == 2:
            Aufgabe = str(Zahl2) + " + " + str(Faktor1) + " x " + str(Faktor2) + " = "
            Loesung = Zahl2+Faktor1*Faktor2
        elif Zufallszahl == 3:
            Aufgabe = str(Zahl2) + " + " + str(Faktor1*Faktor2) + " : " + str(Faktor2) + " = "
            Loesung = Zahl2+Faktor1
    elif Aufgabenart == 9: # Minus mit Uebertrag
        SubtrahendE = randint(1,9) #Damit es einen Übertrag gibt muss der Einer groesser als 0 sein
        MinuendE = randint(0,SubtrahendE-1) # Einer zum abziehen muss kleiner als der Subtrahend sein fuer einen Uebertrag
        SubtrahendZ = randint(1,8)
        MinuendZ= randint(SubtrahendZ+1,9) # immer 1 groesser damit Uebertrag abziehbar ohne negative Zahlen
        Subtrahend = SubtrahendE + SubtrahendZ*10
        Minuend = MinuendE + MinuendZ*10
        Aufgabe = str(Minuend) + " - " + str(Subtrahend) + " = "
        Loesung = Minuend - Subtrahend
    else:
        Aufgabe = "1+1"
        Loesung = 2       
    try:
        fertig = False # Schleife beim ersten Mal immer durchlaufen
        FehlVersuche = 0 # Anzahl der FehlVersuche
        while not fertig: # solange wiederholen bis Aufgabe abgeschlossen (richtig oder zuviel Fehlversuche)
            Eingabe = getSolution(Aufgabe)
            if Eingabe == Loesung:
                print("\033[42m"+"Richtig!"+"\033[;m")
                Richtige+=1
                fertig = True
            else:
                if FehlVersuche < 2:
                    print("\033[41m"+str(Eingabe) + " ist Falsch! Versuch es nocheinmal!"+"\033[;m")
                    FehlVersuche+=1
                    gFehlVersuche+=1
                else:
                    print("Falsch! Es ist " + str(Loesung))
                    fertig = True
                    Falsche+=1
    except KeyboardInterrupt:
        break        
Endzeit = time.time()
Dauer= (Endzeit-Startzeit)
print("\n" + str(int(Dauer//60)) + " Minuten " + str(int(Dauer%60)) + " Sekunden")
print("\nDu hast " + str(Richtige) + " von " + str(Richtige+Falsche) + " Aufgaben richtig geloest!")
if Falsche == 0:
    if gFehlVersuche == 0:
        print("Du hast Alles Richtig geloest! Super!")
    else:
        print("Super! Du hast zwar " + str(gFehlVersuche) + " Fehler gemacht, konntest dann aber alles richtig lösen!")
