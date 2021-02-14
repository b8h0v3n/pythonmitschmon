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
    try:
        answer = int(
            input(f"errate die Zahl in der Grenze {lower} und {upper}:\n"))
    except ValueError:
        answer = int(
            input(f"errate die Zahl! in der Grenze {lower} und {upper}:\n"))
    return answer


def hint(answer, gesucht):
    while answer != gesucht:
        if answer < gesucht:
            try:
                answer = int(input(f"die gesuchte Zahl ist größer {answer}\n"))
            except ValueError:
                answer = int(
                    input(f"die gesuchte Zahl! ist größer {answer}\n"))
        elif answer > gesucht:
            try:
                answer = int(
                    input(f"die gesuchte Zahl ist kleiner {answer}\n"))
            except ValueError:
                answer = int(
                    input(f"die gesuchte Zahl! ist kleiner {answer}\n"))
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
    upper = input("Bitte eine untere Grenze festlegen: ")
    while istZahl(upper) == False:
        print("Das ist keine Zahl !")
        upper = input("Bitte eine untere Grenze festlegen: ")
    print(upper)
    return upper


def main(lower, upper, answer):
    lower = int(unten())
    upper = int(oben())     #wenn man das int(x) entfernt funktioniert das programm nicht
    gesucht = int(randomNumber(lower, upper))
    answer = int(answerdef(lower, upper))
    hint(answer, gesucht)


main(lower, upper, answer)


# replay option
# fix wenn != int eingegeben werden
