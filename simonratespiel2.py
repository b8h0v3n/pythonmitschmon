from random import shuffle
lower = 0
upper = 0
answer = 0


def istZahl(x):
    try:
        int(x)
    except ValueError:
        return False


def randomNumber(lower, upper):
    list = [lower]
    while list[-1] != upper:
        list.append(list[-1] + 1)
    shuffle(list)
    gesucht = int(list[-1])
    return gesucht


def answerdef(lower, upper):
    answer = input(f"Errate die Zahl zwischen {lower} und {upper}: ")
    while istZahl(answer) == False:
        print("Das ist keine Zahl !")
        answer = input(f"Errate die Zahl zwischen {lower} und {upper}: ")
    return int(answer)


def hint(answer, gesucht, lower, upper):
    while answer != gesucht:
        if answer < gesucht:
            print(f"die gesuchte Zahl! ist größer {answer}\n")
            answer = answerdef(lower, upper)
        elif answer > gesucht:
            print(f"Die gesuchte Zahl ist kleiner als {answer}\n")
            answer = answerdef(lower, upper)

    if answer == gesucht:
        print(
            f"Herzlichen glückwunsch du hast die gesuchte Zahl {gesucht} gefunden!")


def unten():
    lower = input("Bitte eine untere Grenze festlegen: ")
    while istZahl(lower) == False:
        print("Das ist keine Zahl !")
        lower = input("Bitte eine untere Grenze festlegen: ")
    print(lower)
    return lower


def oben():
    upper = input("Bitte eine obere Grenze festlegen: ")
    while istZahl(upper) == False:
        print("Das ist keine Zahl !")
        upper = input("Bitte eine obere Grenze festlegen: ")
    print(upper)
    return upper


def main(lower, upper, answer):
    lower = int(unten())
    # wenn man das int(x) entfernt funktioniert das programm nicht
    upper = int(oben())
    gesucht = int(randomNumber(lower, upper))
    answer = int(answerdef(lower, upper))
    hint(answer, gesucht, lower, upper)


main(lower, upper, answer)


# replay option
# fix wenn != int eingegeben werden
