from source.galgje import Galgje
from source.wordlist import scrapeWord

import ttkbootstrap as ttk
from ttkbootstrap.tooltip import ToolTip

from string import ascii_lowercase
import random


# maakt een lijst van galgje images en zet ze in een lijst om er gemakkelijk aan te kunnen
def makeLabelImageList():
    imglist = []
    for x in range(0, 7):
        imgnaam = 'images/Hangman-' + str(x) + '.png'
        img = ttk.PhotoImage(file=imgnaam)  # Figuur maken om in Label te zetten
        imglist.append(img)
    return imglist


# kiest een willekeurige letter uit de lijst van alle letters, min deze die al geprobeerd zijn
def chooseRandomLetter(let):
    letterlist = ascii_lowercase  # Oorspr. lijst bestaat uit alle kleine letters
    for let in letterlist:
        if let in spel.al_geprobeerd:
            letterlist = letterlist.replace(let, '')  # verwijder letter uit lijst als die al geprobeerd is
    random_let = random.choice(letterlist)  # kies willekeurige letter
    return random_let


# Steekt een letter in de raadLetter method van de class Galgje.
# Genereert de boodschappen. Update de nodige labels met de configure() method
def getLetter(let):
    if let == '?':
        let = chooseRandomLetter(let)
    boodschap = spel.raadLetter(let)  # raadLetter method ondersteunt enkel lowercase!
    beurt = 6 - spel.aantal_beurten
    nummer = lettersduos[let]  # bij welk nummer van Button hoort deze letter?
    img = imglist[beurt]  # nieuwe galgfiguur
    lblImage.configure(image=img)  # label updaten
    if spel.geraden or spel.kapot:  # spel gedaan?
        if spel.kapot:
            lblWoord.configure(text=spel.woord, foreground='red')  # label updaten met gegeven woord in rood
        else:
            lblWoord.configure(text=spel.woord, foreground='green')  # label updaten met gegeven woord in rood
    else:
        lblWoord.configure(text=spel.huidig_woord)  # label updaten met nog niet geraden woord
        # update button, zodat duidelijk wordt dat deze letter al eens geraden is
        btnLetter[nummer].configure(state='disabled')
    lblBoodschap.configure(text=boodschap, foreground='black')


# start een nieuw spel. Update de nodige labels. Reset alle buttons
def startSpel():
    woord = scrapeWord()
    global spel
    spel = Galgje(woord, 6)  # spel initialiseren
    beurt = 6 - spel.aantal_beurten
    img = imglist[beurt]  # nieuwe galgfiguur
    lblImage.configure(image=img)  # label updaten
    fontsize = 'Courier 50'
    if len(spel.woord) > 16:
        fontsize = 'Courier 40'
    lblWoord.configure(text=spel.huidig_woord, foreground='black', font=fontsize)  # label updaten
    boodschap = f'Welkom bij Galgje. \nJe hebt nog {spel.aantal_beurten} beurten.'  # boodschap vooraleer het spel begint
    lblBoodschap.configure(text=boodschap, foreground='black')
    for n, c in enumerate(ascii_lowercase):
        btnLetter[n].configure(style='TButton', state='enabled')  # buttons met letters resetten, niet die met het ?
    return spel


# GUI initialiseren
venster = ttk.Window(title='Galgje by Bart')  # venster initialiseren
venster.wm_minsize(width=600, height=560)  # minimum grootte van het venster
icoon = 'images/Hangman-Game.ico'
venster.wm_iconbitmap(icoon)
# Frame voor de titel
imglist = makeLabelImageList()
frmTitel = ttk.Frame(venster, height=50, width=600)
frmTitel.pack(side='top')
initLabel = ttk.Label(frmTitel, text='Galgje by Bart', font=('Arial', 30))
initLabel.pack(side='left')
# spel initialiseren
woord = scrapeWord()
spel = Galgje(woord, 6)  # spel initialiseren
beurt = 6 - int(spel.aantal_beurten)
# frame met galg en woord
frmSpel = ttk.Frame(venster, height=200, width=600)
frmSpel.pack()
lblImage = ttk.Label(frmSpel, padding=10)  # label voor figuur galg aanmaken
lblImage.pack(side='left')
img = imglist[beurt]  # converteren om img in label te zetten
lblImage.configure(image=img)
# label voor het woord, lettergrootte afhankelijk van de lengte van het woord
fontsize = 50
if len(spel.woord) > 16:
    fontsize = 40
lblWoord = ttk.Label(frmSpel, font=('Courier', fontsize), width=18)  # lettertype met gelijke space voor elk karakter
# Opmerking: width van een tekstlabel is het max. aantal karakters in de tekst!
lblWoord.pack(side='right')
lblWoord.configure(text=spel.huidig_woord, foreground='black')
# frame voor de boodschappen
frmBoodschap = ttk.Frame(venster, height=80, width=600)
frmBoodschap.pack()
boodschap = f'Welkom bij Galgje. \nJe hebt nog {spel.aantal_beurten} beurten.'  # boodschap vooraleer het spel begint
lblBoodschap = ttk.Label(frmBoodschap, font=('Arial', 18))  # label voor boodschappen aanmaken
lblBoodschap.pack(side='top')
lblBoodschap.configure(text=boodschap, foreground='black')
# frame voor de letters
frmLetters = ttk.Frame(venster, height=100, width=600)
frmLetters.pack()
# buttons met de letters op
s = ttk.Style()
s.configure('.', font=('Arial', 24))  # lettertype van alle volgende widgets instellen
btnLetter = []  # lijst van buttons initialiseren
letters = ascii_lowercase + '?'  # ascii_lowercase bevat alle kleine letters
duos = dict(enumerate(letters))  # elke letter krijgt een rangnummer, opslaan in een dictionary
lettersduos = {v: k for k, v in duos.items()}  # values en keys omwisselen, is nuttiger!
for n, c in enumerate(letters):  # n is rangnummer, c is letter op de button
    btnLetter.append(
        ttk.Button(frmLetters, text=c, command=lambda letter=c: getLetter(letter), style='TButton', state='enabled',
                   width=6, padding=1))
    btnLetter[n].grid(row=1 + n // 9, column=n % 9)  # drie rijen, negen kolommen
    if c == '?':
        btnLetter[n].configure(style='warning.TButton')
        ToolTip(btnLetter[n], text='Raad een willekeurige letter!', delay=0)
# buttons met Opnieuw en Einde op
frmBottom = ttk.Frame(venster, height=35, width=600)
frmBottom.pack()
btnNew = ttk.Button(frmBottom, text='Opnieuw', command=lambda: startSpel(), style='Outline.TButton', width=15,
                    padding=10)
btnNew.pack(side='left')
btnQuit = ttk.Button(frmBottom, text='Einde', command=lambda: exit(), style='Outline.TButton', width=15, padding=10)
btnQuit.pack(side='right')

venster.mainloop()
