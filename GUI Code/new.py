# This is the skeleton for the game GUI

from Tkinter import *

DEBUG = False

# question class
class Q(object):
    # inputs the question number and the answer
    def __init__(self, number, text):
        self.number = number
        self.text = text
        self.question = {}
        self.answers = {}
        if DEBUG == True:
            print "number: {}, text: {}".format(number, text)
    
    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self, value):
        self._number = value

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, string):
        self._text = string
    
    @property
    def question(self):
        return self._question
    
    @question.setter
    def question(self, string):
        self._question = string

    def addAnswers(self, number, dict):
        pass

    # this should eventually return:
    # The question then four answers in random order
    def __str__(self):
        return "Question {} is:\n{}".format(self.number, self.text)



q1 = Q(0, "How are you?")

print q1
