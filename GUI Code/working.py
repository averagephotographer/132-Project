# This is the skeleton for the game GUI

from Tkinter import *

DEBUG = False

# question class
class Q(object):
    # inputs the question number and the answer
    def __init__(self, text, dif):
        self.text = text # this is the question's text
        self.ans = [] # all 4 answers are saved in a list with the correct answer listed first
        self.dif = dif # this is the difficutly rating (from 1-20)
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



q1 = Q("How are you?", 0)
q1.addAnswers("Good", "okay, I guess", "GREAT!", "bleh")


print q1
if DEBUG == True:
    print "Difficulty: {}".format(q1.dif)