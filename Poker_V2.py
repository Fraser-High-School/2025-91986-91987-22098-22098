import random
from tkinter import *

menu = Tk()
menu.title("Main Menu - Texas Hold-Em Poker")
menu.geometry("800x600")



money = 100

deck = [
    "K♣️", "K♠️", "K♥️", "K♦️",
    "Q♣️", "Q♠️", "Q♥️", "Q♦️",
    "J♣️", "J♠️", "J♥️", "J♦️",
    "10♣️", "10♠️", "10♥️", "10♦️",
    "9♣️", "9♠️", "9♥️", "9♦️",
    "8♣️", "8♠️", "8♥️", "8♦️",
    "7♣️", "7♠️", "7♥️", "7♦️",
    "6♣️", "6♠️", "6♥️", "6♦️",
    "5♣️", "5♠️", "5♥️", "5♦️",
    "4♣️", "4♠️", "4♥️", "4♦️",
    "3♣️", "3♠️", "3♥️", "3♦️",
    "2♣️", "2♠️", "2♥️", "2♦️",
    "A♣️", "A♠️", "A♥️", "A♦️",
    ]
# Shuffle the deck
random.shuffle(deck)

# Create the decks
player_hand = []
cpu_hand = []
starting_money = money
board = []

# Welcome the user to the game 
title_label = Label(menu, text="Welcome To Texas Hold-Em Python", pady="15px")
title_label.pack()

def play_game():
    game = Toplevel(menu)
    game.title("Texas Hold-Em Poker")
    game.geometry("800x600")
    game.focus()

    money_label = Label(game, text=f"You Currently Have ${money} To Bet With", pady="25px")
    money_label.pack()

play_button = Button(menu, text="Play", width="15", command=play_game)
play_button.pack()




menu.mainloop()