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


def betting_round():
    global bet_amount, money
    action = input("what do you want to do (check, raise, fold)?\n")

    if action.lower() == "raise":
        betamnt = int(input("\nHow much do you want to bet? "))
        bet_amount = int(bet_amount) + betamnt
        
        # tell user balance and how much they are playing for
        money -= betamnt
        print(f"\nBalance: ${money}")
        print(f"You have ${bet_amount} On This Hand \n")
    elif action.lower() == "fold":
        fold
        # break


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

betting_round()

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

betting_round()

'''
# ======================================== Add another card to the table =======================================#
'''

# deal 1 card to the table then remove them from the deck
card = random.randint(0, len(deck) - 1)
board.append(deck[card])
deck.pop(card)

print(f"You have ${bet_amount} On This Hand ")
print(f"Your deck {player_hand}\n")

print(f"\nTable {board}\n")

'''
# =========================================== third betting round ===========================================#
'''

betting_round()


'''
# ======================================== Add final card to the table =======================================#
'''

# deal 1 card to the table then remove them from the deck
card = random.randint(0, len(deck) - 1)
board.append(deck[card])
deck.pop(card)

print(f"You have ${bet_amount} On This Hand ")
print(f"Your deck {player_hand}\n")

print(f"\nTable {board}\n")

'''
# =========================================== final betting round ===========================================#
'''

betting_round()


'''
# =========================================== detirmine winners round ===========================================#
'''

player_check = player_hand + board
cpu_check = cpu_hand + board
cpu_win = 0
win = 0

def get_hand_name(rank):
    hand_names = {
        9: "Royal Flush",
        8: "Straight Flush",
        7: "Four of a Kind",
        6: "Full House",
        5: "Flush",
        4: "Straight",
        3: "Three of a Kind",
        2: "Two Pair",
        1: "One Pair",
        0: "High Card"
    }
    return hand_names[rank]

def check_hand(hand, is_cpu = False):
    global win, cpu_win

    # maps all the values of the cards to how good they are
    values = []
    suits = []
    value_map = {"A": 14, "K": 13, "Q": 12, "J": 11, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
    
    for card in hand:
        # Extract value (everything except the last character)
        value = card[:-2]
        # Extract suit (anything thats not the last character)
        suit = card[-2:]
        
        values.append(value)
        suits.append(suit)
    # Convert values to a number for easier comparison
    numeric_values = []
    for v in values:
        v = value_map[v]
        numeric_values.append(v)

    # checks if the value is alredy in the count then add one else add that value
    value_counts = {}
    for value in values:
        if value in value_counts:
            value_counts[value] += 1
        else:
            value_counts[value] = 1
    
    # checks if the suit is alredy in the count then add one else add that suit
    suits_count = {}
    for suit in suits:
        if suit in suits_count:
            suits_count[suit] += 1
        else:
            suits_count[suit] = 1
    
    # Check for flush (all cards of the same suit)
    is_flush = False
    for suit, count in suits_count.items():
        if count >= 5:
            is_flush = True


    # check if 5 cards are the same suit, and check if there is a A,K,Q,K,10
    if is_flush and set([14, 13, 12, 11, 10]).issubset(set(numeric_values)):
        hand_rank = 9
        high_card = 14  # Ace high card

    # Store the result
    result = (hand_rank, high_card)
    
    if is_cpu:
        cpu_win = result
    else:
        win = result

check_hand(hand=player_check, is_cpu=False)
check_hand(hand=cpu_check, is_cpu=True)


print("\nGame Over")
print(f"Opponent had {cpu_hand}")

print(f"Your hand: {get_hand_name(win[0])}")
print(f"CPU hand: {get_hand_name(cpu_win[0])}")

# checks win based on if in the result variable if the rank is higher, then if not then checks whose high card is higher 
# for future reference (win[0] = rank, win[1] = high_card)

if win[0] > cpu_win[0]:
    print(f"You Won ${int(bet_amount) * 2}!")
elif win[0] < cpu_win[0]:
    print(f"You Lost ${bet_amount}")
elif win[1] > cpu_win[1]:
    print(f"You Won ${int(bet_amount) * 2} with a higher card!")
elif win[1] < cpu_win[1]:
    print(f"You Lost ${bet_amount} with a lower card")
else:
    print(f"You drew, your ${bet_amount} is refunded")


'''
CURRENTLY DOESNT WORK TO RUN BECAUSE IT DOESNT LIKE THAT ONLY 1 RANK IS DEFINED
'''

'''
NOTE tom wants an elo system
'''