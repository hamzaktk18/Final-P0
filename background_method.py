#Sher Sanginov helped me create this code because the code is beyond the scope of what we learned during the class

#used code example from this web page : http://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html

#####################################################################################################################

import threading
import time

from tkinter import *

class GUIme:
    def __init__(self, master, score):
        self.master = master
        self.score=score
        master.title("If you are reading this, it's too late.!!")

        self.label = Label(master, text="Thank You For Playing Mario with us! Your total score is:"" "+ str(self.score), font = ("Helvetica", 20) )
        self.label.pack()

        self.label = Label(master, text="You can always play 'another one'", font=("Helvetica", 16))
        self.label.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, alex, salem, wn, interval=0.01):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.wn=wn
        self.alex=alex
        self.salem=salem
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        """ Method that runs forever """
        while True:


            if self.alex.mgoal==True and self.salem.goal==True:
                 root = Tk()
                 root.geometry("1500x900")
                 my_gui = GUIme(root, self.alex.counter)
                 root.mainloop()
                 self.wn.bye()


            time.sleep(self.interval)


