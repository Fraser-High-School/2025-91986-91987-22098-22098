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
fold = False

# Create the decks
player_hand = []
cpu_hand = []

board = []

# Welcome the user to the game 

print()
print("Welcome To Texas Hold-Em Python")
print(f"You Currently Have ${money} To Bet With \n")
# asks for a initial bet and makes sure its a number
while True:
    try:
        bet_amount = input("How Much Do You Want To Bet? (Default is $20) \n")
        if int(bet_amount) < 20:
            bet_amount = 20
            break
        elif int(bet_amount) >= money:
            bet_amount = money
            break
        else:
            break
    except ValueError:
        print(f"{bet_amount} Isnt a number")

# tell user balance and how much they are playing for
money -= int(bet_amount)
print(f"\nBalance: ${money}")
print(f"You have ${bet_amount} On This Hand \n")

'''
# ============================ ADD DEALING DECK TO THE USER AND CPU =========================== #
'''

# deals 2 cards to the user and the cpu then removes from the deck
cardsdealt = 0

while cardsdealt < 2:
    card = random.randint(0, len(deck) - 1)
    player_hand.append(deck[card])
    deck.pop(card)

    card_2 = random.randint(0, len(deck) - 1)
    cpu_hand.append(deck[card_2])
    deck.pop(card_2)

    cardsdealt += 1

print(f"Your deck {player_hand}\n")

'''
# =========================================== first betting round ===========================================#
'''

action_r1 = input("what do you want to do (check, raise, fold)?\n")

if action_r1.lower() == "raise":
    betamnt = int(input("\nHow much do you want to bet? "))
    print(betamnt)
elif action_r1.lower() == "fold":
    fold = True

# tell user balance and how much they are playing for
money -= betamnt
print(f"\nBalance: ${money}")
print(f"You have ${int(bet_amount) + betamnt} On This Hand \n")

'''
# ======================================== Add the cards to the table =======================================#
'''

# deal 3 cards to the table then remove them from the deck
flopcardsdealt = 0

while flopcardsdealt < 3:
    card = random.randint(0, len(deck) - 1)
    board.append(deck[card])
    deck.pop(card)

    flopcardsdealt += 1

print(f"Table {board}\n")

'''
# =========================================== second betting round ===========================================#
'''

action_r2 = input("what do you want to do (check, raise, fold)?\n")

if action_r2.lower() == "raise":
    betamnt = int(input("How much do you want to bet? "))
    bet_amount += betamnt
    print(bet_amount)
elif action_r2.lower() == "fold":
    fold = True