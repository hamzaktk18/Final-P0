#The threading concept was contributed by Mr. Scott Heggen
# and he helped write the code to make sure both turtles are independent of each other to better help find the collision point



######################################################################################

import turtle
import time
import threading
from mario import *

class Obstacle(threading.Thread):

    def __init__(self, wn, mario, h = 1 , w = 20, position = (0,0)):
        threading.Thread.__init__(self)
        self.wn = wn
        self.ting = turtle.Turtle()
        self.ting.shape("khaled.gif")
        self.height = h
        self.width = w
        self.ting.penup()
        self.position = self.ting.setpos(30,-250)
        self.goal=None

    def get_goal(self):
        print(self.goal)

    def run(self):
        self.ting.speed(2)

        for i in range(1000000):
           self.ting.speed(2)
           self.ting.forward(-330)
           self.goal=True
           self.ting.forward(-1)
           self.goal=False
           self.ting.forward(-369)
           if int(self.ting.position()[0]) == -670:
               self.ting.forward(369.6)
               self.goal=True
               self.ting.forward(0.4)
               self.goal=False
               self.ting.forward(330)

#End of class
