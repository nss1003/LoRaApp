# Was ist das Projekt

Dieses Projekt beschäftigt sich mit der drahtlosen Übertragung von Daten
über langen Strecken.

# Inhalt der CD

Dieses Verzeichniss beinhaltet:

- Die Datei "references.bib" enthält die benutzten online Quellen und Bücher.
- Die Datei "Bachelorarbeit_Silvere_Sacker_Ngoufack_5152681.pdf" ist der Bericht
zu dieser Bachelorarbeit.
- Das Verzeichnis "LoRa_Based_IoT_Endpoint_and_Gateway" enthält die Quellendateien 
(lora_app), die benutzte Bibliothek (libopencm3).

- Das Verzeichnis "Subscribe" enthält die Software zur Abonnierung des MQTT-Brokers.

# Ausführbare Datei herstellen

Die Software befindet sich in "lora_app".
- Herstellung/Kompilierung der Software: $ make all
- Software im Board laden: st-flash write lora_app.bin  0x8000000

# MQTT

Um den Datenaustausch zu beoabachten muss ein MQTT-Broker installiert werden.
- sudo apt-get install mosquitto
- sudo apt-get install mosquitto-clients

Die Datei "sub.py" kann gestartet werden. (Das Topic und die IP-Adresse des Servers müssen angepasst werden)

# Demo Video

Das Video zeigt wie die Software funktioniert.

