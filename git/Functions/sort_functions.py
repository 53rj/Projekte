import random
from datetime import datetime


def laufzeit(funktion):
    vor = datetime.now()
    funktion(list)
    nach = datetime.now()

    print(f"Die Sortierung hat {nach - vor} gedauert.")


def bubble(list):
    tausch = True
    while tausch:
        tausch = False
        i = 0
        while i < len(list) - 1:
            if list[i] > list[i+1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                tausch = True
            i += 1


def insertion(list):
    i = 1
    while i < len(list):
        stelle = i-1
        hilf = list[i]
        while stelle >= 0 and list[stelle] > hilf:
            list[stelle + 1] = list[stelle]
            stelle -= 1
        list[stelle+1] = hilf
        i += 1


def selection(list):
    i = 0
    while i <= len(list) - 2:
        minindex = i
        j = i + 1
        while j <= len(list) - 1:
            if list[j] < list[minindex]:
                minindex = j
            j += 1
        hilf = list[i]
        list[i] = list[minindex]
        list[minindex] = hilf
        i += 1


def shell(list):
    h = 1
    while h < len(list) / 2:
        h = 2 * h + 1
    while h >= 1:
        i = h
        while i <= len(list) - 1:
            stelle = i - h
            hilf = list[i]
            while stelle >= 0 and list[stelle] > hilf:
                list[stelle + h] = list[stelle]
                stelle = stelle - h
            list[stelle + h] = hilf
            i += 1
        h = h // 2


def quicksort(feld, links, rechts):
    i = links
    j = rechts
    trenner = feld[(links + rechts)//2]
    while i <= j:
        while feld[i] < trenner:
            i += 1
        while feld[j] > trenner:
            j -= 1
        if i <= j:
            hilf = feld[i]
            feld[i] = feld[j]
            feld[j] = hilf
            i += 1
            j -= 1
    if links < j:
        quicksort(feld,links, j)
    if rechts > i:
        quicksort(feld, i, rechts)


def random_inlist(laenge, spanne=1000000):
    list = []
    random.seed(1337)
    for i in range(laenge):
        list.append(random.randint(1, spanne))
    return list


def namesort(liste):
    for a in range(len(liste)):
        for b in range(len(liste)-1):
            if len(liste[b]) > len(liste[b+1]):
                liste[b], liste[b+1] = liste[b+1], liste[b]

    for c in range(len(liste)):
        for d in range(len(liste)-1):
            if len(liste[d]) == len(liste[d+1]):
                if liste[d] > liste[d+1]:
                    liste[d], liste[d+1] = liste[d+1], liste[d]



liste = ["Meier", "Lindner", "Jensen", "Kohl", "Marz", "Hansen", "Lass"]
namesort(liste)
print(liste)
