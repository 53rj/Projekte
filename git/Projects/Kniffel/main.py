

from menu import *
from game import *
from daten import *


while True:
    ladescreen()

    spieleranzahl = frage_spieleranzahl()

    spielernamen = eingabe_namen(spieleranzahl)

    spieldaten = spieldata(spieleranzahl, spielernamen)

    spielstart = abfrage_spielstart()

    spielerwechsel(spielernamen, spieleranzahl, spielstart, spieldaten)

    spielergebnis_anzeige(spieldaten, spieleranzahl, spielstart)

    break
