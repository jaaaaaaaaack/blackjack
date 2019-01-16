# Walter Stuart and Jack Beal, 2015
# Blackjack

from graphics import *
from jbws_playingCard import PlayingCard
from jbws_button import Button
import random

"""Attributes of this Blackjack class are as follows.

       INSTANCE VARIABLES

        dealerHand: a list of PlayingCard objects representing the dealer's hand
        playerHand: a list of PlayingCard objects representing the player's hand
        playingDeck: a Deck object representing the deck of cards the game is being played with
"""

class Blackjack:
    def __init__(self, dealerHand, playerHand, playingDeck):
        self.dhand = dealerHand # Will be a list
        self.phand = playerHand # Will be a list
        self.deck = playingDeck # Will be a deck object

        self.deck.shuffle()


    def firstDeal(self, gwin, dPt, pPt): # dPt and pPt are the Points for the first cards to draw
        # Deal the first 2 cards for each player
        for hand in [self.phand, self.dhand]:
            newCard1 = self.deck.dealCard()
            newCard2 = self.deck.dealCard()
            hand.append(newCard1)
            hand.append(newCard2)


    def hit(self, gwin, deck, destHand, anchor): # Adds a new card to a hand and puts it onscreen
        # Note that when hit is called, the anchor must be provided from the list of point objects in the main method
        self.gwin = gwin
        self.deck = deck
        self.anchor = anchor # self.anchor is now a Point object
        self.hand = destHand
        self.hand.append(self.deck.dealCard())
        self.hand[-1].drawCard(self.gwin, self.anchor)


    def evaluateHand(self, hand):
        if hand == self.phand:
            self.pflag = 0
        elif hand == self.dhand:
            self.pflag = 1

        handTotal = 0
        numAces = 0

        # Ace checking
        for item in hand:
            if item.getRank() == 1:
                numAces += 1

            # Face card checking
            currentRank = item.getRank()
            if item.getRank() >= 11:
                currentRank = 10

            if handTotal <= 10:
                if item.getRank() == 1:
                    currentRank = 11

            handTotal += currentRank

            if handTotal > 21:
                while numAces > 0:
                    handTotal -= 10
                    numAces -= 1

        return handTotal


    def dealerPlays(self, gwin, xposList, dcp, ypos):
        """dealer deals cards to herself, stopping when hitting "soft 17"
        """
        self.gwin = gwin
        self.dcp = dcp # int
        self.ypos = ypos # int
        self.xposList = xposList # list

        # Evaluate the hand each time to make sure it's under 17
        while self.evaluateHand(self.dhand) <= 17:
            # Make an anchor point for the next card to draw
            self.anchor = Point(self.xposList[self.dcp], self.ypos)
            # Hit once
            self.hit(self.gwin, self.deck, self.dhand, self.anchor)
            self.dcp += 1

