# This is the skeleton for the Riddles GUI

from Tkinter import *

DEBUG = True

# question class
class Q(object):
    # inputs the question number and the answer
    def __init__(self, text, dif):
        self.text = text                # this is the question's text
        self.ans = []                   # all 4 answers are saved in a list with the correct answer listed first
        self.dif = dif                  # this is the difficutly rating (from 1-20)
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
    
    @property
    def ans(self):
        return self._ans
    
    @ans.setter
    def ans(self, value):
        self._ans = value
    
    def addAnswers(self, a, b, c, d):
        self.ans = [a, b, c, d]
        if DEBUG == True:
            print self._ans

    # this should eventually return:
    # The question, then four answers in random order
    def __str__(self):
        return "The question is:\n{} \nAnswers: \na: {} \nb: {} \nc: {} \nd: {}".format(\
            self.text, self.ans[0], self.ans[1], self.ans[2], self.ans[3])


class Riddles(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

    ### creates the  20 questions
    def questions(self):
        q1 = Q("How are you?", 0)
        q2 = Q("What is the most difficult thing you can think of", 20)
        #######################
        q1.addAnswers("Good", "okay, I guess", "Great", "bleh")
        q2.addAnswers("Rocket Science", "Neurosicence", "Computer Science", "*insert hard job here")
        
        print q1
        if DEBUG == True:
            print "Difficulty: {}".format(q1.dif)
    
    def setScore(self, score):
        # should display the score to the GUI
        pass

    def setupGUI(self):
        self.pack(fill=BOTH, expand=1)
        Riddles.player_input = Entry(self, bg="white")
        Riddles.player_input.bind("<Return>", self.process)
        Riddles.player_input.pack(side=BOTTOM, fill=X)
        Riddles.player_input.focus()

        img = None 
        Riddles.image = Label(self, width=WIDTH / 2, image = img)
        Riddles.image.image = img
        Riddles.image.pack(side=LEFT, fill=Y)
        Riddles.image.pack_propagate(False)

        text_frame = Frame(self, width=WIDTH / 2)
        Riddles.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Riddles.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)
    
    # function to check wheter the question is right or wrong
    def answer(self, answer):
        if answer == self.answers[0]:
            print "You got it right!"
        else:
            print "Sorry, that's wrong"
        # function that adds one point to the player's score if they don't get the question wrong
            # we could make each question worth the number of difficulty it is

    def play(self):
        self.questions()
        self.setupGUI()
        # self.setScore()   # not finished yet

    def process(self, event):
        action = Riddles.player_input.get()
        action = action.lower()
        response = "That isn't a valid response"

        if (action == "quit" or action == "exit" or action == "bye" or action == "sionara!"):
            exit(0)

        words = action.split()
        if DEBUG == True:
            print words

# creates the window
WIDTH = 500
HEIGHT = 400

window = Tk()
window.title("How Smart Are You?")

k = Riddles(window)

k.play()

window.mainloop()
