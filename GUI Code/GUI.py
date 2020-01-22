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

    ### creates the  20 questions
    def questions(self):
        q1 = Q("How are you?", 0)
        q2 = Q("What is the most difficult thing you can think of", 20)
        q3 = Q("Who's on first", 12)
        #######################
        q1.addAnswers("Good", "okay, I guess", "Great", "bleh")
        q2.addAnswers("Rocket Science", "Neurosicence", "Computer Science", "*insert hard job here")
        q3.addAnswers("What's on second","I don't know's on third", "Why's in left field", "Tomorrow's the pitcher")
        
        print q1
        if DEBUG == True:
            print "Difficulty: {}".format(q1.dif)
    
    # note: this isn't working yet, the "else:" keeps returning an error
    # def setStatus(self, score):
    #     # should display the status to the GUI
    #     Riddles.text.config(state = NORMAL)
    #     Riddles.text.delete("1.0", END)
    #     # if the player gets the question wrong
    #     if (Q.text == None):
    #         Riddles.text.insert(END, "GAME OVER\n\nYou scored {} points".fomat(Riddles.points)
    #     else:
    #         # display the status
    #         Riddles.text.insert(END, "\n you have" + Riddles.points + "points.")

    def setupGUI(self):
        l1 = Label(window, text = "Question: \n{}".format("Who's on first"), anchor = "center")
        l1.grid(row = 0, columnspan = 2)

        l2 = Label(window, text = "A: {}".format("What's on second"))
        l2.grid(row = 1, column = 0)

        l3 = Label(window, text = "B: {}".format("I don't know's on third"))
        l3.grid(row = 2, column = 0)

        l4 = Label(window, text = "C: {}".format("Why's in left field"))
        l4.grid(row = 1, column = 1)

        l5 = Label(window, text = "D: {}".format("Tomorrow is the pitcher"))
        l5.grid(row = 2, column = 1)

    
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
        # self.setStatus()   # not finished yet

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
