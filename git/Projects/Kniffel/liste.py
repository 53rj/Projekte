def count_1s(roll):
    # Hier wird die gesuchte Zahl abgefragt
    zielzahl = 1

    # Überprüfe, ob zielzahl in der Liste vorkommt
    if zielzahl in roll:
        # wird die Summe der Zielzahlen gebildet
        return sum(zahl for zahl in roll if zahl == zielzahl)
    else:
        return 0


def count_2s(roll):
    # Hier wird die gesuchte Zahl abgefragt
    zielzahl = 2

    # Überprüfe, ob zielzahl in der Liste vorkommt
    if zielzahl in roll:
        # wird die Summe der Zielzahlen gebildet
        return sum(zahl for zahl in roll if zahl == zielzahl)
    else:
        return 0


def count_3s(roll):
    # Hier wird die gesuchte Zahl abgefragt
    zielzahl = 3

    # Überprüfe, ob zielzahl in der Liste vorkommt
    if zielzahl in roll:
        # wird die Summe der Zielzahlen gebildet
        return sum(zahl for zahl in roll if zahl == zielzahl)
    else:
        return 0


def count_4s(roll):
    # Hier wird die gesuchte Zahl abgefragt
    zielzahl = 4

    # Überprüfe, ob zielzahl in der Liste vorkommt
    if zielzahl in roll:
        # wird die Summe der Zielzahlen gebildet
        return sum(zahl for zahl in roll if zahl == zielzahl)
    else:
        return 0


def count_5s(roll):
    # Hier wird die gesuchte Zahl abgefragt
    zielzahl = 5

    # Überprüfe, ob zielzahl in der Liste vorkommt
    if zielzahl in roll:
        # wird die Summe der Zielzahlen gebildet
        return sum(zahl for zahl in roll if zahl == zielzahl)
    else:
        return 0


def count_6s(roll):
    # Hier wird die gesuchte Zahl abgefragt
    zielzahl = 6

    # Überprüfe, ob zielzahl in der Liste vorkommt
    if zielzahl in roll:
        # wird die Summe der Zielzahlen gebildet
        return sum(zahl for zahl in roll if zahl == zielzahl)
    else:
        return 0


#######################################################################################################################


def ist_dreier_pasch(roll):
    for zahl in roll:
        if roll.count(zahl) == 3:
            l1 = sum(roll)
            return l1
    else:
        l1 = 0
    return l1


def ist_vierer_pasch(roll):
    for zahl in roll:
        if roll.count(zahl) == 4:
            l2 = sum(roll)
            return l2
    else:
        l2 = 0
    return l2


def ist_full_house(roll):
    sort_roll = sorted(roll)

    dreierpasch = False
    for zahl in sort_roll:
        if sort_roll.count(zahl) == 3:
            dreierpasch = True
            break

    zweierpasch = False
    for zahl in sort_roll:
        if roll.count(zahl) == 2 and zahl != roll[roll.index(zahl) - 1]:
            zweierpasch = True
            break
    l3 = 25 if dreierpasch and zweierpasch else 0

    return l3


def ist_kleine_strasse(roll):
    if [1, 2, 3, 4] in roll and 5 not in roll:
        l4 = 30
    elif [2, 3, 4, 5] in roll and (6 not in roll and 1 not in roll):
        l4 = 30
    elif [3, 4, 5, 6] in roll and 2 not in roll:
        l4 = 30
    else:
        l4 = 0
    return l4


def ist_grosse_strasse(roll):

    if {1, 2, 3, 4, 5}.issubset(roll) or {2, 3, 4, 5, 6}.issubset(roll):
        l5 = 40
    else:
        l5 = 0
    return l5


def ist_kniffel(roll):
    for zahl in roll:
        if roll.count(zahl) == 5:
            l6 = sum(roll)
            return l6
    else:
        l6 = 0
    return l6


def chance(roll):
    l7 = sum(roll)
    return l7
