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
    global bet_amount, bet_display, money
    game = Toplevel(menu)
    game.title("Texas Hold-Em Poker")
    game.geometry("800x600")
    game.focus()

    bet_question = Label(game, text="How Much Do You Want To Bet? (Default is $20)", pady="15px")
    bet_question.pack()
    bet_input = Text(game, height=1, width=5)
    bet_input.pack()

    bet_display = Label(game, text="Current Bet: $0")
    bet_display.pack(pady=(25, 0))
    
    def on_enter_pressed(key):
        global money, bet_amount
        try:
            # Get the text from the input widget and strip whitespace
            bet_text = bet_input.get("1.0", "end-1c").strip()
        
            if int(bet_text) < 20:
                bet_amount = 20
            elif int(bet_text) >= money:
                bet_amount = money

            money -= bet_amount
            
            balance = Label(game, text=f"Balance: ${money}")
            balance.pack()
            # Update the display label
            bet_display.config(text=f"You have ${bet_amount} On This Hand")
            
        except ValueError:
            bet_display.config(text="Please enter a valid number")
    
    # Bind the Enter key to the text widget
    bet_input.bind("<Return>", on_enter_pressed)

play_button = Button(menu, text="Play", width="15", command=play_game)
play_button.pack()

menu.mainloop()