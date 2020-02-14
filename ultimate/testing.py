from Tkinter import *
import random
from time import sleep

class Q(object):
    def __init__(self, name):
        self.text = {} ##stores the dif and correct answer in a dictionary
        self.answers = []### contains the options including the correct answer
        self.questions = []### contains the questions
        k.qlist.append(self)

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
        self.qlist = []

        

    ## creates the 20 questions
    def questions(self):
        # self.currentQuestion
        self.count = 0

        
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
 
        
        q1.addquestions("What is the powerhouse of the cell?") ## calls the add questions function
        q1.addcorrect(1, "mitochondria")
        q1.addoptions("fitness-gram pacer test", "vacoule", "cell wall" )## calls the add options function
        
        q2.addquestions("What is President Obama's Last name") ## calls the add questions function
        q2.addcorrect(1, "Care")
        q2.addoptions("Barac", "Bush", "Globama" )## calls the add options function
        
        q3.addquestions("The best High School Musical Movie") ## calls the add questions function
        q3.addcorrect(1, "High School Musical 2")
        q3.addoptions("High School Musical", "High School Musical 3", "High School Musical: The Musical: The Series" )## calls the add options function

        q4.addquestions("What kind of bird is this?") ## calls the add questions function
        q4.addcorrect(1, "It's a butterfly")
        q4.addoptions("It's a bird", "Bird are robots made by the government", "Perigrine Falcon" )## calls the add options function

        q5.addquestions("Who is the fastest man alive?")
        q5.addcorrect(1, "Barry Allen")
        q5.addoptions("Zoom", "Savitar", "The Thinker" )

        q6.addquestions("Bears, Beats, _____")
        q6.addcorrect(1, "Battlestar Galactica!")
        q6.addoptions("Michale!!!", "Michael!", "Identity theft is not a joke, Jim" )

        q7.addquestions("Pac-Man's Original Name")
        q7.addcorrect(1, "Puck-Man")
        q7.addoptions("Chuck-Man", "Bite-Man", "Hockey-Man" )

        q8.addquestions("How long would it take to fall from Wyly tower?")
        q8.addcorrect(1, "3.526 seconds")
        q8.addoptions("12.039 seconds", "93.7 hours", "0.1s seconds" )

        q9.addquestions("How many keys are on a piano?")
        q9.addcorrect(1, "88")
        q9.addoptions("75", "108", "56" )

        q10.addquestions("How many times can you listen to 'Piano Man' in a single day?")
        q10.addcorrect(1, "254")
        q10.addoptions("134", "over 9000", "536" )

        q11.addquestions("What is the gravity constant on earth?")
        q11.addcorrect(1, "9.81")
        q11.addoptions("9.1", "9.3", "8.5")

        q12.addquestions("What is the biggest city in the United States?")
        q12.addcorrect(1, "New York")
        q12.addoptions("Los Angeles", "Chicago", "Miami")

        q13.addquestions("What is SIN(30)?")
        q13.addcorrect(1, "0.5")
        q13.addoptions("1.5", "0.6", "0.525")

        q14.addquestions("What is the derivative of SIN(X)?")
        q14.addcorrect(1, "COS(X)")
        q14.addoptions("-SIN(X)", "-COS(X)", "TAN(X)")

        q15.addquestions("Most Populated Country in the World?")
        q15.addcorrect(1, "China")
        q15.addoptions("India", "United States", "Indonesia")

        q16.addquestions("What is the Largest Continent in the World?")
        q16.addcorrect(1, "Asia")
        q16.addoptions("Africa", "Europe", "South America")

        q17.addquestions("Who killed the night watchman in Game of Thrones?")
        q17.addcorrect(1, "Arya")
        q17.addoptions("Jon", "Sansa", "Jamie")

        q18.addquestions("Who killed James St.Patrick in Power?")
        q18.addcorrect(1, "Tariq")
        q18.addoptions("Tasha", "Tommy", "Kanan")

        q19.addquestions("What is the equation for calculating the voltage of a circuit?")
        q19.addcorrect(1, "V = IR")
        q19.addoptions("V = I/R", "V = R/I", "V = CR")

        q20.addquestions("Who played the role fo Joe Goldberg in 'You', the Netlifx series")
        q20.addcorrect(1, "Penn Badgley")
        q20.addoptions("Josheph Morgan", "Tom Holland", "Chadwick Boseman")

        q21.addquestions("Who is Iron Man?")
        q21.addcorrect(1, "Tony Stark")
        q21.addoptions("Bruce Banner", "Peter Parker", "Steve Rogers")

        q22.addquestions("Who is the Ghostbuster who has glasses?")
        q22.addcorrect(1, "Egon Spengler")
        q22.addoptions("Winston Zeddemore", "Peter Venkmen", "Ray Stanz")

        q23.addquestions("Who played the 11th Doctor on Doctor Who?")
        q23.addcorrect(1, "Matt Smith")
        q23.addoptions("Peter Capaldi", "Jodie Whittaker", "David Tennant")

        q24.addquestions("What is the subtitle for the 8th Star Wars film?")
        q24.addcorrect(1, "The Last Jedi")
        q24.addoptions("The Force Awakens", "Attack of the Clones", "A New Hope")

        q25.addquestions("What is the name of Doc Brown's dog in 1955?")
        q25.addcorrect(1, "Copernicus")
        q25.addoptions("Einstein", "Newton", "Oppenheimer")

        q26.addquestions("What is first name of Kramer in Seinfeld?")
        q26.addcorrect(1, "Cosmo")
        q26.addoptions("George", "Jerry", "Newman")

        q27.addquestions("How many rings were orignially forged in Lord of the Rings?")
        q27.addcorrect(1, "20")
        q27.addoptions("9", "7", "3")

        q28.addquestions("Who sings the popular song 'All-Star' from Shrek?")
        q28.addcorrect(1, "Smashmouth")
        q28.addoptions("Black Sabbath", "AC/DC", "Van Halen")

        q29.addquestions("What is the name of the fictional country in Black Panther?")
        q29.addcorrect(1, "Wakanda")
        q29.addoptions("Wyoming", "Ontario", "South Korea")

        q30.addquestions("What is Buzz Lightyear's catchphrase?")
        q30.addcorrect(1, "To infinity and beyond!")
        q30.addoptions("This really is a Toy Story", "What's the deal with toys?", "Buzz")

        
        for i in self.qlist:
            i.shuffle()
            self.questionlist(i)
        

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

        # if (button == "next" and self.count == len(self.allQuestions)): # goes through all questions
        if (button == "next" and self.count == 3): # goes through less questions
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

        
        
    
