# Kattenasiel - Flask Webapplicatie

Dit is een eenvoudige Flask-webapplicatie voor het beheren van katten in een kattenasiel. Hier kunnen gebruikers katten toevoegen, hun informatie bij werken en hun dagelijkse voedselconsumptie bij houden.

## Installatie

Volg deze stappen om de applicatie op uw computer te installeren en uit te voeren:

1. Zorg ervoor dat u Python 3.7 of hoger geïnstalleerd heeft op uw computer via de link:

https://www.python.org/downloads/


2. Installeer de vereiste pakketten met behulp van het volgende commando:


Navigeer naar de map waar de applicatie is gedownload. Unzip de map. 

Voor Windows (Command Prompt):

Type in de search bar "cmd" en druk op ENTER. Nu opent er een Command prompt. Kopieer en plak de volgende commando's (Kan in een keer)
	
py -m pip install -r requirements.txt
set FLASK_APP=base.py
py -m flask db init
py -m flask db migrate
py -m flask db upgrade


Voor Linux:

Open een terminal en kopieer de volgende commando's:
pip install -r requirements.txt
export FLASK_APP=base.py    
flask db init
flask db migrate
flask db upgrade

Deze stappen hoeven maar een enkele keer gedaan te worden. 
    
3. Nu kunt U de applicatie starten door in de terminal dit commando uit te voeren:

py -m flask run (Windows)
flask run (Linux)

4. Open uw webbrowser en ga naar `http://localhost:5000` om de applicatie te gebruiken.

## Functies

Deze Flask-webapplicatie biedt de volgende functies:

- Lijst met alle katten in het asiel
- Een kat toevoegen en verwijderen aan/uit het asiel
- Informatie over een kat bijwerken
- Dagelijkse voedselconsumptie van een kat bijhouden
