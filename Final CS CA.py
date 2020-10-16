print("Welcome to the quiz" + '\n')

FirstName = input("Please enter your FirstName: ")
SurName = input ("Please enter your SurName: ")
Age = input("Please enter your Age: ")
UserName1 =(FirstName[0:3]+Age)
Group = input("Please enter your year group: ")
print("Welcome your username is " + UserName1 + "\n")

password1 = input("Please create a password: ")
password2 = input("Please re enter your password: ")
while password1 != password2:
    print("Passwords do not match, please re-enter both")
    password1 = input("Please create a password: ")
    password2 = input("Please re-enter your password: ")
if password1 == password2:
        print("Welcome, " + UserName1 + "\n")










Quiz = input ("Which Computer Science quiz level would you like to choose? \
Easy, Medium or Hard\n")
score = 0
if Quiz == "Easy":
    print ("Ok, here is the Computer Science Easy question sheet")
    print ("Scroll down to answer the questions")
    print("\n")
    f = open("Computer Science quiz easy.txt","r")
    print(f.read(1))
    print(f.read())
    print("\n")

    CSQUIZEASY1 = input('Please answer Q1: \n')
    if CSQUIZEASY1 == "a":
        print ("Correct")
        score = score + 1
    else:
        print ("Wrong")

    CSQUIZEASY2 = input ("Please answer Q2: \n")
    if CSQUIZEASY2 == "b":
        print ("Correct")
        score = score + 1
    else:
        print ("Wrong")

    CSQUIZEASY3 = input  ("Please answer Q3: \n")
    if CSQUIZEASY3 == "b":
        print ("Correct")
        score = score + 1
    else:
        print ("Wrong")

    CSQUIZEASY4 = input ("Please answer Q4: \n")
    if CSQUIZEASY4 == "b":
        print ("Correct")
        score = score + 1
    else:
        print ("Wrong")

    CSQUIZEASY5 = input ("Please answer Q5: \n")
    if CSQUIZEASY5 == "b":
        print ("Correct")
        score = score + 1
    else:
        print ("Wrong")

    print ("Your score is: " + str(score))
    efficiency = score/5*100
    print('your efficiency is:' + str(efficiency)+ '%')

if Quiz == "Medium":
    print ("OK ,here is the Computer science Medium Question sheet")
    print ("Scroll down to answer the questions")
    print("\n")
    f = open("Computer Science quiz medium.txt","r")
    print(f.read(1))
    print(f.read())
    print("\n")

    CSQUIZMEDIUM1 = input ("Please answer Q1: \n")
    if CSQUIZMEDIUM1 == "b":
        print ("Correct")
        score = score + 1
    else:
        print ("Wrong")

    CSQUIZMEDIUM2 = input ("Please answer Q2: \n")
    if CSQUIZMEDIUM2 == "a":
        print ("Correct")
        score = score + 1
    else:
        print ("Wrong")

    CSQUIZMEDIUM3 = input ("Please answer Q3: \n")
    if CSQUIZMEDIUM3 == "c":
        print ("Correct")
        score = score + 1
    else:
        print ("Wrong")

    CSQUIZMEDIUM4 = input ("Please answer Q4: \n")
    if CSQUIZMEDIUM4 == "a":
        print ("Correct")
        score = score + 1
    else:
        print ("Wrong")

    CSQUIZMEDIUM5 = input ("Please answer Q5: \n")
    if CSQUIZMEDIUM5 == "c":
        print ("Correct")
        score = score + 1
    else:
        print ("Wrong")

    print ("Your score is: " + str(score))
    efficiency = score/5*100
    print('your efficiency is:' + str(efficiency)+ '%')

if Quiz == "Hard":
    print ("OK ,here is the Computer science Hard Question sheet")
    print ("Scroll down to answer the questions")
    print("\n")
    f = open("Computer Science quiz hard.txt","r")
    print(f.read(1))
    print(f.read())
    print("\n")

    CSQUIZHARD1 = input ("Please enter Q1: \n")
    if CSQUIZHARD1 == "d":
        print ("Correct")
        score = score + 1
    else:
        print ("Wrong")

    CSQUIZHARD2 = input ("Please enter Q2: \n")
    if CSQUIZHARD2 == "d":
        print ("Correct")
        score = score + 1
    else:
        print ("Wrong")

    CSQUIZHARD3 = input ("Please enter Q3: \n")
    if CSQUIZHARD3 == "a":
        print ("Correct")
        score = score + 1
    else:
        print ("Wrong")

    CSQUIZHARD4 = input ("Please enter Q4: \n")
    if CSQUIZHARD4 == "d":
        print ("Correct")
        score = score + 1
    else:
        print ("Wrong")

    CSQUIZHARD5 = input ("Please enter Q5: \n")
    if CSQUIZHARD5 == "c":
        print ("Correct")
        score = score + 1
    else:
        print ("Wrong")

    print ("Your score is: " + str(score))
    efficiency = score/5*100
    print('your efficiency is:' + str(efficiency)+ '%')

    



text_file = open("Student_details.txt", "a+")
text_file.write("Student name: " + FirstName + (" ") + SurName +'\n')
text_file.write("Student age: " + Age + '\n')
text_file.write("Student year group: " + Group + '\n')
text_file.write("Student username: " + UserName1 + '\n')
text_file.write("Student's password: " + password2 + '\n')
text_file.write("Quiz taken by student: " + Quiz + '\n')
text_file.write("Score for quiz taken: " + score + '\n')
text_file.write("Efficiency for the quiz taken: " + efficiency + '\n')
text_file.write("\n")
text_file.write("\n") 
text_file.close()

























    
