# This is the skeleton for the game GUI

from Tkinter import *

DEBUG = True

# question class
class Q(object):
    # inputs the question number and the answer
    def __init__(self, text, dif):
        self.text = text                    # this is the question's text
        self.ans = []                       # all 4 answers are saved in a list with the correct answer listed first
        self.dif = dif                      # this is the difficutly rating (from 1-20)
        if DEBUG == True:
            print "text: {}, dif: {}".format(text, dif)
    
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, string):
        self._text = string
    
    @property
    def dif(self):
        return self._dif
    
    @dif.setter
    def dif(self, value):
        self._dif = value

    def addAnswers(self, a, b, c, d):
        self._ans = [a, b, c, d]
        if DEBUG == True:
            print self._ans

    # this should eventually return:
    # The question then four answers in random order
    def __str__(self):
        return "The question is:\n{} \nAnswers: \na: {} \nb: {} \nc: {} \nd: {}".format(self._text, self._ans[0], self._ans[1], self._ans[2], self._ans[3])


class Game(Frame):
    def makeQuestions(self):
        
        q1 = Q("How are you?", 0)
        q2 = Q("What is the most difficult thing you can think of", 20)






        q1.addAnswers("Good", "okay, I guess", "GREAT!", "bleh")

        q2.addAnswers("Rocket Science", "Neurosicence", "Computer Science", "*insert hard job here")

        print q1
        if DEBUG == True:
            print "Difficulty: {}".format(q1.dif)

    def setupGUI(self):
        # organize the GUI
        self.pack(fill=BOTH, expand=1)

        # setup the player input at the bottom of the GUI
        # the widget is a Tkinter Entry
        # set its background to white and bind teh return key to the
        # function process in the class
        # push it to the bottom of the GUI and let it fill 
        # horozontally
        # give it focus so teh player doesn't have to click on it
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()

        # setup the image to the left of the GUI
        # the widget is a Tkinter Label
        # don't let teh image control the widget's size
        img = None 
        Game.image = Label(self, width=WIDTH / 2, image = img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)

        # setup the text to teh right of the GUI
        # first, the frame in which the text will be placed
        text_frame = Frame(self, width=WIDTH / 2)
        # the widget is a Tkinter TExt
        # disable it by defualt
        # don't let the widget control the frame's size
        Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)

    
    def setScore(self, score):
            # enable the text widget, clear it, set it, and disabled it
            Game.text.config(state = NORMAL)
            Game.text.delete("1.0", END)


    # function to check whether the question is right or wrong
    def answer(self, answer):
        if answer == self.answers[0]:
            print "You got it right!"
        else:
            print "Sorry, that's wrong"
        # function that adds one point to the player's score if they don't get the question wrong
            # we could make each question worth the number of difficulty it is

    def play(self):
        self.makeQuestions()
        self.setupGUI()
        self.setScore()

    def process(self, event):
        # grab the player's input from the input at the bottom of the GUI
        action = Game.player_input.get()
        # set the user's input to lowercase to make it easier to compare the verb and noun to known values
        action = action.lower()
        # set a defualt response
        response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"

        # exit the game if the palyer wants to leave (supports quit, exit, and bye)
        if (action == "quit" or action == "exit" or action == "bye" or action == "sionara!"):
            exit(0)

        # splits the user input into words (words are separated by spaces) and store the words in a list
        words = action.split()
        if DEBUG == True:
            print words

        

           
WIDTH = 800
HEIGHT = 600

window = Tk()
window.title("Questionaire")

# create the GUI as a Tkinter canvas inside teh window
g = Game(window)

# play the game
g.play()

# wait for the window to close
window.mainloop()
