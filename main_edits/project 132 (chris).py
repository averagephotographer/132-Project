from Tkinter import *
import random
from time import sleep

class Q(object):
    def __init__(self, name):
        self.text = {} ##stores the dif and correct answer in a dictionary
        self.answers = []### contains the options including the correct answer
        self.questions = []### contains the questions



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

    @property
    def questions(self):
        return self._questions

    @questions.setter
    def questions(self, string):
        self._questions = string

    
    def addcorrect(self, dif, correct): ##adds the question as the key and the correct answer as the data value in the dictionary
        self._text[dif] = correct
        #self._questions = question
        self._answers.append(correct) ## adds the correct answer into the self.answers list

    def addquestions(self, q):
        self._questions.append(q)

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
        self.allQuestions = [] ## adds all the question variables into a list
        

    ## creates the 20 questions
    def questions(self):
        global currentQuestion
        self.count = 0
        self.points = 0

        q1 = Q("question1")
        q2 = Q("question2")
        q3 = Q("question3")
        es = Q("Game Over!")

        q1.addquestions("How are you?") ## calls the add questions function
        q2.addquestions("Who's on first?")
        q3.addquestions("what is the most difficult job?")
        es.addquestions("Game Over!\nYou scored {} points!".format(self.points))

        q1.addcorrect(1, "good")
        q2.addcorrect(1, "me")
        q3.addcorrect(1, "computer science")
        es.addcorrect(1, "exit")

        q1.addoptions("bleh", "okay", "not good" )## calls the add options function
        q1.shuffle() ## calls the shuffle function
        
        
        q2.addoptions("you", "andres", "chris")
        q2.shuffle()
        
        
        q3.addoptions("biology", "physics", "child education" )
        q3.shuffle()
        
        es.addoptions("Congrats!", "Points = n", "more words")
        
        self.questionlist(q1)## append each question into a list
        self.questionlist(q2)
        self.questionlist(q3)
        self.questionlist(es)

        self.currentQuestion = self.allQuestions[self.count]


    def questionlist(self, q):
        self.allQuestions.append(q)

    def process(self, button):
        
        if(button == self.currentQuestion.text[1] and button == self.currentQuestion.answers[0]):
            self.b1.configure(bg = "green")
            self.points += 1
        elif(button == self.currentQuestion.text[1]and button == self.currentQuestion.answers[1]):
            self.b2.configure(bg = "green")
            self.points += 1
        elif(button == self.currentQuestion.text[1] and button == self.currentQuestion.answers[2]):
            self.b3.configure(bg = "green")
            self.points += 1
        elif(button == self.currentQuestion.text[1] and button == self.currentQuestion.answers[3]):
            self.b4.configure(bg = "green")
            self.points += 1

        #wrong answer
        elif(button != self.currentQuestion.text[1] and button == self.currentQuestion.answers[0]):
            self.b1.configure(bg = "red")
            #correct = self.currentQuestion.text[1]     
        elif(button != self.currentQuestion.text[1]and button == self.currentQuestion.answers[1]):
            self.b2.configure(bg = "red")
        elif(button != self.currentQuestion.text[1] and button == self.currentQuestion.answers[2]):
            self.b3.configure(bg = "red")
        elif(button != self.currentQuestion.text[1] and button == self.currentQuestion.answers[3]):
            self.b4.configure(bg = "red")
            
        # else:
        #     for i in range(len(self.currentQuestion)):
        #         if self.currentQuestion.text[1] == self.currentQuestion.answers[i]:
        #             self.buttonAnswerList[i].configure(bg = 'green')
                    
        
            

    def next(self, button):
        self.count += 1
        if (button == "next" and self.count < 2):
            self.currentQuestion = self.allQuestions[self.count]
            self.b1.destroy()
            self.b2.destroy()
            self.b3.destroy()
            self.b4.destroy()
            self.b4.destroy()

        elif self.count >= 2:
            self.b1.destroy()
            self.b2.destroy()
            self.b3.destroy()
            self.b4.destroy()
            self.b4.destroy()
            self.currentQuestion = self.allQuestions[-1]
            self.b1.configure(text = "Exit", command = window.destroy)

        
        self.setupGUI()
        
        
                      
            


    def setupGUI(self):
        self.display = Label(window, text = "Question: \n{}".format(self.currentQuestion.questions[0]), anchor = "center", bg = "lightblue")
        ##sets each question as a
        #label by calling its key from the dictionary.if it is confusing you can check the lectures on "more on data" on moodle.
        self.display.grid(row = 0,  columnspan = 5)

        self.b1 = Button(window, text = "A: {}".format(self.currentQuestion.answers[0]), command = lambda: self.process(self.currentQuestion.answers[0]))
        self.b1.grid(row = 1, column = 0)

        self.b2 = Button(window, text = "B: {}".format(self.currentQuestion.answers[1]), command = lambda: self.process(self.currentQuestion.answers[1]))
        self.b2.grid(row = 1, column = 1)

        self.b3 = Button(window, text = "C: {}".format(self.currentQuestion.answers[2]), command = lambda: self.process(self.currentQuestion.answers[2]))
        self.b3.grid(row = 2, column = 0)

        self.b4 = Button(window, text = "D: {}".format(self.currentQuestion.answers[3]), command = lambda: self.process(self.currentQuestion.answers[3]))
        self.b4.grid(row = 2, column = 1)

        self.b5 = Button(window, text = "next", command = lambda : self.next("next"))
        self.b5.grid(row = 4, column = 2)

        self.buttonAnswerList = [self.b1, self.b2, self.b3, self.b4]

    def play(self):
        self.questions()
        self.setupGUI()


WIDTH = 800
HEIGHT = 600

window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("How Smart are You?")
k = Riddles(window)
k.play()

window.mainloop()

        
        
    
