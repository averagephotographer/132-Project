q1 = Q("Question1")
q2 = Q("Question2")
q3 = Q("Question3")
q4 = Q("Question4")
q5 = Q("Question5")
q6 = Q("Question6")
q7 = Q("Question7")
q8 = Q("Question8")
q9 = Q("Question9")

q1.addquestions("What is the gravity constant on earth?")
q1.addcorrect(9.81)
q1.addoptions(9.1, 9.3, 8.5)

q2.addquestions("What is the biggest city in the United States?")
q2.addcorrect("New York")
q2.addoptions("Los Angeles", "Chicago", "Miami")

q3.addquestions("What is SIN(30)?")
q3.addcorrect(0.5)
q3.addoptions(1.5, 0.6, 0.525)

q4.addquestions("What is the derivative of SIN(X)?")
q4.addcorrect("COS(X)")
q4.addoptions("-SIN(X)", "-COS(X)", "TAN(X)")

q5.addquestions("Most Populated Country in the World?")
q5.addcorrect("China")
q5.addoptions("India", "United States", "Indonesia")

q6.addquestions("What is the Largest Continent in the World?")
q6.addcorrect("Asia")
q6.addoptions("Africa", "Europe", "South America")

q7.addquestions("Who killed the night watchman in Game of Thrones?")
q7.addcorrect("Arya")
q7.addoptions("Jon", "Sansa", "Jamie")

q8.addquestions("Who killed James St.Patrick in Power?")
q8.addcorrect("Tariq")
q8.addoptions("Tasha", "Tommy", "Kanan")

q9.addquestions("What is the equation for calculating the voltage of a circuit?")
q9.addcorrect("V = IR")
q9.addoptions("V = I/R", "V = R/I", "V = CR")