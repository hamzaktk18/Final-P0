######################################################################
# Author: Muhammad Hamza khattak, Salem Ben Saad
# Username: khattakm, BenSaadS
# #
# Assignment: P0 : Final Project
# Purpose: Create an interactive game based on Mario and DJ Khaleed's shenanigans.
#
######################################################################
# Acknowledgements:
#  Mr. Scott Heggens
#  TA Rusty Doston
#  TA Will
#  Sher Sanginov (CS department)
####################################################################################

import mario
from world import *
import turtle
from obstacle import *
from background_method import *

def main():


    wn = turtle.Screen()
    wn.register_shape("mario.gif")
    wn.register_shape("khaled.gif")
    alex = mario.Mario(wn)
    salem = Obstacle(wn, mario)

    example = ThreadingExample(alex, salem, wn)
    time.sleep(1)
    earth = World(wn, alex, salem)
    earth.run()

    wn.mainloop()

main()
