# This is the skeleton for the Riddles GUI
from Tkinter import *
import random
DEBUG = False
# question class
class Q(object):
    # inputs the question number and the answer
    def __init__(self, text, dif):
        self.text = text                # this is the question's text
        self.ans = []                   # all 4 answers are saved in a list with the correct answer listed first
        self.dif = dif                  # this is the difficutly rating (from 1-20)
        k.allQuestions.append(self)

        if DEBUG == True:
            print "text: {}, dif: {}".format(self.text, self.dif)


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


# this is the game function
class Riddles(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.allQuestions = []

    # creates the  20 questions
    def questions(self):
        q1 = Q("How are you?", 0)
        q2 = Q("What is the most difficult thing you can think of?", 20)
        q3 = Q("Who's on first?", 12)
        q4 = Q("The earth is approximately how many miles from the Sun?", 12)
        #######################
        q1.addAnswers("Good", "okay, I guess", "Great", "bleh")
        q2.addAnswers("Rocket Science", "Neurosicence", "Computer Science", "*insert hard job here")
        q3.addAnswers("What's on second","I don't know's on third", "Why's in left field", "Tomorrow's the pitcher")
        q4.addAnswers("9.3 million", "39 million", "93 million", "193 million")


        # shuffles questions so they appear in random order
        random.shuffle(self.allQuestions)
        # sets the current question to the first 
        self.currentQuestion = self.allQuestions[0]
        
        if DEBUG == True:
            print "current: {}, \n\nall: {}".format(self.currentQuestion, self.allQuestions)
                            
    def setupGUI(self):
        self.l1 = Label(window, text = "Question: \n{}".format(self.currentQuestion.text), anchor = "center")
        self.l1.grid(row = 0, columnspan = 2)

        self.l2 = Label(window, text = "A: {}".format(self.currentQuestion.ans[0]))
        self.l2.grid(row = 1, column = 0)

        self.l4 = Label(window, text = "B: {}".format(self.currentQuestion.ans[2]))
        self.l4.grid(row = 1, column = 1)

        self.l3 = Label(window, text = "C: {}".format(self.currentQuestion.ans[1]))
        self.l3.grid(row = 2, column = 0)

        self.l5 = Label(window, text = "D: {}".format(self.currentQuestion.ans[3]))
        self.l5.grid(row = 2, column = 1)

    
    # function to check wheter the question is right or wrong
    def answer(self, answer):
        if answer == self.answers[0]:
            print "You got it right!"
            poinnts += Q.dif
        else:
            print "Sorry, that's wrong"
        # function that adds one point to the player's score if they don't get the question wrong
            # we could make each question worth the number of difficulty it is

    def play(self):
        self.questions()
        self.setupGUI()

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

window = Tk()

window.title("How Smart Are You?")

k = Riddles(window)

k.play()

window.mainloop()
