Installation:

- mit git clone https://github.com/Felix-95/programming_challenge in Ordner herunterladen
- Im base Ordner des Projects ein Virtual Environment erschaffen und dieses aktiveren
- pip install -r requirements.txt
- /src/main.py ausführen

Sollte ein Problem mit dem Browser auftreten kann dieser unter 
https://github.com/mozilla/geckodriver/releases heruntergeladen in /brower platziert werden.


Beschreibung:

Die Variablen (außer vorgegebene Bezeichnungen) und Kommentare im Code sind auf Englisch. 
Ich habe versucht mich an Konventionen, was Aufbau des Projektes, 
Strukturierung des Codes und Kommentare betrifft, zu halten.

Das Webscraping führe ich mit dem Modul Selenium durch, da ich damit die meiste Erfahrung habe.
Gesuchte Produktnamen und Marken werden aus der Datei /data/products.xls ausgelesen. 
Unterschiedliche Produkte können durch Ändern der Tabelle gesucht werden.
Die gesammelten Informationen werden im Ordner output im XML Format gespeichert und mit der Urzeit benannt,
um möglicherweise einen zeitlichen Verlauf dazustellen.

Sollten sich die Anforderungen (Produkteigenschaften) ändern, kann dies leicht
durch Hinzufügen im Code in der Funktion/src/scraper.get_product_properties erreicht werden.
Kann eine Produktnamen-Marken-Kombination nicht gefunden werden,
so hat das Produkt in der XML Datei ein Element "error" in dem steht worin der Fehler besteht.
Das Lieferdatum der Produkte konnt ich nicht finden, deshalb habe ich stattdessen die Eigenschaft 
"lieferbar" benutzt.

Um den Code zu testen, muss die Datei /src/test.py ausgeführt werden. 
Leider ist es mir nicht gelungen diese in den Ordner /tests unterzubringen
ohne die Hauptdateien und deren Imports zu ändern.

Eine weitere Schwachstelle der Tests ist dass mehrere Test eine Funktion benutzten und somit
bei Versagen dieser, mehrere Test fehlschlagen. Dies könnte noch verbessert werden.

Für das Projekt inkl. Tests habe ich ca. 5 Stunden gebraucht. 



