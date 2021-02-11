from random import shuffle

#fragt nach einer zahl zw. min und max und gibt die Antwort des benutzers zurück
def userInput(min, max):
    min = min
    max = max
    uInput = input(f"Bitte geben sie eine Zahl, zwischen {min} und {max} ein:\n\n")
    try:
        int(uInput)
    except ValueError:
        try:
            float(uInput)
        except ValueError:
            print("Dies ist keine Zahl!")
            uInput = input(f"Bitte geben sie eine Zahl, zwischen {min} und {max} ein:\n\n")
            pass
    return int(uInput)






#vergleicht die zahl des nutzers mit der generierten und gibt tipps
def compare(rdmNumber, input):
    if rdmNumber > input :
        print(f"Die gesuchte Zahl ist größer, als die {input}.")
    if rdmNumber < input:
        print(f"Die gesuchte Zahl ist kleiner, als die {input}.")

#prüft, ob die zahl erraten wurde, gibt true oder false zurück
def istRichtig(rdmNumber, input):
    if input == rdmNumber:
        print(f"Du hast die Zahl erraten, es war eine {rdmNumber}")
        return True
    else:
        return False

#generiert und gibt eine zufällige Zahl zurück, die mithilfe einer liste generiert wird
def randomNumber(min, max):
    min = int(min)
    max = int(max)
    numbers = []
    #liste innerhalb der grenzen wir generiert
    for number in range(min, max+1):
        numbers.append(number)
    #liste wird durchgemischt
    shuffle(numbers)
    #die erste Zahl in der Liste wird als rdmNumber zurückgegeben
    rdmNumber = numbers[-1]
    return rdmNumber

def nochmal():
    again = input("Nochmal spielen ? (Y/N)")
    if again.lower() == "y":
        ratespiel()
    elif again.lower() == "n":
        print("Spiel beendet")
    else:
        print("Bitte mit 'N' oder 'N'")




#main methode
def main(min, max, uInput, rdmNumber):
    #wiederholt sich so lange, bis die richte zahl geraten wurde
    while istRichtig(rdmNumber, uInput) == False:
        uInput = userInput(min, max) #Es wird nach dem User Input gefragt
        compare(rdmNumber, uInput) #Es wird geprüft, ob die Zahl größer oder kleiner als rdmNumber ist
    nochmal()

def ratespiel():
    print("\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\tRatespiel: Errate die gesuchte Zahl!")
    min = input(f"Bitte legen sie eine Untergrenze fest: ")
    try:
        int(min)
    except ValueError:
        try:
            float(min)
        except ValueError:
            print("Das ist keine Zahl !")
            min = input(f"Bitte legen sie eine Untergrenze fest: ")

    max = input(f"Bitte legen sie eine Obergrenze fest: ")
    try:
        int(max)
    except ValueError:
        try:
            float(max)
        except ValueError:
            print("Das ist keine Zahl !")
            max = input(f"Bitte legen sie eine Obergrenze fest: ")


    #print(min + max)
    rdmNumber = randomNumber(min, max)

    #print(rdmNumber)
    main(min, max, 0, rdmNumber)


ratespiel()




