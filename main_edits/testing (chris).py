# This is the skeleton for the Riddles GUI
from Tkinter import *
import random
from time import sleep
#import os
DEBUG = False

# question class
class Q(object):
    # inputs the question number and the answer
    def __init__(self, name):
        self.text = {}
        self.text = ""                  # this is the question's text
        self.ans = []
        self.dif = ""
        # all 4 answers are saved in a list with the correct answer listed first        
        #self.dif = ""                   # this is the difficutly rating (from 1-20)
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

    def addQuestions(self, text, dif):
        self._text = text
        self._dif = dif

    # this should eventually return:
    # The question, then four answers in random order
    def __str__(self):
        return "The question is:\n{} \nAnswers: \na: {} \nb: {} \nc: {} \nd: {}".format(\
            self.allQuestions, self.ans[0], self.ans[1], self.ans[2], self.ans[3])


# this is the game function
class Riddles(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

    # creates the  20 questions
    def questions(self):
        global currentQuestion
        self.allQuestions = []
        self.count = 0

        q1 = Q("question1")
        q2 = Q("question2")
        q3 = Q("question3")
        q4 = Q("question4")

        
        q1.addQuestions("How are you?", 0)
        q2.addQuestions("What is the most difficult thing you can think of?", 20)
        q3.addQuestions("Who's on first?", 12)
        q4.addQuestions("The earth is approximately how many miles from the Sun?", 12)
        #######################
        q1.addAnswers("Good", "okay, I guess", "Great", "bleh")
        q2.addAnswers("Rocket Science", "Neurosicence", "Computer Science", "*insert hard job here")
        q3.addAnswers("What's on second","I don't know's on third", "Why's in left field", "Tomorrow's the pitcher")
        q4.addAnswers("9.3 million", "39 million", "93 million", "193 million")

        


        # shuffles questions so they appear in random order
        self.x = self.allQuestions
        random.shuffle(self.x)

        # sets the current question 
        Riddles.currentQuestion = self.x[self.count]



        if DEBUG == True:
            print "current: {}, \n\nall: {}".format(self.currentQuestion, self.allQuestions)



    def iterator(self, event):
        if self.count < len(self.x):
            Riddles.currentQuestion = self.x[self.count]
            Riddles.text = Riddles.currentQuestion
            self.count += 1

        else:
            self.l1.configure(text = "Game Over!\nThanks for playing!")
            self.b1.configure(bg = "#40E0D0", text = "Your score was: ")
            self.b2.configure(bg = "#40E0D0", text = "{} points!".format("12"))
            self.b3.configure(bg = "#40E0D0", text = "To exit, click there -->")
            self.b4.configure(bg = "#40E0D0", text = "Exit", command = window.destroy)

    def greenClick(self):
        if self.count < len(self.x):
            self.b1.configure(bg = "green")
            self.l1.configure(text = "Question: \n{}".format(self.currentQuestion.text))
            
            self.b1.configure(text = "A: {}".format(self.currentQuestion.ans[0]))
            self.b2.configure(text = "B: {}".format(self.currentQuestion.ans[2]))
            self.b3.configure(text = "C: {}".format(self.currentQuestion.ans[1]))
            self.b4.configure(text = "D: {}".format(self.currentQuestion.ans[3]))

        ## LED code will be here
##    def setStatus(self, status):
##        
##        self.l1.configure(text = "Question: \n{}".format(self.currentQuestion.text))
##        self.b1.configure(text = "A: {}".format(self.currentQuestion.ans[0]) )
##        self.b2.configure(text = "B: {}".format(self.currentQuestion.ans[2]))
##        self.b3.configure(text = "C: {}".format(self.currentQuestion.ans[1]))
##        self.b4.configure(text = "D: {}".format(self.currentQuestion.ans[3]))

 
    def setupGUI(self):
        self.l1 = Label(window, text = "Question: \n{}".format(self.currentQuestion.text), anchor = "center", bg = "lightgreen")
        self.l1.grid(row = 0, columnspan = 2)
    
        self.b1 = Button(window, text = "A: {}".format(self.currentQuestion.ans[0]), command = lambda : self.greenClick())
        self.b1.grid(row = 1, column = 0)

        self.b2 = Button(window, text = "B: {}".format(self.currentQuestion.ans[2]))
        self.b2.grid(row = 1, column = 1)

        self.b3 = Button(window, text = "C: {}".format(self.currentQuestion.ans[1]))
        self.b3.grid(row = 2, column = 0)

        self.b4 = Button(window, text = "D: {}".format(self.currentQuestion.ans[3]))
        self.b4.grid(row = 2, column = 1)


##    def delete(self):
##        self.l1.configure(text = "Question: \n{}".format(self.currentQuestion.text))
##        self.b1.configure(text = "A: {}".format(self.currentQuestion.ans[0]))
##        self.b2.configure(text = "B: {}".format(self.currentQuestion.ans[2]))
##        self.b3.configure(text = "C: {}".format(self.currentQuestion.ans[1]))
##        self.b4.configure(text = "D: {}".format(self.currentQuestion.ans[3]))


    #def setStatus(self, status):
   
    def play(self):
        self.questions()
        self.setupGUI()
        
        


###GPIO settings
#import RPi.GPIO as GPIO
#from time import sleep

##setting up the LED and switch pin numbers
wrong = 22
correct = 20
buttons = [12, 16, 24, 26]

## use the Broadcam pin code
#GPIO.setmode(GPIO.BCM)
##set up the LED and switch pins
#GPIO.setup(wrong, GPIO.OUT)
#GPIO.setup(correct, GPIO.OUT)
#GPIO.setup(buttons, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# creates the window

window = Tk()

window.title("How Smart Are You?")

k = Riddles(window)

k.play()
window.bind("<Button-1>", k.iterator)

#

window.mainloop()
