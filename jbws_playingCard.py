# playingCard.py by Jack Beal

from random import randrange
from graphics import *

class PlayingCard:
    """ Playing card objects have two attributes, Suit and Rank, both of which have accessor methods, .getSuit() and .getRank(). The object may be converted into a string, which returns e.g. "Four of hearts" or "Jack of spades"
    """

    def __init__(self, rank, suit, faceup=True):
        # rank is an int in range 1–13 for ranks Ace–King
        # suit is a single character “d”, “c”, “h”, or “s”
        self.suit = suit
        self.rank = rank
        self.faceup = faceup

    def getRank(self): # Returns the rank of the card.
        return self.rank

    def getSuit(self): # Returns the suit of the card.
        return self.suit

    def getFace(self): # For those times when you're wondering if a card really is face-up
        return self.faceup

    def setFace(self, state): # Sets faceup flag
        self.faceup == state

    def __str__(self): # Returns the name of the card
        nameDict = {1:'Ace', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Eleven', 11:'Jack', 12:'Queen', 13:'King'}
        suitDict = {'d':'diamonds', 'c':'clubs', 'h':'hearts', 's':'spades'}
        return str(nameDict[self.rank] + ' of ' + suitDict[self.suit])

    def drawCard(self, win, anchor, faceup=False): # Draw a card at a point object <anchor>
        #creates an image object from the file by concatenating the above variables
        self.faceup = faceup
        if self.faceup == False:
            im = Image(anchor, "playingcards/" + self.suit + str(self.rank) + ".gif")
        elif self.faceup == True:
            color = randrange(1,3)
            im = Image(anchor, "playingcards/b" + str(color) + "fv.gif")
        im.draw(win)

