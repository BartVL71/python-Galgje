from source.galgje import Galgje

import tkinter as tk
from tkinter import messagebox
from string import ascii_uppercase
import random

if __name__ == "__main__":
    venster = tk.Tk()
    venster.title = 'Galgje'
    venster.size = '300x200'
    woord = 'zagevent'
    spel = Galgje(woord)
    venster.mainloop()

'''
photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"),
          PhotoImage(file="images/hang3.png"), PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"),
          PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"), PhotoImage(file="images/hang8.png"),
          PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"),
          PhotoImage(file="images/hang11.png")]
imgLabel = Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)

lblWord = StringVar()
Label(window, text=g).grid(row=0, column=3, columnspan=6, padx=10)
print (g.huidig_woord)
n = 0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c: g.raadLetter(c), font=('Helvetica 24'), width=4).grid(row=1 + n // 9,
                                                                                              column=n % 9)
    n += 1
#Button(window, text="Nieuw\nspel", command=lambda: newGame(), font=("Helvetica 10 bold")).grid(row=3, column=8)

'''
