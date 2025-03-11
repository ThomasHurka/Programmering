import random
import time



cardDeck = ["a1","a2","a3","a4","21","22","23","24","31","32","33","34","41","42","43","44",
            "51","52","53","54","61","62","63","64","71","72","73","74","81","82","83","84",
            "91","92","93","94","101","102","103","104","j1","j2","j3","j4","q1","q2","q3",
            "q4","k1","k2","k3","k4"]
playerDeck1 = []
playerDeck2 = []
playerDeck3 = []
playerDecks = [playerDeck1, playerDeck2, playerDeck3]
validCards = ["a", "2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k"]


player2Askchoices = ["p1","p3"]
player3Askchoices = ["p2","p1"]



rank = {
    "a": "Ace", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", 
    "9": "9", "10": "10", "j": "Jack", "q": "Queen", "k": "King"
}
faction = {
    "1": "Spades",
    "2": "Clubs",
    "3": "Diamonds",
    "4": "Hearts"
}


playerTurn = 0 
player1Points = 0
player2Points = 0
player3Points = 0 


def introduction():
    print("Welcome to Go-Fish!")
    time.sleep(0.1)
    print("Shuffling Deck")
    time.sleep(0.2)
    random.shuffle(cardDeck)
    for y in range(3):
        for i in range(7): 
            playerDecks[y].append(cardDeck[0])
            cardDeck.pop(0)
    time.sleep(0.2)
    
def gameFunction(askChoice, askCardchoice):
    global player1Points, player2Points, player3Points, playerTurn, cardDeck
  
    if askChoice == "p2":

        matchCards = [card for card in playerDeck2 if card.startswith(askCardchoice)]
    
        if matchCards:
           for card in matchCards: 
                cardCheck(card)
                playerDeck1.append(card)
                playerDeck2.remove(card)
                playerTurn += 1
        else: 
            if cardDeck: 
                print("Go Fish!")
                playerDeck1.append(cardDeck[0])
                cardDeck.pop(0)
                playerTurn += 1
                print(" ")
    elif askChoice == "p3":

        matchCards = [card for card in playerDeck3 if card.startswith(askCardchoice)]
    
        if matchCards:
           for card in matchCards: 
                cardCheck(card)
                playerDeck1.append(card)
                playerDeck3.remove(card)
                playerTurn += 1
                print(" ")
        else: 
            if cardDeck: 
                print(" ")
                print("Go Fish!")
                playerDeck1.append(cardDeck[0])
                cardDeck.pop(0)
                playerTurn += 1
                
    else:
        print("ERROR")
def AIturn(askChoice, askCardchoice, askingPlayer):
    global player1Points, player2Points, player3Points, playerTurn, cardDeck

    if askingPlayer == "p2":
        if askChoice == "p3":
            print("Player2: I Choose Player3!")

            matchCards = [card for card in playerDeck3 if card.startswith(askCardchoice)]

            time.sleep(2)
            if matchCards:
                for card in matchCards: 
                    AIcardCheck(card)
                    playerDeck2.append(card)
                    playerDeck3.remove(card)
                    print(" ")
            else: 
                if cardDeck: 
                    print(" ")
                    print("Go Fish!")
                
                    playerDeck2.append(cardDeck[0])
                    cardDeck.pop(0)
        elif askChoice == "p1":
            print("Player2: I Choose Player1!")
            matchCards = [card for card in playerDeck1 if card.startswith(askCardchoice)]
            time.sleep(2)
            if matchCards:
                for card in matchCards: 
                    AIcardCheck(card)
                    playerDeck2.append(card)
                    playerDeck1.remove(card)
                    print(" ")
            else: 
                if cardDeck:
                    print(" ") 
                    print("Go Fish!")
                    
                    playerDeck2.append(cardDeck[0])
                    cardDeck.pop(0)
    elif askingPlayer == "p3":
        if askChoice == "p2":
            print("Player3: I Choose Player2!")
            matchCards = [card for card in playerDeck2 if card.startswith(askCardchoice)]
            time.sleep(2)
            if matchCards:
                for card in matchCards: 
                    AIcardCheck(card)
                    playerDeck3.append(card)
                    playerDeck2.remove(card)
                    print(" ")
            else: 
                if cardDeck:
                    print(" ") 
                    print("Go Fish!")
                    
                    playerDeck3.append(cardDeck[0])
                    cardDeck.pop(0)
        elif askChoice == "p1":
            print("Player3: I Choose Player1!")
            matchCards = [card for card in playerDeck1 if card.startswith(askCardchoice)]
            time.sleep(2)
            if matchCards:
                for card in matchCards: 
                    AIcardCheck(card)
                    playerDeck3.append(card)
                    playerDeck1.remove(card)
                    print(" ")
            else: 
                if cardDeck: 
                    print(" ")
                    print("Go Fish!")
                    
                    playerDeck3.append(cardDeck[0])
                    cardDeck.pop(0)
    
def cardCheck(card):
    for key, name in rank.items():
            if card.startswith(key):
                for rankKey, factionName in faction.items():
                    if card.endswith(rankKey):
                        print(f"You took: {name} of {factionName}!")
                    
def AIcardCheck(card):
    if askingPlayer == "p2":
        player = "Player2"
    elif askingPlayer == "p3":
        player = "Player3"
    for key, name in rank.items():
            if card.startswith(key):
                for rankKey, factionName in faction.items():
                    if card.endswith(rankKey):
                        print(f"{player} took: {name} of {factionName}!", end="  ")

def deckCheck(playerDeck1):
    print("Player 2 = p2, Player 3 = p3")
    print("Your Deck: ")
    for card in playerDeck1:
        for key, name in rank.items():
            if card.startswith(key):
                for rankKey, factionName in faction.items():
                    if card.endswith(rankKey):
                        print(f"{name} of {factionName},", end="  ")

  
def fourCards(askCardchoice):
    for askCardchoice.startswith in playerDeck1:
        print()
        
    

    
introduction()
    
    

while True:
    try: 
        if playerTurn == 0: 
            deckCheck(playerDeck1)
            print(" ")
            askChoice = (input("Input the player, you want to ask from: ")).lower()
            askCardchoice = (input("Input the card you want to ask for: ")).lower()


            if askChoice == "p2" or askChoice == "p3": 
                invalidity = True
                for card in playerDeck1:
                    if playerDeck1 is not None: 
                        if card.startswith(askCardchoice):
                            invalidity = False
                            gameFunction(askChoice, askCardchoice)
                            break
                if invalidity:
                    print("Invalid Card, Retry")
            else:
                print("Invalid Player, Retry")
        elif playerTurn == 1: 
            print("Player2 Turn; ")
            time.sleep(2)
            print(" ")
            playerTurn += 1
            askingPlayer = "p2"
            askChoice = random.choice(player2Askchoices)
            cardRandom = random.choice(playerDeck2)
            askCardchoice = cardRandom[0]
            AIturn(askChoice, askCardchoice, askingPlayer)
        elif playerTurn > 1: 
            print("Player3 Turn; ")
            time.sleep(2)
            print(" ")
            playerTurn = 0
            askingPlayer = "p3"
            askChoice = random.choice(player3Askchoices)
            cardRandom = random.choice(playerDeck3)
            askCardchoice = cardRandom[0]
            AIturn(askChoice, askCardchoice, askingPlayer)
    except ValueError:
        print("Value Error")
    except KeyError:
        print("Key Error")
    except KeyboardInterrupt:
        print("Exiting Program")
        break




