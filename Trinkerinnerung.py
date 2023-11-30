import time
import ctypes
from datetime import datetime, timedelta

def trink_erinnerung():
    # Funktion zur Anzeige einer Benachrichtigung (MessageBox)
    ctypes.windll.user32.MessageBoxW(0, "Haben Sie Wasser getrunken?", "Trinkerinnerung", 1)

def trinken_check():
    while True:
        # Benutzer nach dem Trinkverhalten fragen
        antwort = input("Haben Sie Wasser getrunken? (ja/nein): ").lower()
        
        # Überprüfen, ob die Eingabe gültig ist (nur 'ja' oder 'nein' erlaubt)
        if antwort in ('ja', 'nein'):
            return antwort == 'ja'
        else:
            print("Ungültige Eingabe. Bitte antworten Sie mit 'ja' oder 'nein'.")

def trinken_aufforderung():
    # Aufforderung zum Trinken
    print("Bitte trinken Sie etwas Wasser!")

def gut_gemacht_meldung():
    # Meldung für den Fall, dass der Benutzer Wasser getrunken hat
    print("Gut gemacht!")

def main():
    try:
        while True:
            # Trinkerinnerung anzeigen
            trink_erinnerung()

            # Aktuelle Uhrzeit abrufen
            aktuelle_zeit = datetime.datetime.now()
            
            # Warten für 20 Minuten (1200 Sekunden)
            time.sleep(1200)
            
            # Überprüfen, ob der Benutzer Wasser getrunken hat
            if trinken_check():
                gut_gemacht_meldung()
            else:
                trinken_aufforderung()
    except KeyboardInterrupt:
        # Meldung, wenn das Programm durch Tastaturunterbrechung beendet wird (nur für Testzwecke)
        print("\nProgramm wurde beendet.")





    