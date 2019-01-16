# Walter Stuart and Jack Beal, 2015
# Blackjack control script

from jbws_graphics import *
from jbws_button import *
from jbws_playingCard import *
from jbws_deck import Deck
from jbws_blackjack import Blackjack

from random import *
from time import sleep

def playAgain(win): # Allows repeated play by restarting the main method
    win.close()
    main()

def main():

    # Establish the window
    win = GraphWin("BlackJack",800,600)
    win.setBackground(color_rgb(0,125,0))

    # Load the title and background images
    titleIm = Image(Point(400,300),"title.gif")
    bgIm = Image(Point(400,300), "background.gif")
    # Draw the title
    titleIm.draw(win)

    """ To significantly speed up testing across multiple plays, disable titleIm.draw(win) in line 23, and titleIm.undraw() in line 32.
    """

    # Wait
    win.getMouse()

    # Swap the title for the background and continue
    bgIm.draw(win)
    titleIm.undraw()

    # Get some text objects ready; these display the player's score
    Result = Text(Point(400,200),"")
    Result.setFill("white")
    Result.setStyle("bold")
    Result.setSize(16)
    Result.draw(win)

    scoreCard = Text(Point(75,350),"Player Score:")
    scoreCard.setFill("white")
    scoreCard.setSize(16)
    scoreCard.draw(win)

    playerScore = Text(Point(135,350),"")
    playerScore.setFill("white")
    playerScore.setSize(16)
    playerScore.draw(win)


    # Store all of the information for the buttons in one easy-to-access place
    hitBtPoint, hitBtW, hitBtH = Point(300,275), 100, 50
    standBtPoint, standBtW, standBtH = Point(500,275), 100, 50
    playBtPoint, playBtW, playBtH = Point(400,525), 100, 50
    quitBtPoint, quitBtW, quitBtH = Point(741,50), 50, 35

    # Make the buttons
    Hit = Button(win, "Hit", hitBtPoint, hitBtW, hitBtH, True)
    Stand = Button(win, "Stand", standBtPoint, standBtW, standBtH, True)
    PlayAgain = Button(win, "Play Again", playBtPoint, playBtW, playBtH, True)
    Quit = Button(win, "Quit", quitBtPoint, quitBtW, quitBtH, True)

    # Make a deck object
    deck = Deck()

    # Make two lists, playerHand and dealerHand
    playerHand, dealerHand = [], []

    # Set up the placement of the first two cards for each player
    playerFirstCardPoint = Point(100,450)
    dealerFirstCardPoint = Point(100,100)

    # Make the blackjack object
    game = Blackjack(dealerHand, playerHand, deck)

    # Perform the first deal
    game.firstDeal(win, playerFirstCardPoint, dealerFirstCardPoint)

    # Play starts, set the condition to Ongoing
    gameOverCond = 0

    # Generate the list of integers called xposList
    xposList = [100]
    for i in range(7):
        xposList.append(xposList[i] + 86) # 71px card width + 15px gutter

    # Keep track of where to start in the list
    pcp = 2
    dcp = 2
    for item in xposList: # Shifts the positions over to account for two initial cards
        item += 172

    # Draw out the first two cards
    count = 0
    for item in playerHand:
        item.drawCard(win, Point(xposList[count], 425), False)
        count += 1

    dealerHand[0].drawCard(win, Point(xposList[0], 100), True)
    dealerHand[1].drawCard(win, Point(xposList[1], 100))

    # Check the hands' scores right away
    presult, dresult = game.evaluateHand(playerHand), game.evaluateHand(dealerHand)

    # Display the starting score
    playerScore.setText(presult)

    # The game might be over — here's what happens next
    if presult == 21 and dresult == 21:
        gameOverCond = 6 # Hands tie at 21
        Result.setText("The hands are tied!")
        print("Player and dealer both dealt 21") # Debug
    elif presult == 21:
        Result.setText("Blackjack! You win!")
        gameOverCond = 2 # Player dealt 21
    elif dresult == 21:
        Result.setText("The dealer was dealt 21. Your loss...")
        gameOverCond = 7 # Dealer dealt 21


    # Table of game-ending conditions
    endGame = {
        0:"Game ongoing",
        1:"You busted...",
        2:"Your hand totals 21! You win!",
        3:"The dealer wins with the better hand...",
        4:"You win with the better hand!",
        5:"Both hands are tied!",
        6:"Both hands are tied at 21!",
        7:"The dealer was dealt 21...",
        8:"The dealer busted!",
        98:"Player chose to restart game",
        99:"Player chose to quit. Thanks for playing!",
    }

    # Or the game might not be over, in which case, do all of this:
    while gameOverCond == 0: # 0 is game ongoing

    # Start looping for button clicks
        pt = win.getMouse()


        if Hit.isClicked(pt):
            # Do the hit thing
            game.hit(win, deck, playerHand, Point(xposList[pcp],425))
            # Update score display
            result = game.evaluateHand(playerHand)

            # Check to see if the game ends
            if result > 21:
                playerScore.setText(result)
                Result.setText(endGame[1])
                gameOverCond = 1 # Player busts

            elif result == 21:
                playerScore.setText(result)
                Result.setText(endGame[2])
                gameOverCond = 2 # Player dealt 21

            elif result < 21:
                playerScore.setText(result)
                gameOverCond = 0 # Play continues

            pcp += 1 # Increment to the next-card slot in the player's hand


        elif Stand.isClicked(pt):
            # Do that stand thing
            Hit.deactivate() # Play passes to the dealer, so Hitting is useless
            game.dealerPlays(win, xposList, dcp, 100) # Simulates the dealer's turn

            # Scorekeeping
            dealerTotal = game.evaluateHand(dealerHand)
            playerTotal = game.evaluateHand(playerHand)

            # Check to see if the game is over
            if dealerTotal > 21:
                Result.setText(endGame[8])
                gameOverCond = 8 # Dealer busts
            else:
                if dealerTotal > playerTotal:
                    Result.setText(endGame[3])
                    gameOverCond = 3 # Dealer wins with better hand
                elif dealerTotal < playerTotal:
                    Result.setText(endGame[4])
                    gameOverCond = 4 # Player wins with better hand
                elif dealerTotal == playerTotal:
                    Result.setText(endGame[5])
                    gameOverCond = 5 # Hands tie

        elif PlayAgain.isClicked(pt):
            # Play again
            playAgain(win)

        elif Quit.isClicked(pt):
            # Quit the things
            gameOverCond = 99

    # Flip the dealer's card
    dealerHand[0].drawCard(win, Point(xposList[0],100), False)

    # Stop the useless buttons from deactivating
    Hit.deactivate()
    Stand.deactivate()

    # Game is over, check for the two functioning buttons
    # The second loop is because the game does not necessaily only end when Quit is clicked
    while gameOverCond < 90:

        pt = win.getMouse()
        if PlayAgain.isClicked(pt):
            # Play again
            playAgain(win)

        elif Quit.isClicked(pt):
            # Quit the things
            gameOverCond = 99


    win.close()

main()
