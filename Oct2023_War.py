import random

deck = []
player_1_hand = []
player_2_hand = []
total_rounds = 0
game_auto_run = False
suits = ["\u2660", "\u2663", "\u2665", "\u2666"]
card_numbers = [("2",2), ("3",3), ("4",4), ("5",5), ("6",6), ("7",7), ("8",8), ("9",9), ("10",10), ("J",11), ("Q", 12), ("K", 13), ("A", 14)]

#Functions
def add_player_cards_to_deck(cardsToDraw):
    for i in range(cardsToDraw):
        player1Card = player_1_hand.pop(0)
        deck.append(player1Card)

        player2Card = player_2_hand.pop(0)
        deck.append(player2Card)

def display_deck():
    print()
    print("Player 1       Player 2")
    for i in range(0, len(deck), 2):
        print(f"{deck[i]}               {deck[i+1]}")
    print()

def display_score():
    print(f"Player 1 Hand: {len(player_1_hand)} cards | Player 2 Hand: {len(player_2_hand)} cards")
    print("___________________________________________________")

def win_condition():
    if(len(player_1_hand) > 0):
        print(f"Player 1 Won In {total_rounds} Rounds!")
    else:
        print(f"Player 2 Won In {total_rounds} Rounds!")
    quit()

#Generate Starting Hands
class Card:
    def __init__(self, number, suit, value):
        self.number = number
        self.suit = suit
        self.value = value
    
    def __str__(self):
        return f"{self.number}{self.suit}"

for suit in suits:
    for cardNumber in card_numbers:
        deck.append(Card(cardNumber[0], suit, cardNumber[1]))

random.shuffle(deck)

while len(deck) > 0:
    player_1_hand.append(deck.pop())
    player_2_hand.append(deck.pop())

#Game Setup
print("Enter 'y' to let the game run itself to the end. Otherwise, enter.")
user_input = input()
if user_input == "y":
    game_auto_run = True

#Play War
while len(player_1_hand) > 0 and len(player_2_hand) > 0:
    if not game_auto_run:
        input("Press Enter to Draw Cards")
    add_player_cards_to_deck(1)
    player_1_card = deck[len(deck) - 2]
    player_2_card = deck[len(deck) - 1]
    display_deck()

    if player_1_card.value == player_2_card.value:
        print("War!")
        if not game_auto_run:
            input("Press Enter to Declare War")
        if len(player_1_hand) < 4:
            player_1_hand.clear()
            print("Player 1 Did Not Have Enough Cards To Commit War")
            win_condition()
        elif len(player_2_hand) < 4:
            player_2_hand.clear()
            print("Player 2 Did Not Have Enough Cards To Commit War")
            win_condition()
        add_player_cards_to_deck(3)
        display_deck()
    else:
        random.shuffle(deck)
        if player_1_card.value > player_2_card.value:
            print("Player 1 Won This Hand")
            player_1_hand.extend(deck)
        else:
            print("Player 2 Won This Hand")
            player_2_hand.extend(deck)
        display_score()
        deck.clear()
    total_rounds += 1
win_condition()