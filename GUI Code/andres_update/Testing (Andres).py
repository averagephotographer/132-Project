from Tkinter import *
import random
from time import sleep
import RPi.GPIO as GPIO

##setting up the LED
wrong = 22
correct = 12

##use the broadcam pin code
GPIO.setmode(GPIO.BCM)

##Setup the LED and switch pins
GPIO.setup(wrong, GPIO.OUT)
GPIO.setup(correct, GPIO.OUT)

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
##        parent.attributes("-fullscreen", True)
        self.allQuestions = [] ## adds all the question variables into a list
        self.points = 0

        # timer stuff
        self.remaining = 0
        #self.countdown(20)
        

    ## creates the 20 questions
    def questions(self):
        # self.currentQuestion
        self.count = 0

        
        q1 = Q("Chris1")
        q2 = Q("Chris2")
        q3 = Q("Chris3")
        q4 = Q("Chris4")
        q5 = Q("Chris5")
        q6 = Q("Chris6")
        q7 = Q("Chris7")
        q8 = Q("Chris8")
        q9 = Q("Chris9")
        q10 = Q("Chris10")
        q11 = Q("Sadiat1")
        q12 = Q("Sadiat2")
        q13 = Q("Sadiat3")
        q14 = Q("Sadiat4")
        q15 = Q("Sadiat5")
        q16 = Q("Sadiat6")
        q17 = Q("Sadiat7")
        q18 = Q("Sadiat8")
        q19 = Q("Sadiat9")
        q20 = Q("Sadiat10")
        q21 = Q("Andres1")
        q22 = Q("Andres2")
        q23 = Q("Andres3")
        q24 = Q("Andres4")
        q25 = Q("Andres5")
        q26 = Q("Andres6")
        q27 = Q("Andres7")
        q28 = Q("Andres8")
        q29 = Q("Andres9")
        q30 = Q("Andres10")
 
        
        q1.addquestions("What is the powerhouse of the cell?") ## calls the add questions function
        q1.addcorrect(1, "mitochondria")
        q1.addoptions("fitness-gram pacer test", "vacoule", "cell wall" )## calls the add options function
        q1.shuffle()
        
        q2.addquestions("What is President Obama's Last name") ## calls the add questions function
        q2.addcorrect(1, "Barack")
        q2.addoptions("Care", "Bush", "Globama" )## calls the add options function
        q2.shuffle()
        
        q3.addquestions("The best High School Musical Movie") ## calls the add questions function
        q3.addcorrect(1, "High School Musical 2")
        q3.addoptions("High School Musical", "High School Musical 3", "High School Musical: The Musical: The Series" )## calls the add options function
        q3.shuffle()
        
        
        q4.addquestions("Who is the fastest man alive?")
        q4.addcorrect(1, "Barry Allen")
        q4.addoptions("Zoom", "Savitar", "The Thinker" )
        q4.shuffle()
        
        q5.addquestions("Bears, Beats, _____")
        q5.addcorrect(1, "Battlestar Galactica!")
        q5.addoptions("Michale!!!", "Michael!", "Identity theft is not a joke, Jim" )
        q5.shuffle()
        
        
        q6.addquestions("How long would it take to fall from Wyly tower?")
        q6.addcorrect(1, "3.526 seconds")
        q6.addoptions("12.039 seconds", "93.7 hours", "0.1s seconds" )
        q6.shuffle()

        q7.addquestions("How many keys are on a piano?")
        q7.addcorrect(1, "88")
        q7.addoptions("75", "108", "56" )
        q7.shuffle()

        
        q8.addquestions("What is the gravity constant on earth?")
        q8.addcorrect(1, "9.81")
        q8.addoptions("9.1", "9.3", "8.5")
        q8.shuffle()

        q9.addquestions("What is the biggest city in the United States?")
        q9.addcorrect(1, "New York")
        q9.addoptions("Los Angeles", "Chicago", "Miami")
        q9.shuffle()

        q10.addquestions("What is SIN(30)?")
        q10.addcorrect(1, "0.5")
        q10.addoptions("1.5", "0.6", "0.525")
        q10.shuffle()

        q11.addquestions("What is the derivative of SIN(X)?")
        q11.addcorrect(1, "COS(X)")
        q11.addoptions("-SIN(X)", "-COS(X)", "TAN(X)")
        q11.shuffle()

        q12.addquestions("Most Populated Country in the World?")
        q12.addcorrect(1, "China")
        q12.addoptions("India", "United States", "Indonesia")
        q12.shuffle()

        q13.addquestions("What is the Largest Continent in the World?")
        q13.addcorrect(1, "Asia")
        q13.addoptions("Africa", "Europe", "South America")
        q13.shuffle()

        q14.addquestions("Who killed the night watchman in Game of Thrones?")
        q14.addcorrect(1, "Arya")
        q14.addoptions("Jon", "Sansa", "Jamie")
        q14.shuffle()

        
    

        q15.addquestions("What is the equation for calculating the voltage of a circuit?")
        q15.addcorrect(1, "V = IR")
        q15.addoptions("V = I/R", "V = R/I", "V = CR")
        q15.shuffle()

        q16.addquestions("Who played the role fo Joe Goldberg in 'You', the Netlifx series")
        q16.addcorrect(1, "Penn Badgley")
        q16.addoptions("Josheph Morgan", "Tom Holland", "Chadwick Boseman")
        q16.shuffle()

        q17.addquestions("Who is Iron Man?")
        q17.addcorrect(1, "Tony Stark")
        q17.addoptions("Bruce Banner", "Peter Parker", "Steve Rogers")
        q17.shuffle()

        q18.addquestions("Who is the Ghostbuster who has glasses?")
        q18.addcorrect(1, "Egon Spengler")
        q18.addoptions("Winston Zeddemore", "Peter Venkmen", "Ray Stanz")
        q18.shuffle()

        q19.addquestions("Who played the 11th Doctor on Doctor Who?")
        q19.addcorrect(1, "Matt Smith")
        q19.addoptions("Peter Capaldi", "Jodie Whittaker", "David Tennant")
        q19.shuffle()

        q20.addquestions("What is the subtitle for the 8th Star Wars film?")
        q20.addcorrect(1, "The Last Jedi")
        q20.addoptions("The Force Awakens", "Attack of the Clones", "A New Hope")
        q20.shuffle()

        q21.addquestions("What is the name of Doc Brown's dog in 1955?")
        q21.addcorrect(1, "Copernicus")
        q21.addoptions("Einstein", "Newton", "Oppenheimer")
        q21.shuffle()

        q22.addquestions("What is first name of Kramer in Seinfeld?")
        q22.addcorrect(1, "Cosmo")
        q22.addoptions("George", "Jerry", "Newman")
        q22.shuffle()

        q23.addquestions("How many rings were orignially forged in Lord of the Rings?")
        q23.addcorrect(1, "20")
        q23.addoptions("9", "7", "3")
        q23.shuffle()

        q24.addquestions("Who sings the popular song 'All-Star' from Shrek?")
        q24.addcorrect(1, "Smashmouth")
        q24.addoptions("Black Sabbath", "AC/DC", "Van Halen")
        q24.shuffle()

        q25.addquestions("What is the name of the fictional country in Black Panther?")
        q25.addcorrect(1, "Wakanda")
        q25.addoptions("Wyoming", "Ontario", "South Korea")
        q25.shuffle()

        q26.addquestions("What is Buzz Lightyear's catchphrase?")
        q26.addcorrect(1, "To infinity and beyond!")
        q26.addoptions("This really is a Toy Story", "What's the deal with toys?", "Buzz")
        q26.shuffle()

        self.questionlist(q1)
        self.questionlist(q2)
        self.questionlist(q3)
        self.questionlist(q4)
        self.questionlist(q5)
        self.questionlist(q6)
        self.questionlist(q7)
        self.questionlist(q8)
        self.questionlist(q9)
        self.questionlist(q10)
        self.questionlist(q11)
        self.questionlist(q12)
        self.questionlist(q13)
        self.questionlist(q14)
        self.questionlist(q15)
        self.questionlist(q16)
        self.questionlist(q17)
        self.questionlist(q18)
        self.questionlist(q19)
        self.questionlist(q20)
        self.questionlist(q21)
        self.questionlist(q22)
        self.questionlist(q23)
        self.questionlist(q24)
        self.questionlist(q25)
        self.questionlist(q26)
        

        
        random.shuffle(self.allQuestions)

        self.currentQuestion = self.allQuestions[self.count]


    def questionlist(self, q):
        self.allQuestions.append(q)

    def process(self, button, window):
        if(button == self.currentQuestion.text[1] and button == self.currentQuestion.answers[0]):
            self.b1.configure(bg = "green")
            
            self.l1 = Label(window , text = "correct !", anchor = "center", bg = "green")
            
            self.points+= 1

            GPIO.output(correct, GPIO.HIGH)
            sleep(1.0)
            GPIO.output(correct, GPIO.LOW)

            self.l1.pack(fill = Y, expand = True)
            
##            self.l1.grid(rowspan = 4, columnspan = 6)
            
        elif(button == self.currentQuestion.text[1]and button == self.currentQuestion.answers[1]):
            self.b2.configure(bg = "green")
            
            self.l1 = Label(window, text = "correct!", anchor = "center", bg = "green")
            self.points+= 1

            GPIO.output(correct, GPIO.HIGH)
            sleep(1.0)
            GPIO.output(correct, GPIO.LOW)

            self.l1.pack(fill = Y, expand = True)
            
##            self.l1.grid(rowspan = 4, columnspan = 6)
            
        elif(button == self.currentQuestion.text[1] and button == self.currentQuestion.answers[2]):
            self.b3.configure(bg = "green")
            self.l1 = Label(window, text = "correct!", anchor = "center", bg = "green")
            self.points += 1
            
            GPIO.output(correct, GPIO.HIGH)
            sleep(1.0)
            GPIO.output(correct, GPIO.LOW)


            self.l1.pack(fill = Y, expand = True)

##            self.l1.grid(rowspan = 4, columnspan = 6)
            
        elif(button == self.currentQuestion.text[1] and button == self.currentQuestion.answers[3]):
            
            self.b4.configure(bg = "green")
            
            self.l1 = Label(window, text = "correct", bg = "green")

            self.points+= 1
            
            GPIO.output(correct, GPIO.HIGH)
            sleep(1.0)
            GPIO.output(correct, GPIO.LOW)


            self.l1.pack(fill = Y, expand = True)
##            self.l1.grid(rowspan = 4, columnspan = 6)

        #wrong answer
        elif(button != self.currentQuestion.text[1] and button == self.currentQuestion.answers[0]):
            
            self.b1.configure(bg = "red")
            
            self.l1 = Label(window, text = "wrong, the correct answer is ({})".format(self.currentQuestion.text[1]) , anchor = "center", bg = "red")

            GPIO.output(wrong, GPIO.HIGH)
            sleep(1.0)
            GPIO.output(wrong, GPIO.LOW)
            
            self.l1.pack(fill = Y, expand = True)
##            self.l1.grid(rowspan = 10, columnspan = 7)
            
            #correct = self.currentQuestion.text[1]     
        elif(button != self.currentQuestion.text[1]and button == self.currentQuestion.answers[1]):
            
            self.b2.configure(bg = "red")
            
            self.l1 = Label(window, text = "wrong, the correct answer is ({})".format(self.currentQuestion.text[1]) , anchor = "center", bg = "red")

            GPIO.output(wrong, GPIO.HIGH)
            sleep(1.0)
            GPIO.output(wrong, GPIO.LOW)
            
            self.l1.pack(fill = Y, expand = True)
##            self.l1.grid(rowspan = 10, columnspan = 7)

        elif(button != self.currentQuestion.text[1] and button == self.currentQuestion.answers[2]):
            
            self.b3.configure(bg = "red")
            
            self.l1 = Label(window, text = "wrong, the correct answer is ({})".format(self.currentQuestion.text[1]) , anchor = "center", bg = "red")

            GPIO.output(wrong, GPIO.HIGH)
            sleep(1.0)
            GPIO.output(wrong, GPIO.LOW)
            
            self.l1.pack(fill = Y, expand = True)
##            self.l1.grid(rowspan = 10, columnspan = 7)

        elif(button != self.currentQuestion.text[1] and button == self.currentQuestion.answers[3]):
            self.b4.configure(bg = "red")
            
            self.l1 = Label(window, text = "wrong, the correct answer is ({})".format(self.currentQuestion.text[1]) , anchor = "center", bg = "red")

            GPIO.output(wrong, GPIO.HIGH)
            sleep(1.0)
            GPIO.output(wrong, GPIO.LOW)
            

            self.l1.pack(fill = Y, expand = True)
##            self.l1.grid(rowspan = 10, columnspan = 7)

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.display.destroy()
            self.b1.destroy()
            self.b2.destroy()
            self.b3.destroy()
            self.b4.destroy()
            self.b5.destroy()
            self.l1.destroy()
            self.clock.destroy()
            self.end = Label(window, text = "Game over Man", font = ("Courier", 44), anchor = "center", bg = "lightgreen")
            self.end.pack(fill = Y, expand = True)
            self.b6 = Button(text = "Exit", command = window.destroy)
            self.b6.pack(fill = Y, expand = True)

            if (self.points == 1):
                self.score = Label(window, text = "You scored {} point!".format(self.points), \
                                   font = ("Courier", 30), anchor = "center", bg = "lightgreen")
            else:
                self.score = Label(window, text = "You scored {} points!".format(self.points), \
                                   font = ("Courier", 30), anchor = "center", bg = "lightgreen")
                
            self.score.pack(fill = Y, expand = True)


        elif self.remaining > 0:
            self.clock = Label(text="Time left: %d:%d" % (int(self.remaining / 60), self.remaining - (self.remaining / 60) * 60))
            self.clock.pack(fill = Y, expand = True)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)
                

    def next(self, button):
        self.count += 1

            
        if (button == "NEXT" and self.count < len(self.allQuestions)):
            self.currentQuestion = self.allQuestions[self.count]
            self.display.destroy()
            self.b1.destroy()
            self.b2.destroy()
            self.b3.destroy()
            self.b4.destroy()
            self.b4.destroy()
            self.b5.destroy()
            self.l1.destroy()
            self.setupGUI()

        # if (button == "next" and self.count == len(self.allQuestions)): # goes through all questions
        if (button == "NEXT" and self.count == 8): # goes through less questions

            self.display.destroy()
            self.b1.destroy()
            self.b2.destroy()
            self.b3.destroy()
            self.b4.destroy()
            self.b5.destroy()
            self.l1.destroy()
            self.end = Label(window, text = "Game over Man", font = ("Courier", 44), anchor = "center", bg = "lightgreen")
            self.end.pack(fill = Y, expand = True)
            self.b6 = Button(text = "Exit", command = window.destroy)
            self.b6.pack(fill = Y, expand = True)

            if(self.points == 1):
                self.score = Label(window, text = "You scored {} point!".format(self.points), \
                                   font = ("Courier", 30), anchor = "center", bg = "lightgreen")
            else:
                self.score = Label(window, text = "You scored {} points!".format(self.points), \
                                   font = ("Courier", 30), anchor = "center", bg = "lightgreen")
                
            self.score.pack(fill = Y, expand = True)               

                 
                


    def setupGUI(self):
        self.display = Label(window, text = "Question: \n{}".format(self.currentQuestion.questions[0]), anchor = "center", bg = "lightblue")##sets each question as a \
        #label by calling its key from the dictionary.if it is confusing you can check the lectures on "more on data" on moodle.
        #self.display.grid(row = 0,  columnspan = 5)
        self.display.pack(fill = Y, expand = True)

        self.b1 = Button(window, text = "A: {}".format(self.currentQuestion.answers[0]), command = lambda: self.process(self.currentQuestion.answers[0], window))
        self.b1.pack(fill = Y, expand = True)
        #self.b1.grid(row = 1, column = 0)

        self.b2 = Button(window, text = "B: {}".format(self.currentQuestion.answers[1]), command = lambda: self.process(self.currentQuestion.answers[1], window))
        self.b2.pack(fill = Y, expand = True)
        #self.b2.grid(row = 1, column = 1)

        self.b3 = Button(window, text = "C: {}".format(self.currentQuestion.answers[2]), command = lambda: self.process(self.currentQuestion.answers[2], window))
        self.b3.pack(fill = Y, expand = True)
        #self.b3.grid(row = 2, column = 0)

        self.b4 = Button(window, text = "D: {}".format(self.currentQuestion.answers[3]), command = lambda: self.process(self.currentQuestion.answers[3], window))
        self.b4.pack(fill = Y, expand = True)
        #self.b4.grid(row = 2, column = 1)

        self.b5 = Button(window, text = "NEXT", command = lambda : self.next("NEXT"))
        self.b5.pack(fill = Y, expand = True)
        #self.b5.grid(row = 10, column = 2)

        
    def play(self):
        self.questions()
        self.setupGUI()


window = Tk() 
window.title("How Smart are You?")
window.geometry("%dx%d+0+0" % (window.winfo_screenwidth(), window.winfo_screenheight()))
k = Riddles(window)
k.play()

window.mainloop()

        
        
    
