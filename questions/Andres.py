# format for questions:
    # q1 = Q("question1")
    # q1.addquestions("How are you?") ## calls the add questions function
    # q1.addcorrect(1, "good")
    # q1.addoptions("bleh", "okay", "not good" )## calls the add options function

q1 = Q("question1")
q1.addquestions("Who is Iron Man?")
q1.addcorrect(1, "Tony Stark")
q1.addoptions("Bruce Banner", "Peter Parker", "Steve Rogers")

q2 = Q("question2")
q2.addquestions("Who is the Ghostbuster who has glasses?")
q2.addcorrect(1, "Egon Spengler")
q2.addoptions("Winston Zeddemore", "Peter Venkmen", "Ray Stanz")

q3 = Q("question3")
q3.addquestions("Who played the 11th Doctor on Doctor Who?")
q3.addcorrect("Matt Smith")
q3.addoptions("Peter Capaldi", "Jodie Whittaker", "David Tennant")

q4 = Q("question4")
q4.addquestions("What is the subtitle for the 8th Star Wars film?")
q4.addcorrect("The Last Jedi")
q4.addoptions("The Force Awakens", "Attack of the Clones", "A New Hope")

q5 = Q("question5")
q5.addquestions("What is the name of Doc Brown's dog in 1955?")
q5.addcorrect("Copernicus")
q5.addoptions("Einstein", "Newton", "Oppenheimer")

q6 = Q("question6")
q6.addquestions("What is first name of Kramer in Seinfeld?")
q6.addcorrect("Cosmo")
q6.addoptions("George", "Jerry", "Newman")

q7 = Q("question7")
q7.addquestions("How many rings were orignially forged in Lord of the Rings?")
q7.addcorrect("20")
q7.addoptions("9", "7", "3")

q8 = Q("question8")
q8.addquestions("Who sings the popular song 'All-Star' from Shrek?")
q8.addcorrect("Smashmouth")
q8.addoptions("Black Sabbath", "AC/DC", "Van Halen")

q9 = Q("question9")
q9.addquestions("What is the name of the fictional country in Black Panther?")
q9.addcorrect("Wakanda")
q9.addoptions("Wyoming", "Ontario", "South Korea")

q10 = Q("question10")
q10.addquestions("What is Buzz Lightyear's catchphrase?")
q10.addcorrect("To infinity and beyond!")
q10.addoptions("This really is a Toy Story", "What's the deal with toys?", "Buzz")
