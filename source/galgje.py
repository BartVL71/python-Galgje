# controleert of de ingevoerde letter effectief een letter is
# eigenlijk niet nodig met deze GUI
def isValidLetter(invoer):
    letter = str(invoer)
    if len(letter) > 1:
        return False
    if letter.isalpha():  # is de invoer een letter?
        return True
    return False

# telt hoeveel keer de gegeven letter in het woord voorkomt
def hoeveelKeerLetterInWwoord(letter, woord):
    woord=woord.lower()
    letter=letter.lower()
    aantal = woord.count(letter)  # hoeveel keer letter in woord?
    return aantal

# vervangt elke keer een letter geraden is, het '-' teken door de letter
def vervangLetter(te_vervangen_woord, letter, woord):
    resultwoord = te_vervangen_woord
    for x in range(len(woord)):
        if (woord[x] == letter) or (woord[x] == letter.upper()):
            resultwoord = resultwoord[:x] + woord[x] + resultwoord[x + 1:]
    return resultwoord
class Galgje:
    def __init__(self, woord, beurten=6):
        self.woord = woord
        self.aantal_beurten = beurten
        self.geraden = False
        self.kapot = False
        self.al_geprobeerd = ''
        self.huidig_woord = '-' * len(woord)

    def __str__(self):
        if self.kapot:
            return f'Ai, je bent opgehangen.'
        if not self.geraden:
            return f'Je hebt nog {self.aantal_beurten} beurten.\n{self.huidig_woord}'
        return f'Proficiat! Je hebt het woord geraden!'

    #deze method verwerkt een gerade letter en update alle nodige attributen indien nodig
    def raadLetter(self, letter: str):
        if self.geraden or self.kapot:
            return 'Sorry, het spel is reeds voorbij.\n Klik "Opnieuw" om een nieuw spel te starten.'
        if self.aantal_beurten ==1:
            beurtstring = 'beurt'
        else:
            beurtstring = 'beurten'

        if not isValidLetter(letter):
            return f'De invoer is geen geldige letter.\n Je hebt nog {self.aantal_beurten} {beurtstring}.'

        if letter in self.al_geprobeerd:
            return f'De letter {letter} is al eens geprobeerd. \n Je hebt nog {self.aantal_beurten} {beurtstring}.'

        self.al_geprobeerd += letter
        aantal = hoeveelKeerLetterInWwoord(letter, self.woord)

        if aantal > 0:
            self.huidig_woord = vervangLetter(self.huidig_woord, letter, self.woord)
            if self.huidig_woord == self.woord:
                self.geraden = True
                return f'Correct: letter {letter} komt {aantal} keer voor in het woord.\nProficiat! Je hebt het woord geraden!'
            else:
                return f'Correct: letter {letter} komt {aantal} keer voor in het woord.\nJe hebt nog {self.aantal_beurten} {beurtstring}.'
        else:
            self.aantal_beurten -= 1
            if self.aantal_beurten == 0:
                self.kapot = True
                return f'Fout: letter {letter} komt niet voor in het woord.\nAi, je bent opgehangen. '
            else:
                if self.aantal_beurten == 1:
                    beurtstring = 'beurt'
                else:
                    beurtstring = 'beurten'
                return f'Fout: letter {letter} komt niet voor in het woord.\nJe hebt nog {self.aantal_beurten} {beurtstring}.'


