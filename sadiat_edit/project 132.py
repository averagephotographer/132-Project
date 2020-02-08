from Tkinter import *
import random
from time import sleep

class Q(object):
    def __init__(self, name):
        self.text = {} ##stores the questions and correct answer in a dictionary
        self.answers = [] ### contains the options including the correct answer



    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, string):
        self._text = string

    @property
    def answers(self):
        return self._answers

    @answers.setter
    def answers(self, string):
        self._answers = string

    
    def addquestions(self, question, correct): ##adds the question as the key and the correct answer as the data value in the dictionary
        self._text[question] = correct
        self._answers.append(correct) ## adds the correct answer into the self.answers list

    def addoptions(self, a,b,c): ##adds the wrong answers to a list ##adds the wrong answers into the self.answers list
        self._answers.append(a)
        self._answers.append(b)
        self._answers.append(c)

    def shuffle(self):
        random.shuffle(self.answers) ## function that shuffles the answers


    def __str__(self):
        pass

    #this is the game function
class Riddles(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

    ## creates the 20 questions
    def questions(self):
        global currentQuestion
        self.count = 0

        q1 = Q("question1")
        q2 = Q("question2")
        q3 = Q("question3")

        q1.addquestions("How are you?", "good") ## calls the add questions function
        q2.addquestions("who's on first?", "me")
        q3.addquestions("difficult job?", "computer science")

        q1.addoptions("bleh", "okay", "not good" )## calls the add options function
        
        q1.shuffle() ## calls the shuffle function
        
        q2.addoptions("you", "andres", "chris")
        
        q2.shuffle()
        
        q3.addoptions("biology", "physics", "child education" )
        
        q3.shuffle()


        self.currentQuestion = q1


    def iterator(self, event): ## iono how to iterate it 
        pass

    def setupGUI(self):
        self.l1 = Label(window, text = "Question: \n{}".format(self.currentQuestion.text.keys()), anchor = "center", bg = "lightblue")##sets each question as a \
        #label by calling its key from the dictionary.if it is confusing you can check the lectures on "more on data" on moodle.
        self.l1.grid(row = 0, columnspan = 2)

        self.b1 = Button(window, text = "A: {}".format(self.currentQuestion.answers[0]))
        self.b1.grid(row = 1, column = 0)

        self.b2 = Button(window, text = "B: {}".format(self.currentQuestion.answers[1]))
        self.b2.grid(row = 1, column = 1)

        self.b3 = Button(window, text = "C: {}".format(self.currentQuestion.answers[2]))
        self.b3.grid(row = 2, column = 0)

        self.b4 = Button(window, text = "D: {}".format(self.currentQuestion.answers[3]))
        self.b4.grid(row = 2, column = 1)


    def play(self):
        self.questions()
        self.setupGUI()



window = Tk()
window.title("How Smart are You?")
k = Riddles(window)
k.play()
window.mainloop()

        
        
    
