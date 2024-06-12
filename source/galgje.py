class Galgje:
    def __init__(self, woord, beurten=6):
        self.woord = woord
        self.woord_lc = woord.lower()
        self.aantal_beurten = beurten
        self.geraden = False
        self.kapot = False
        self.al_geprobeerd = ''
        self.huidig_woord = '.' * len(woord)

    def __str__(self):
        if self.kapot:
            return f'Ai, je bent opgehangen.\n{self.woord}'
        if not self.geraden:
            return f'Je hebt nog {self.aantal_beurten} beurten.\n{self.huidig_woord}'
        return f'Proficiat! Je hebt het woord geraden!\n{self.woord}'

    def raadLetter(self, letter: str):
        if self.geraden or self.kapot:
            return 'Sorry, het spel is reeds voorbij.'

        if not is_valid_letter(letter):
            return 'De invoer is geen geldige letter.'

        if letter in self.al_geprobeerd:
            return 'De letter is al eens geprobeerd.'

        self.al_geprobeerd += letter
        aantal = hoeveel_keer_letter_in_woord(letter, self.woord_lc)

        if aantal > 0:
            self.huidig_woord = vervang_letter(self.huidig_woord, letter, self.woord)
            if self.huidig_woord == self.woord:
                self.geraden = True
                return f'Correct: letter {letter} komt {aantal} keer voor in het woord.\nProficiat! Je hebt het woord geraden!\n{self.woord}'
            else:
                return f'Correct: letter {letter} komt {aantal} keer voor in het woord.\nJe hebt nog {self.aantal_beurten} beurten.\n{self.huidig_woord}'
        else:
            self.aantal_beurten -= 1
            if self.aantal_beurten == 0:
                self.kapot = True
                return f'Fout: letter {letter} komt niet voor in het woord.\nAi, je bent opgehangen.\n{self.woord}'
            else:
                return f'Fout: letter {letter} komt niet voor in het woord.\nJe hebt nog {self.aantal_beurten} beurten.\n{self.huidig_woord}'


