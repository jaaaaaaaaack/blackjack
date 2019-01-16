from jbws_playingCard import *
from random import *


class Deck:
    """A deck object contains a list of card objects (assumes 52 of them) and provides methods for dealing a card out, shuffling the deck, and returning a list of remaining cards.
    """

    def __init__(self):
        self.cardList = Deck.Constructor()

    def Constructor():
        cardList = []
        for i in ["c","d","s","h"]:
            for j in range(1,14):
                cardList.append(PlayingCard(j,i))
        return cardList

    def shuffle(self): # Randomizes the positions of cards in a Deck object's cardlist
        self.newList = self.cardList
        for i in range(0, len(self.newList)):
            c = self.newList[i]
            r = self.newList[int(random()*52)]
            c, r = r, c

        self.cardList = self.newList


    def retList(self):
        return self.cardList

    def dealCard(self): # Deals the top (last) card from the deck and returns the card object
        return self.cardList.pop(randrange(0,len(self.cardList)))
