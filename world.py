
import turtle
from mario import *
from obstacle import *
import sys

class World:

    def __init__(self, wen, mario, obstacle):

        self.wen = wen
        self.wen.register_shape("bbg.gif")
        self.image = ("bbg.gif")
        self.wen.bgpic(self.image)
        self.mario = mario
        self.obstacle = obstacle
        self.wen.setup(1200,700)
        self.wen.title("The Key is to make Mario Jump on time!!")


    def run(self):
        self.wen.onkey(self.mario.jump, "Up")
        self.wen.onkey(self.wen.bye, "q")
        self.wen.listen()
        self.obstacle.start()

#End of class
