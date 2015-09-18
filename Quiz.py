#In this game i will ask each question and IF they get the answer correct
#then i will add one to the value 'x'



print ("Welcome to the Quiz")

restart = True
while restart: 

    x = 0

    Answer1 = input("What is the capital of france?   ")
    if Answer1 == "Paris":
        print ("Correct")
        x=x+1

    else: print ("Incorrect")

    Answer2 = int(input("What is the sum of 5674 + 9880?   "))
    if Answer2 == (5674+9880):
        print ("Correct")
        x=x+1

    else: print ("Incorrect")

    Answer3 = int(input("What is 5674 - 9880?   "))
    if Answer3 == (5674-9880):
        print ("Correct")
        x=x+1

    else: print("Incorrect")

    Answer4 = int(input("what is 5674 times by 9880?   "))
    if Answer4 == 5674*9880:
        print ("Correct")
        x=x+1

    else: print("Incorrect")

    Answer5 = int(input("What is 5674 divided by 9?   "))
    if Answer5 == (5674/9) or Answer5 == 630:
        print ("Correct")
        x=x+1

    else: print ("Incorrect")

    Answer6 = int(input("What is the remainder integer of 5674 divided by 9?   "))
    if Answer6 == 3 or Answer6 == 4:
        print ("Correct")
        x=x+1

    else: print ("Incorrect")

    Answer7 = input("What was the year the first Doctor Who episode was aired on TV?   ")
    if Answer7 == 1963:
        print ("Correct")
        x=x+1

    else: print ("Incorrect")

    print ("Your final score is",x, "out of 7")

    restart = input("Would you like to continue? (yes/no)  ")
    
    if restart == 'yes':
            restart = True
           
    else: print ("Thank you for using the programm")
    


