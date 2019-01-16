# button.py by Jack Beal

from graphics import *

class Button:

    """ A button is a labelled Zelle rectangle in a window. Its active state is a bool toggle.
        Using activate() or deactivate() this can be switched.
        isClicked() will return true is the button is active and the clickpoint is inside of the rectangle defining the button.
    """

    def __init__(self, win, lbl, cpt, width, height, active):

        """ Makes a rectangular button wherein <win> is a Zelle window into which to draw, <label> is a string label for the button, <cpt> is a Zelle point object for the central anchor of the button, <width> and <height> are integers specifying the dimensions.
        """

        self.label = Text(cpt, lbl)
        self.active = active
        self.win = win
        self.cpt = cpt

        x,y = self.cpt.getX(), self.cpt.getY()
        self.xMin = x - width / 2
        self.xMax = x + width / 2
        self.yMin = y - height / 2
        self.yMax = y + height / 2

        self.rect = Rectangle(Point(self.xMin, self.yMin), Point(self.xMax, self.yMax))
        self.rect.draw(self.win)
        self.label.draw(win)

        if self.active == True:
            self.activate()
        elif self.active == False:
            self.deactivate()

    def activate(self):

        """ Sets a Button object to state Active by making the text black and makes the outline bolder, then sets flag Active to True
        """
        self.label.setFill("black")
        self.rect.setWidth(2)
        self.rect.setFill("grey")

        self.active = True

    def deactivate(self):
        """Sets this button to 'inactive' . """
        self.label.setFill('darkgray')
        self.rect.setWidth(.5)
        self.active = False


    def isClicked(self, p):
        if self.active == True:
            """Returns true if button active and Point p is inside"""
            if (p.getX() < self.xMax) and (p.getX() > self.xMin) and (p.getY() < self.yMax) and (p.getY() > self.yMin):
                return True
            else:
                return False
        else:
            return False
