"""A Texas Hold-Em Poker in Python"""

import random

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

money = 100

# Create the decks
player_hand = []
cpu_hand = []

board = []

# Welcome the user to the game and asks for a initial bet

print()
print("Welcome To Texas Hold-Em Python")
print(f"You Currently Have ${money} To Bet With \n")

while True:
    try:
        bet_amount = int(input("How Much Do You Want To Bet? (Default is $20) \n"))
        if bet_amount < 20:
            bet_amount = 20
            break
        elif bet_amount >= money:
            bet_amount = money
            break
        else:
            break
    except ValueError:
        print(f"{bet_amount} Isnt a number")

if bet_amount < money:
    print(f"\nYou have Chosen To Bet ${bet_amount} \n")
else:
    print(f"\nYou have Chosen To Go All In \n")

'''
# ============================ ADD DEALING DECK TO THE USER AND CPU =========================== #
'''

cardsdealt = 0

while cardsdealt < 2:
    card = random.randint(0, len(deck) - 1)
    print(card)
    print(deck[card])

    cardsdealt += 1