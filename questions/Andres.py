# format for questions:
    # q1 = Q("question1")
    # q1.addquestions("How are you?") ## calls the add questions function
    # q1.addcorrect(1, "good")
    # q1.addoptions("bleh", "okay", "not good" )## calls the add options function

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

q21.addquestions("Who is Iron Man?")
q21.addcorrect(1, "Tony Stark")
q21.addoptions("Bruce Banner", "Peter Parker", "Steve Rogers")

q22.addquestions("Who is the Ghostbuster who has glasses?")
q22.addcorrect(1, "Egon Spengler")
q22.addoptions("Winston Zeddemore", "Peter Venkmen", "Ray Stanz")

q23.addquestions("Who played the 11th Doctor on Doctor Who?")
q23.addcorrect("Matt Smith")
q23.addoptions("Peter Capaldi", "Jodie Whittaker", "David Tennant")

q24.addquestions("What is the subtitle for the 8th Star Wars film?")
q24.addcorrect("The Last Jedi")
q24.addoptions("The Force Awakens", "Attack of the Clones", "A New Hope")

q25.addquestions("What is the name of Doc Brown's dog in 1955?")
q25.addcorrect("Copernicus")
q25.addoptions("Einstein", "Newton", "Oppenheimer")

q26.addquestions("What is first name of Kramer in Seinfeld?")
q26.addcorrect("Cosmo")
q26.addoptions("George", "Jerry", "Newman")

q27.addquestions("How many rings were orignially forged in Lord of the Rings?")
q27.addcorrect("20")
q27.addoptions("9", "7", "3")

q28.addquestions("Who sings the popular song 'All-Star' from Shrek?")
q28.addcorrect("Smashmouth")
q28.addoptions("Black Sabbath", "AC/DC", "Van Halen")

q29.addquestions("What is the name of the fictional country in Black Panther?")
q29.addcorrect("Wakanda")
q29.addoptions("Wyoming", "Ontario", "South Korea")

q30.addquestions("What is Buzz Lightyear's catchphrase?")
q30.addcorrect("To infinity and beyond!")
q30.addoptions("This really is a Toy Story", "What's the deal with toys?", "Buzz")
