from Tkinter import *
import Tkinter
import random
from time import sleep
import shelve

class Q(object):
    def __init__(self, name, difficulty):
        self.text = {} ##stores the dif and correct answer in a dictionary
        self.answers = []### contains the options including the correct answer
        self.questions = []### contains the questions
        self.difficulty = difficulty
        k.allQuestions.append(self)

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

    def addCorrect(self, dif, correct): ##adds the question as the key and the correct answer as the data value in the dictionary
        self._text[dif] = correct
        self._answers.append(correct) ## adds the correct answer into the self.answers list

    def addQuestions(self, q):
        self._questions.append(q)

    def addOptions(self, a,b,c): ##adds the wrong answers to a list ##adds the wrong answers into the self.answers list
        self._answers.append(a)
        self._answers.append(b)
        self._answers.append(c)

    def shuffle(self):
        random.shuffle(self.answers) ## function that shuffles the answers

#this is the game function
class Riddles(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.allQuestions = [] ## adds all the question variables into a list
        self.points = 0

        # clock stuff
        self.remaining = 0
        self.countdown(20)
        self.over = False
    
    ## creates the 20 questions
    def questions(self):
        self.count = 0
        q1 = Q("Chris1", 2)
        q2 = Q("Chris2", 3)
        q3 = Q("Chris3", 4)
        q4 = Q("Chris4", 5)
        q5 = Q("Chris5", 1)
        q6 = Q("Chris6", 1)
        q7 = Q("Chris7", 4)
        q8 = Q("Chris8", 5)
        q9 = Q("Chris9", 4)
        q10 = Q("Chris10", 5)
        q11 = Q("Sadiat1", 1)
        q12 = Q("Sadiat2", 2)
        q13 = Q("Sadiat3", 4)
        q14 = Q("Sadiat4", 3)
        q15 = Q("Sadiat5", 1)
        q16 = Q("Sadiat6", 1)
        q17 = Q("Sadiat7", 3)
        q18 = Q("Sadiat8", 3)
        q19 = Q("Sadiat9", 4)
        q20 = Q("Sadiat10", 5)
        q21 = Q("Andres1", 1)
        q22 = Q("Andres2", 5)
        q23 = Q("Andres3", 5)
        q24 = Q("Andres4", 5)
        q25 = Q("Andres5", 4)
        q26 = Q("Andres6", 5)
        q27 = Q("Andres7", 2)
        q28 = Q("Andres8", 1)
        q29 = Q("Andres9", 1)
        q30 = Q("Andres10", 1)

        random.shuffle(self.allQuestions)
        
        q1.addQuestions("What is the powerhouse of the cell?") ## calls the add questions function
        q1.addCorrect(1, "mitochondria")
        q1.addOptions("medulla oblongata", "vacuole", "rhibosomes" )## calls the add options function
        
        q2.addQuestions("What is the Ultimate ANSWER to life, the universe and everything?") ## calls the add questions function
        q2.addCorrect(1, "42")
        q2.addOptions("Douglas Adams", "24", "nobody knows" )## calls the add options function
        
        q3.addQuestions("The best High School Musical Movie") ## calls the add questions function
        q3.addCorrect(1, "High School Musical 2")
        q3.addOptions("High School Musical", "High School Musical 3", "High School Musical: The Musical: The Series" )## calls the add options function

        q4.addQuestions("What is the Ultimate QUESTION to life, the universe and everything?") ## calls the add questions function
        q4.addCorrect(1, "How many roads must a man walk down?")
        q4.addOptions("Why?", "How many Vogons does it take to change a lightbulb?", "What do you get when you multiply six by seven?" )## calls the add options function

        q5.addQuestions("Who is the fastest man alive?")
        q5.addCorrect(1, "Barry Allen")
        q5.addOptions("Zoom", "Savitar", "The Thinker" )

        q6.addQuestions("Bears, Beats, _____")
        q6.addCorrect(1, "Battlestar Galactica!")
        q6.addOptions("Michael!!!", "Michael!", "Identity theft is not a joke, Jim" )

        q7.addQuestions("Pac-Man's Original Name")
        q7.addCorrect(1, "Puck-Man")
        q7.addOptions("Chuck-Man", "Bite-Man", "Hockey-Man" )

        q8.addQuestions("How long would it take to fall from Wyly tower?")
        q8.addCorrect(1, "3.526 seconds")
        q8.addOptions("12.039 seconds", "93.7 hours", "0.1s seconds" )

        q9.addQuestions("How many keys are on a piano?")
        q9.addCorrect(1, "88")
        q9.addOptions("75", "108", "56" )

        q10.addQuestions("How many people are in space as of today?")
        q10.addCorrect(1, "3")
        q10.addOptions("0", "1", "2" )

        q11.addQuestions("What is the gravity constant on earth?")
        q11.addCorrect(1, "9.81")
        q11.addOptions("9.1", "9.3", "8.5")

        q12.addQuestions("What is the biggest city in the United States?")
        q12.addCorrect(1, "New York")
        q12.addOptions("Los Angeles", "Chicago", "Miami")

        q13.addQuestions("What is SIN(30)?")
        q13.addCorrect(1, "0.5")
        q13.addOptions("1.5", "0.6", "0.525")

        q14.addQuestions("What is the derivative of SIN(X)?")
        q14.addCorrect(1, "COS(X)")
        q14.addOptions("-SIN(X)", "-COS(X)", "TAN(X)")

        q15.addQuestions("Most Populated Country in the World?")
        q15.addCorrect(1, "China")
        q15.addOptions("India", "United States", "Indonesia")

        q16.addQuestions("What is the Largest Continent in the World?")
        q16.addCorrect(1, "Asia")
        q16.addOptions("Africa", "Europe", "South America")

        q17.addQuestions("Who killed the night watchman in Game of Thrones?")
        q17.addCorrect(1, "Arya")
        q17.addOptions("Jon", "Sansa", "Jamie")

        q18.addQuestions("Who killed James St.Patrick in Power?")
        q18.addCorrect(1, "Tariq")
        q18.addOptions("Tasha", "Tommy", "Kanan")

        q19.addQuestions("What is the equation for calculating the voltage of a circuit?")
        q19.addCorrect(1, "V = IR")
        q19.addOptions("V = I/R", "V = R/I", "V = CR")

        q20.addQuestions("Who played the role fo Joe Goldberg in 'You', the Netlifx series")
        q20.addCorrect(1, "Penn Badgley")
        q20.addOptions("Josheph Morgan", "Tom Holland", "Chadwick Boseman")

        q21.addQuestions("Who is Iron Man?")
        q21.addCorrect(1, "Tony Stark")
        q21.addOptions("Bruce Banner", "Peter Parker", "Steve Rogers")

        q22.addQuestions("Who is the Ghostbuster who has glasses?")
        q22.addCorrect(1, "Egon Spengler")
        q22.addOptions("Winston Zeddemore", "Peter Venkmen", "Ray Stanz")

        q23.addQuestions("Who played the 11th Doctor on Doctor Who?")
        q23.addCorrect(1, "Matt Smith")
        q23.addOptions("Peter Capaldi", "Jodie Whittaker", "David Tennant")

        q24.addQuestions("What is the subtitle for the 8th Star Wars film?")
        q24.addCorrect(1, "The Last Jedi")
        q24.addOptions("The Force Awakens", "Attack of the Clones", "A New Hope")

        q25.addQuestions("What is the name of Doc Brown's dog in 1955?")
        q25.addCorrect(1, "Copernicus")
        q25.addOptions("Einstein", "Newton", "Oppenheimer")

        q26.addQuestions("What is first name of Kramer in Seinfeld?")
        q26.addCorrect(1, "Cosmo")
        q26.addOptions("George", "Jerry", "Newman")

        q27.addQuestions("How many rings were orignially forged in Lord of the Rings?")
        q27.addCorrect(1, "20")
        q27.addOptions("9", "7", "3")

        q28.addQuestions("Who sings the popular song 'All-Star' from Shrek?")
        q28.addCorrect(1, "Smashmouth")
        q28.addOptions("Black Sabbath", "AC/DC", "Van Halen")

        q29.addQuestions("What is the name of the fictional country in Black Panther?")
        q29.addCorrect(1, "Wakanda")
        q29.addOptions("Wyoming", "Ontario", "South Korea")

        q30.addQuestions("What is Buzz Lightyear's catchphrase?")
        q30.addCorrect(1, "To infinity and beyond!")
        q30.addOptions("This really is a Toy Story", "What's the deal with toys?", "Buzz")

        
        for i in self.allQuestions:
            i.shuffle()

        self.currentQuestion = self.allQuestions[self.count]
    
    
    def process(self, button, window):
        if(button == self.currentQuestion.text[1] and button == self.currentQuestion.answers[0]):
            self.b1.configure(bg = "green")
            self.points += 1
            
            self.l1 = Label(window , text = "correct !", anchor = "center", bg = "green")
            
            self.l1.grid(rowspan = 4, columnspan = 6)
            
        elif(button == self.currentQuestion.text[1]and button == self.currentQuestion.answers[1]):
            self.points += 1
            self.b2.configure(bg = "green")
            
            self.l1 = Label(window, text = "correct!", anchor = "center", bg = "green")
            
            self.l1.grid(rowspan = 4, columnspan = 6)
            
        elif(button == self.currentQuestion.text[1] and button == self.currentQuestion.answers[2]):
            self.points += 1
            self.b3.configure(bg = "green")
            self.l1 = Label(window, text = "correct!", anchor = "center", bg = "green")

            self.l1.grid(rowspan = 4, columnspan = 6)
            
        elif(button == self.currentQuestion.text[1] and button == self.currentQuestion.answers[3]):
            self.points += 1
            
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
            self.display.destroy()
            self.l1.destroy()
            self.setupGUI()

        # we're in the endgame now
        if (button == "next" and self.count >= 3): # goes through less questions
            self.gameOver()
                
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
        
        self.l1 = Label(window, text = "") # init's the l1 so the game dones't crash if user accidentally clicks next button

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.gameOver()
            
        elif self.remaining > 0:
            self.clock = Label(text="Time left: %d:%d" % (int(self.remaining / 60), (self.remaining - int(self.remaining / 60) * 60 )))
            self.clock.grid(row = 10, column = 0)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)
    
    def play(self):
        self.questions()
        self.setupGUI()

    def gameOver(self):
            self.b1.destroy()
            self.b2.destroy()
            self.b3.destroy()
            self.b4.destroy()
            self.b4.destroy()
            self.display.destroy()
            self.clock.destroy()
            self.l1.destroy()
            self.b5.config(text = "Exit", command = window.destroy)
            self.end = Label(window, text = "GAME OVER", font = ("Courier", 44), anchor = "center", bg = "lightgreen")
            self.end.grid(row = 0, column = 0, columnspan = 5)
            
            if self.points == 1:
                self.score = Label(window, text = "You scored {} point!".format(self.points), font = ("Courier", 30), anchor = "center", bg = "lightgreen")
            else:
                self.score = Label(window, text = "You scored {} points!".format(self.points), font = ("Courier", 30), anchor = "center", bg = "lightgreen")
            
            self.score.grid(row = 2, column = 0, columnspan = 5)

            self.highscores()

            self.getName()
    
    # this makes a tkinter entry that allows the user to save their score
    def getName(self):
        self.name = Label(window, text = "ENTER YOUR NAME: ")
        self.name.grid(row = 3, column = 0)
        self.string = StringVar()
        self.input = Entry(window, textvariable = self.string).grid(row = 3, column = 1)
        enterName = Button(window, text = "Enter", command = self.getValue).grid(row = 3, column = 2)

    # this stores a file with the scores in it
    def save(self, score, name):
        s = shelve.open("score.txt")
        s[name] = score
        s.close()

    def getValue(self):
        # the player's name
        var = self.string.get()
        self.save(self.points, var)

    # displays high scores
    def highscores(self):
        s = shelve.open("score.txt")
        for key in s:
            highscores = Label(window, text = "{}: {}".format(key, s[key])).grid(row = 4, column = 1)

window = Tk()
window.title("%dx%d+0+0" % (window.winfo_screenwidth(), window.screenheight()))

k = Riddles(window)
k.play()

window.mainloop()

        
        
    
