import requests
from bs4 import BeautifulSoup
from string import ascii_lowercase
import os
import random


# Haalt een willekeurig woord uit een bestand
def extractRandomWordFromFile(file_path):
    try:
        with open(file_path, 'r') as file:
            allText = file.read()
            words = list(map(str, allText.split()))
            word = random.choice(words)
        return word
    except Exception as e:
        print(f"Fout: {e}")
        return None


# controleert of het gegeven woord geen speciale karakters bevat en of het niet te lang of niet te kort is
def isValidWord(woord):
    valid = True
    if len(woord) < 4 or len(woord) > 18:
        valid = False
    else:
        for x in woord:
            if x not in ascii_lowercase:
                valid = False
                break
        return valid


# scrapet een woord uit de random word generator op https://willekeurigwoord.franq.nl/
# woord zit in een <h2> tag
# indien dat niet lukt, leest een woord uit lokaal tekstbestand
def scrapeWord():
    URL = "https://willekeurigwoord.franq.nl/"
    schraapwoord = '@'  # niet-valide woord om mee te starten zodat de eerste lus zeker gedaan wordt
    while not isValidWord(schraapwoord):
        try:
            response = requests.get(URL)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                # Vind de h2 tag
                h2_tag = soup.find('h2')
                # Checkt of er een h2-tag gevonden wordt
                if h2_tag:
                    # Haalt de tekst uit de h2 tag
                    schraapwoord = h2_tag.get_text()
                    valid = isValidWord(schraapwoord)  # Is het een valide woord? (geen spec. tekens of te lang of te kort)
                    if valid:
                        return schraapwoord
                    else:
                        continue
            else:  # website werkt niet? haal woord uit bestandje
                schraapwoord = extractRandomWordFromFile('data/wordlist.txt')
                return schraapwoord
        except:
            schraapwoord = extractRandomWordFromFile('data/wordlist.txt')
            return schraapwoord


# genereer een lijst van x woorden om offline te gebruiken

def voegWoordToeAanFile(file_path, woord):
    try:
        with open(file_path, 'a') as file:
            file.write(woord + '\n')
    except Exception as e:
        print(f"Fout: {e}")


def genereerWoordenlijst(bestandsnaam, aantal):
    os.makedirs(os.path.dirname(bestandsnaam), exist_ok=True)  # bestaat het bestand? Zoniet, maak het aan
    for x in range(0, aantal):
        woord = scrapeWord()
        voegWoordToeAanFile(bestandsnaam, woord)
