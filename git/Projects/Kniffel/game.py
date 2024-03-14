def spielerwechsel(spielernamen, spieleranzahl, spielstart, spieldaten):
    runden_nummer = 13 * spieleranzahl
    count = 1
    if spielstart is True:
        while count <= runden_nummer:
            for spieler in spielernamen:
                print(f'{spieler} ist am Zug')
                print()
                for i in range(len(spieldaten[0])):
                    for j in range(len(spieldaten)):
                        value = spieldaten[j][i]
                        print(f"{value:<25}" if value is not None else "                         ", end=" ")
                    print()
                print()
                ergebnis = roll_dice()
                spielername = spieler
                count += 1
                tabellen_eintrag(spielernamen, spielername, ergebnis, spieldaten)
                zusammen_rechnen(spieldaten, spielernamen, spielername)
                print()


def roll_dice():
    import random

    lower_bound = 1
    upper_bound = 6

    def keeprolls():
        print()
        while True:
            response = input("Möchtest du deine Würfel behalten? (ja/nein)")
            if response in ["ja", "nein"]:
                return response
            else:
                print("Ungültige Eingabe, bitte 'ja' oder 'nein' eingeben!")

    w1 = random.randint(lower_bound, upper_bound)
    w2 = random.randint(lower_bound, upper_bound)
    w3 = random.randint(lower_bound, upper_bound)
    w4 = random.randint(lower_bound, upper_bound)
    w5 = random.randint(lower_bound, upper_bound)

    roll = [w1, w2, w3, w4, w5]

    print(f'Dein Würfelergebnis = {roll}')

    # Hiernach entscheidet der Spieler, welche Variablen der Liste roll behalten werden sollen und welche ersetzt
    # werden.
    availablererolls = 2
    print(f"Verfügbare Neuwürfe: {availablererolls}")

    while True:
        entscheidung = keeprolls()

        bereits_geworfen = []

        while entscheidung == "nein":
            availablererolls -= 1

            while True:
                try:
                    roll_number = int(input("Wie viele Würfel sollen neu geworfen werden?"))

                    if 1 <= roll_number <= 5:
                        break
                    else:
                        print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 5 eingeben.")
                except ValueError:
                    print("Ungültige Eingabe. Bitte eine ganze Zahl eingeben.")

            rrcount = 0

            if roll_number == 5:  # Wenn alle 5 Würfel neu geworfen werden sollen
                roll = [random.randint(lower_bound, upper_bound) for _ in range(5)]
                print(f'Dein Würfelergebnis = {roll}')
            else:
                while roll_number > rrcount:
                    reroll = input("Gib den Würfel ein, der neu geworfen werden soll (w1-w5):").lower()
                    print()

                    if reroll in ["w1", "w2", "w3", "w4", "w5"]:
                        index = int(reroll[1]) - 1

                        # Überprüfen, ob der Würfel bereits neu geworfen wurde
                        if index in bereits_geworfen:
                            print("Dieser Würfel wurde bereits neu geworfen. Bitte wähle einen anderen.")
                            continue

                        roll[index] = random.randint(lower_bound, upper_bound)
                        bereits_geworfen.append(index)
                        rrcount += 1
                    else:
                        print("Ungültige Eingabe, bitte 'w1', 'w2', 'w3', 'w4' oder 'w5' eingeben.")
                        continue

                print(f'Dein Würfelergebnis = {roll}')
                bereits_geworfen = []

            print(f"Verfügbare Neuwürfe: {availablererolls}")

            if availablererolls == 0:
                print("Keine weiteren Neuwürfe mehr möglich.")
                break

            entscheidung = keeprolls()

        return roll


def tabellen_eintrag(spielernamen, spielername, ergebnis, spieldaten):
    import liste
    spalte = spielernamen.index(spielername) + 3

    pos1 = "1: nur Einser zählen"
    pos2 = "2: nur Zweier zählen"
    pos3 = "3: nur Dreier zählen"
    pos4 = "4: nur Vierer zählen"
    pos5 = "5: nur Fünfer zählen"
    pos6 = "6: nur Sechser zählen"
    pos7 = "7: Dreierpasch"
    pos8 = "8: Viererpasch"
    pos9 = "9: Full-House"
    pos10 = "10: Kleine Straße"
    pos11 = "11: Große Straße"
    pos12 = "12: Kniffel"
    pos13 = "13: Chance"

    while True:
        try:
            tabelle_position = int(input("Geben Sie die Position an wo Ihr Ergebnis eingetragen werden soll. 1-13: "))

            if 1 <= tabelle_position <= 13:
                if 1 <= tabelle_position <= 6:
                    if spieldaten[spalte][tabelle_position] is None:
                        break
                    else:
                        print('Die Position ist bereits vergeben. Bitte eine freie Stelle auswählen')
                elif 7 <= tabelle_position <= 13:
                    tabelle_position_unten = tabelle_position + 3
                    if spieldaten[spalte][tabelle_position_unten] is None:
                        break
                    else:
                        print('Die Position ist bereits vergeben. Bitte eine freie Stelle auswählen')
            else:
                print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 13 eingeben.")
        except ValueError:
            print("Ungültige Eingabe. Bitte eine ganze Zahl eingeben.")

    if tabelle_position == 1:
        eintrag = liste.count_1s(ergebnis)
        spieldaten[spalte][1] = eintrag
        print(f'Ihre Eingabe wird bei Position {pos1} eingetragen')
    elif tabelle_position == 2:
        eintrag = liste.count_2s(ergebnis)
        spieldaten[spalte][2] = eintrag
        print(f'Ihre Eingabe wird bei Position {pos2} eingetragen')
    elif tabelle_position == 3:
        eintrag = liste.count_3s(ergebnis)
        spieldaten[spalte][3] = eintrag
        print(f'Ihre Eingabe wird bei Position {pos3} eingetragen')
    elif tabelle_position == 4:
        eintrag = liste.count_4s(ergebnis)
        spieldaten[spalte][4] = eintrag
        print(f'Ihre Eingabe wird bei Position {pos4} eingetragen')
    elif tabelle_position == 5:
        eintrag = liste.count_5s(ergebnis)
        spieldaten[spalte][5] = eintrag
        print(f'Ihre Eingabe wird bei Position {pos5} eingetragen')
    elif tabelle_position == 6:
        eintrag = liste.count_6s(ergebnis)
        spieldaten[spalte][6] = eintrag
        print(f'Ihre Eingabe wird bei Position {pos6} eingetragen')
    elif tabelle_position == 7:
        eintrag = liste.ist_dreier_pasch(ergebnis)
        spieldaten[spalte][10] = eintrag
        print(f'Ihre Eingabe wird bei Position {pos7} eingetragen')
    elif tabelle_position == 8:
        eintrag = liste.ist_vierer_pasch(ergebnis)
        spieldaten[spalte][11] = eintrag
        print(f'Ihre Eingabe wird bei Position {pos8} eingetragen')
    elif tabelle_position == 9:
        eintrag = liste.ist_full_house(ergebnis)
        spieldaten[spalte][12] = eintrag
        print(f'Ihre Eingabe wird bei Position {pos9} eingetragen')
    elif tabelle_position == 10:
        eintrag = liste.ist_kleine_strasse(ergebnis)
        spieldaten[spalte][13] = eintrag
        print(f'Ihre Eingabe wird bei Position {pos10} eingetragen')
    elif tabelle_position == 11:
        eintrag = liste.ist_grosse_strasse(ergebnis)
        spieldaten[spalte][14] = eintrag
        print(f'Ihre Eingabe wird bei Position {pos11} eingetragen')
    elif tabelle_position == 12:
        eintrag = liste.ist_kniffel(ergebnis)
        spieldaten[spalte][15] = eintrag
        print(f'Ihre Eingabe wird bei Position {pos12} eingetragen')
    elif tabelle_position == 13:
        eintrag = liste.chance(ergebnis)
        spieldaten[spalte][16] = eintrag
        print(f'Ihre Eingabe wird bei Position {pos13} eingetragen')


def zusammen_rechnen(spieldaten, spielernamen, spielername):
    spalte2 = spielernamen.index(spielername) + 3
    summe1 = 0
    summe2 = 0

    for i in spieldaten[spalte2][1:7]:
        if i is not None:
            summe1 += i

    for i in spieldaten[spalte2][11:18]:
        if i is not None:
            summe2 += i

    spieldaten[spalte2][7] = summe1
    spieldaten[spalte2][17] = summe2
    if spieldaten[spalte2][7] >= 63:
        spieldaten[spalte2][8] = 35
    else:
        spieldaten[spalte2][8] = 0

    spieldaten[spalte2][9] = spieldaten[spalte2][8] + spieldaten[spalte2][7]

    spieldaten[spalte2][18] = spieldaten[spalte2][9]

    spieldaten[spalte2][19] = spieldaten[spalte2][17] + spieldaten[spalte2][18]


def spielergebnis_anzeige(spieldaten, spieleranzahl, spielstart):
    from daten import spielerliste_ausgabe

    if spielstart is True:
        count = 1
        spalte3 = 3
        punkte_endstand = []
        name_gewinner = []
        while count <= spieleranzahl:
            punkte_spieler = spieldaten[spalte3][19]
            name_spieler = spieldaten[spalte3][0]
            punkte_endstand.append(punkte_spieler)
            name_gewinner.append(name_spieler)
            count += 1
            spalte3 += 1

        punkte_gewinner = max(punkte_endstand)
        index_max_punkte = punkte_endstand.index(max(punkte_endstand))
        name_gewinner = name_gewinner[index_max_punkte]
        print()
        print(f'Glückwunsch, {name_gewinner} hat mit {punkte_gewinner} Punkten gewonnen!')
        print()
        spielerliste_ausgabe(spieldaten)
