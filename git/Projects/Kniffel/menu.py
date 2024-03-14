def ladescreen():
    import time
    import sys

    def update_loading_bar(percentage):
        bar_length = 50
        block = int(round(bar_length * percentage))
        progress = "[" + "#" * block + " " * (bar_length - block) + "]"
        sys.stdout.write(f"\r{progress} {int(percentage * 100)}%")
        sys.stdout.flush()

    def blink_loading_bar():
        for _ in range(5):  # Blinkt 5-mal während der Pause
            sys.stdout.flush()
            sys.stdout.write("\r[#############################                     ] 69%")
            sys.stdout.flush()
            time.sleep(0.4)
            sys.stdout.write("\r[##############################                    ] 69%")
            sys.stdout.flush()
            time.sleep(0.4)

    def ladebalken():
        for i in range(70):  # Bis 60 % normal
            update_loading_bar(i / 100)
            time.sleep(0.05)

        blink_loading_bar()  # Blinkt während der Pause bei 60 %

        for i in range(70, 101, 2):  # Schneller von 61 % bis 100 %
            update_loading_bar(i / 100)
            time.sleep(0.025)
        update_loading_bar(1.0)  # Setze den Ladebalken auf 100 %

        print("\nLaden abgeschlossen.")
        print()

    # Beispielaufruf
    ladebalken()

    print("/////////////   /////////////    /////////////   /////////////   /////////////    /////////////")
    time.sleep(0.5)
    print("///       ///   ///     o ///    /// o     ///   /// o   o ///   /// o   o ///    /// o   o ///")
    time.sleep(0.5)
    print("///   o   ///   ///       ///    ///   o   ///   ///       ///   ///   o   ///    /// o   o ///")
    time.sleep(0.5)
    print("///       ///   /// o     ///    ///     o ///   /// o   o ///   /// o   o ///    /// o   o ///")
    time.sleep(0.5)
    print("/////////////   /////////////    /////////////   /////////////   /////////////    /////////////")
    time.sleep(0.5)
    print()
    print()
    print("///////////////////////////////////////////////////////////////////////////////////////////////")
    time.sleep(0.5)
    print("////////////  ///   //  ///////  ///  ///       ///       ///       ///  //////////////////////")
    time.sleep(0.5)
    print("////////////  //  ////    /////  ///  ///  ////////  ////////  ////////  //////////////////////")
    time.sleep(0.5)
    print("////////////     /////  //  ///  ///  ///     /////     /////     /////  //////////////////////")
    time.sleep(0.5)
    print("////////////     /////  ////  /  ///  ///  ////////  ////////  ////////  //////////////////////")
    time.sleep(0.5)
    print("////////////  //  ////  //////   ///  ///  ////////  ////////  ////////  //////////////////////")
    time.sleep(0.5)
    print("////////////  ///   //  ///////  ///  ///  ////////  ////////       ///       /////////////////")
    time.sleep(0.5)
    print("///////////////////////////////////////////////////////////////////////////////////////////////")
    time.sleep(0.5)
    print("             by      Sergiy Stuempel     &       Markus Finger                                 ")
    time.sleep(0.5)
    print("                                IT-Projekt 1. Semester                                         ")
    time.sleep(0.5)
    print()
    print("/////////////   /////////////    /////////////   /////////////   /////////////    /////////////")
    time.sleep(0.5)
    print("/// o   o ///   /// o   o ///    /// o   o ///   ///     o ///   /// o     ///    ///       ///")
    time.sleep(0.5)
    print("/// o   o ///   ///   o   ///    ///       ///   ///   o   ///   ///       ///    ///   o   ///")
    time.sleep(0.5)
    print("/// o   o ///   /// o   o ///    /// o   o ///   /// o     ///   ///     o ///    ///       ///")
    time.sleep(0.5)
    print("/////////////   /////////////    /////////////   /////////////   /////////////    /////////////")
    time.sleep(0.5)


def frage_spieleranzahl():
    print()
    print("Herzlich Willkommen zu Kniffel.")
    print()
    while True:
        try:
            spieleranzahl = int(input('Geben Sie die Spieleranzahl an: '))
            print()
        except ValueError:
            print('Ihre Eingabe ist nicht Korrekt. Bitte geben Sie eine ganze Zahl an!')
            continue
        else:
            break
    return spieleranzahl


def eingabe_namen(spieleranzahl):
    count = 1
    namen_inp = []
    while count <= spieleranzahl:
        namen_inp.append(input(f'Geben Sie bitte einen Namen ein Spieler {count}: '))
        count += 1

    if spieleranzahl > 1:
        print()
        print(f'Es wird ein Spiel mit {spieleranzahl} Spielern erstellt.')
        print()
    else:
        print()
        print('Es wird ein Spiel mit einem Spieler erstellt.')
        print()

    count2 = 1
    while count2 <= spieleranzahl:
        print(f'Spieler {count2} = {namen_inp[count2 - 1]}')
        count2 += 1

    return namen_inp


def abfrage_spielstart():
    x = False
    print()
    while x is False:
        start_inp = input('Soll das Spiel gestartet werden? ')
        print()
        if start_inp == 'ja':
            x = True
            return True
        elif start_inp == 'nein':
            x = True
            return False
        else:
            print('Ihre Eingabe kann nicht erkannt werden. Bitte geben sie "ja" oder "nein" an.')
            print()
            continue
