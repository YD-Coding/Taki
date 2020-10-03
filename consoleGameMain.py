import random

class Card():
    def __init__(self, number, color):
        self.number = number
        self.color = color
        self.usage = None

USAGES = ["changeColor", "changeDirection", "+2", "stop", "plus", "taki", "superTaki"]    
COLORS = ["yellow", "blue", "red", "green"]
NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

class SpecialCard(Card):
    
    def __init__(self, color, usage):
        super().__init__(self, color) # check about the self... no need of color for the special cards...

        self.usage = usage

        if self.usage == "changeColor" or self.usage == "superTaki":
            self.color == None
        else:
            self.color = color # not working for some reason...



    
        

class Game:
    def __init__(self):
        self.turn = 0
        self.playercount = 0
        self.players = [] 
        self.currentCard = None

    def add_player(self, player):
        self.playercount += 1
        self.players.append(player)
    
    """def run(self):
        self.players(self.turn)"""

    def divideCards(self):
        for player in self.players:
            for _ in range(8):
                if random.randint(1, 4) == 1:
                    usage = random.choice(USAGES)
                    player.hand.append(SpecialCard(usage = usage, color = random.choice(COLORS)))
                else:    
                    player.hand.append(Card(number = random.randint(1, 10), color = random.choice(COLORS)))



    
class Player:
    def __init__(self, name):
        self.name = name
        self.turn = None
        self.hand = []
    
    def isCardMatch(self, game : Game):           
        cardToPut = self.isCardInHand()        
        while cardToPut.color != game.currentCard.color and cardToPut.color != None and cardToPut.number != game.currentCard.number:
            print("you can't put that card it's not the same color!")
            cardToPut = self.isCardInHand()
        return cardToPut


    def isCardInHand(self):
        cardToPut = input("choose card to put - ")
        cardToPut = Card(cardToPut.split()[0], cardToPut.split()[1])  
        while cardToPut not in self.hand:
            print("no such card as " + cardToPut + " in your hand!")
            cardToPut = input("choose card to put - ")
            cardToPut = Card(int(cardToPut.split()[0]), cardToPut.split()[1])
        return cardToPut
        
    
    def putCard(self):
        card = self.isCardMatch(game)
        self.hand.remove(card)
        game.currentCard = card


    def turnBeginning(self):
        while True:
            whatToDo = input("what do you want to do? ")
            if whatToDo == "t" or whatToDo == "T":
                self.takeCard()
                break
            elif whatToDo == "p" or whatToDo == "P":
                self.putCard()
                break
            else:
                print("please choose 'p' or 'P' for putting card and 't' or 'T' for taking card")

    def takeCard(self):
        return None


            

dan = Player('Dan')
yarin = Player('Yarin')


game = Game()
game.players.append(dan)
game.players.append(yarin)
game.divideCards()

print("dan's hand: ")
for card in dan.hand:
    if card.usage != None:
        print(str(card.usage) + " " + str(card.color))
    else:
        print(str(card.number) + " " + str(card.color))

print("\n\nyarin's hand: ")
for card in yarin.hand:
    if card.usage != None:
        print(str(card.usage) + " " + str(card.color))
    else:
        print(str(card.number) + " " + str(card.color))

    