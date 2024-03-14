def spieldata(spieleranzahl, spielernamen):

    spieldaten = []
    gewinnkarte = ["         Spielername", "                 1er", "                 2er", "                 3er",
                   "                 4er", "                 5er", "                 6er", "              gesamt",
                   "  Bonus >= 63 Punkte", "  gesamt oberer Teil", "         Dreierpasch", "         Viererpasch",
                   "          Full-House", "       Kleine Straße", "        Große Straße", "             Kniffel",
                   "              Chance", " gesamt unterer Teil", "  gesamt oberer Teil", "            Endsumme"]
    gewinnkarte2 = ["                    ", "      nur 1er zählen", "      nur 2er zählen", "      nur 3er zählen",
                    "      nur 4er zählen", "      nur 5er zählen", "      nur 6er zählen", "                  ->",
                    "             plus 35", "                  ->", "   alle Augen zählen", "   alle Augen zählen",
                    "           25 Punkte", "           30 Punkte", "           40 Punkte", "           50 Punkte",
                    "   alle Augen zählen", "                  ->", "                  ->", "                  ->"]
    positionen = ["     ", " 1 ->", " 2 ->", " 3 ->",
                  " 4 ->", " 5 ->", " 6 ->", "     ",
                  "     ", "     ", " 7 ->", " 8 ->",
                  " 9 ->", "10 ->", "11 ->", "12 ->",
                  "13 ->", "     ", "     ", "     "]

    spieldaten.append(gewinnkarte)
    spieldaten.append(gewinnkarte2)
    spieldaten.append(positionen)

    for i in range(spieleranzahl):
        temp = [None] * 20
        temp[0] = spielernamen[i]
        spieldaten.append(temp)

    return spieldaten


def spielerliste_ausgabe(spieldaten):
    for i in range(len(spieldaten[0])):
        for j in range(len(spieldaten)):
            value = spieldaten[j][i]
            print(f"{value:<25}" if value is not None else "                         ", end=" ")
        print()
