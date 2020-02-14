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
        # self.currentQuestion
        self.count = 0

        
        q1 = Q("Chris1")
        q1.addquestions("What is the powerhouse of the cell?") ## calls the add questions function
        q1.addcorrect(1, "mitochondria")
        q1.addoptions("fitness-gram pacer test", "vacoule", "cell wall" )## calls the add options function

        q2 = Q("Chris2")
        q2.addquestions("What is President Obama's Last name") ## calls the add questions function
        q2.addcorrect(1, "Care")
        q2.addoptions("Barac", "Bush", "Globama" )## calls the add options function

        q3 = Q("Chris3")
        q3.addquestions("The best High School Musical Movie") ## calls the add questions function
        q3.addcorrect(1, "High School Musical 2")
        q3.addoptions("High School Musical", "High School Musical 3", "High School Musical: The Musical: The Series" )## calls the add options function

        q4 = Q("Chris4")
        q4.addquestions("What kind of bird is this?") ## calls the add questions function
        q4.addcorrect(1, "It's a butterfly")
        q4.addoptions("It's a bird", "Bird are robots made by the government", "Perigrine Falcon" )## calls the add options function

        q5 = Q("Chris5")
        q5.addquestions("Who is the fastest man alive?")
        q5.addcorrect(1, "Barry Allen")
        q5.addoptions("Zoom", "Savitar", "The Thinker" )

        # 6
        q6 = Q("Chris")
        q6.addquestions("Bears, Beats, _____")
        q6.addcorrect(1, "Battlestar Galactica!")
        q6.addoptions("Michale!!!", "Michael!", "Identity theft is not a joke, Jim" )

        # 7
        q7 = Q("Chris")
        q7.addquestions("Pac-Man's Original Name")
        q7.addcorrect(1, "Puck-Man")
        q7.addoptions("Chuck-Man", "Bite-Man", "Hockey-Man" )

        # 8
        q8 = Q("Chris")
        q8.addquestions("How long would it take to fall from Wyly tower?")
        q8.addcorrect(1, "3.526 seconds")
        q8.addoptions("12.039 seconds", "93.7 hours", "0.1s seconds" )

        # 9
        q9 = Q("Chris")
        q9.addquestions("How many keys are on a piano?")
        q9.addcorrect(1, "88")
        q9.addoptions("75", "108", "56" )

        # 10
        q10 = Q("Chris")
        q10.addquestions("How many times can you listen to 'Piano Man' in a single day?")
        q10.addcorrect(1, "254")
        q10.addoptions("134", "over 9000", "536" )
        
        
        q1.shuffle() ## calls the shuffle function
        q2.shuffle()
        q3.shuffle()
        q4.shuffle()
        q5.shuffle()
        q6.shuffle()
        q7.shuffle()
        q8.shuffle()
        q9.shuffle()
        q10.shuffle()
        q11.shuffle()
        q12.shuffle()
        q13.shuffle()
        q14.shuffle()
        q15.shuffle()
        q16.shuffle()
        q17.shuffle()
        q18.shuffle()
        q19.shuffle()
        q20.shuffle()
        q21.shuffle()
        q22.shuffle()
        q23.shuffle()
        q24.shuffle()
        q25.shuffle()
        q26.shuffle()
        q27.shuffle()
        q28.shuffle()
        q29.shuffle()
        q30.shuffle()
        
        
        
        # end screen
        es = Q("endScreen")


        self.questionlist(q1) ## append each question into a list
        self.questionlist(q2)
        self.questionlist(q3)
        

        self.currentQuestion = self.allQuestions[self.count]


    def questionlist(self, q):
        self.allQuestions.append(q)

    def process(self, button, window):
        if(button == self.currentQuestion.text[1] and button == self.currentQuestion.answers[0]):
            self.b1.configure(bg = "green")
            
            self.l1 = Label(window , text = "correct !", anchor = "center", bg = "green")
            
            self.l1.grid(rowspan = 4, columnspan = 6)
            
        elif(button == self.currentQuestion.text[1]and button == self.currentQuestion.answers[1]):
            self.b2.configure(bg = "green")
            
            self.l1 = Label(window, text = "correct!", anchor = "center", bg = "green")
            
            self.l1.grid(rowspan = 4, columnspan = 6)
            
        elif(button == self.currentQuestion.text[1] and button == self.currentQuestion.answers[2]):
            self.b3.configure(bg = "green")
            self.l1 = Label(window, text = "correct!", anchor = "center", bg = "green")

            self.l1.grid(rowspan = 4, columnspan = 6)
            
        elif(button == self.currentQuestion.text[1] and button == self.currentQuestion.answers[3]):
            
            self.b4.configure(bg = "green")
            
            self.l1 = Label(window, text = "correct", bg = "green")
            self.l1.grid(rowspan = 4, columnspan = 6)

        #wrong answer
        elif(button != self.currentQuestion.text[1] and button == self.currentQuestion.answers[0]):
            
            self.b1.configure(bg = "red")
            
            self.l1 = Label(window, text = "wrong, the correct answer is ({})".format(self.currentQuestion.text[1]) , anchor = "center", bg = "red")
            
            self.l1.grid(rowspan = 10, columnspan = 7)
            
            #correct = self.currentQuestion.text[1]     
        elif(button != self.currentQuestion.text[1]and button == self.currentQuestion.answers[1]):
            
            self.b2.configure(bg = "red")
            
            self.l1 = Label(window, text = "wrong, the correct answer is ({})".format(self.currentQuestion.text[1]) , anchor = "center", bg = "red")
            
            self.l1.grid(rowspan = 10, columnspan = 7)

        elif(button != self.currentQuestion.text[1] and button == self.currentQuestion.answers[2]):
            
            self.b3.configure(bg = "red")
            
            self.l1 = Label(window, text = "wrong, the correct answer is ({})".format(self.currentQuestion.text[1]) , anchor = "center", bg = "red")
            
            self.l1.grid(rowspan = 10, columnspan = 7)

        elif(button != self.currentQuestion.text[1] and button == self.currentQuestion.answers[3]):
            self.b4.configure(bg = "red")
            
            self.l1 = Label(window, text = "wrong, the correct answer is ({})".format(self.currentQuestion.text[1]) , anchor = "center", bg = "red")
            
            self.l1.grid(rowspan = 10, columnspan = 7)


    def next(self, button):
        self.count += 1

            
        if (button == "next" and self.count < len(self.allQuestions)):
            self.currentQuestion = self.allQuestions[self.count]
            self.b1.destroy()
            self.b2.destroy()
            self.b3.destroy()
            self.b4.destroy()
            self.b4.destroy()
            self.l1.destroy()
            self.setupGUI()

        if (button == "next" and self.count == len(self.allQuestions)):
            self.b1.destroy()
            self.b2.destroy()
            self.b3.destroy()
            self.b4.destroy()
            self.b4.destroy()
            self.l1.destroy()
            self.b5.config(text = "Exit", command = window.destroy)
            self.display.destroy()
            self.end = Label(window, text = "Game over Man", font = ("Courier", 44), anchor = "center", bg = "lightgreen")
            self.end.grid(row = 0, columnspan = 5)

        
            
                


    def setupGUI(self):
        self.display = Label(window, text = "Question: \n{}".format(self.currentQuestion.questions[0]), anchor = "center", bg = "lightblue")##sets each question as a \
        #label by calling its key from the dictionary.if it is confusing you can check the lectures on "more on data" on moodle.
        self.display.grid(row = 0,  columnspan = 5)

        self.b1 = Button(window, text = "A: {}".format(self.currentQuestion.answers[0]), command = lambda: self.process(self.currentQuestion.answers[0], window))
        self.b1.grid(row = 1, column = 0)

        self.b2 = Button(window, text = "B: {}".format(self.currentQuestion.answers[1]), command = lambda: self.process(self.currentQuestion.answers[1], window))
        self.b2.grid(row = 1, column = 1)

        self.b3 = Button(window, text = "C: {}".format(self.currentQuestion.answers[2]), command = lambda: self.process(self.currentQuestion.answers[2], window))
        self.b3.grid(row = 2, column = 0)

        self.b4 = Button(window, text = "D: {}".format(self.currentQuestion.answers[3]), command = lambda: self.process(self.currentQuestion.answers[3], window))
        self.b4.grid(row = 2, column = 1)

        self.b5 = Button(window, text = "next", command = lambda : self.next("next"))
        self.b5.grid(row = 10, column = 2)


    def play(self):
        self.questions()
        self.setupGUI()


window = Tk()
window.title("How Smart are You?")
k = Riddles(window)
k.play()
#window.bind("<Button-1>", k.iterator)

window.mainloop()

        
        
    
