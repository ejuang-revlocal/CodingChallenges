import random

deck = []
player1Hand = []
player2Hand = []
totalRounds = 0
gameAutoRun = False
suits = ["\u2660", "\u2663", "\u2665", "\u2666"]
cardNumbers = [("2",2), ("3",3), ("4",4), ("5",5), ("6",6), ("7",7), ("8",8), ("9",9), ("10",10), ("J",11), ("Q", 12), ("K", 13), ("A", 14)]

#Functions
def addPlayerCardsToDeck(cardsToDraw):
    for i in range(cardsToDraw):
        player1Card = player1Hand.pop(0)
        deck.append(player1Card)

        player2Card = player2Hand.pop(0)
        deck.append(player2Card)

def displayDeck():
    print()
    print("Player 1       Player 2")
    for i in range(0, len(deck), 2):
        print(f"{deck[i]}               {deck[i+1]}")
    print()

def displayScore():
    print(f"Player 1 Hand: {len(player1Hand)} cards | Player 2 Hand: {len(player2Hand)} cards")
    print("___________________________________________________")

def winCondition():
    if(len(player1Hand) > 0):
        print(f"Player 1 Won In {totalRounds} Rounds!")
    else:
        print(f"Player 2 Won In {totalRounds} Rounds!")
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
    for cardNumber in cardNumbers:
        deck.append(Card(cardNumber[0], suit, cardNumber[1]))

random.shuffle(deck)

while len(deck) > 0:
    player1Hand.append(deck.pop())
    player2Hand.append(deck.pop())

#Game Setup
print("Enter 'y' to let the game run itself to the end. Otherwise, enter.")
userInput = input()
if userInput == "y":
    gameAutoRun = True

#Play War
while len(player1Hand) > 0 and len(player2Hand) > 0:
    if not gameAutoRun:
        input("Press Enter to Draw Cards")
    addPlayerCardsToDeck(1)
    player1Card = deck[len(deck) - 2]
    player2Card = deck[len(deck) - 1]
    displayDeck()

    if player1Card.value == player2Card.value:
        print("War!")
        if not gameAutoRun:
            input("Press Enter to Declare War")
        if len(player1Hand) < 4:
            player1Hand.clear()
            print("Player 1 Did Not Have Enough Cards To Commit War")
            winCondition()
        elif len(player2Hand) < 4:
            player2Hand.clear()
            print("Player 2 Did Not Have Enough Cards To Commit War")
            winCondition()
        addPlayerCardsToDeck(3)
        displayDeck()
    else:
        random.shuffle(deck)
        if player1Card.value > player2Card.value:
            print("Player 1 Won This Hand")
            player1Hand.extend(deck)
        else:
            print("Player 2 Won This Hand")
            player2Hand.extend(deck)
        displayScore()
        deck.clear()
    totalRounds += 1
winCondition()