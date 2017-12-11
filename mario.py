import turtle
from time import *

class Mario:

    def __init__(self, wn, height=50, width=50):
        self.wn = wn
        self.sprite = turtle.Turtle()
        self.sprite.shape("mario.gif")
        self.height = height
        self.width = width
        self.counter = 0
        self.sprite.penup()
        self.position = self.sprite.setposition(-300,-257)
        self.sprite.left(90)
        self.mgoal=True

    def jump(self):
        self.sprite.forward(50)
        self.mgoal=False
        self.sprite.forward(210)
        self.sprite.forward(-210)
        self.mgoal=True
        self.sprite.forward(-50)
        self.counter += 1


    def left(self):
        self.sprite.left(90)

#End of class
