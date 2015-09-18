restartp = True
while restartp:

    x = 0
    y = 0

    restart = True
    while restart:
        
        Answer = input("Input a number   ")

        if Answer.isdigit():

            Answer = int(Answer)
                     
            if Answer>0:
                x=x+1
                restart = True

            if Answer<0:
                y=y+1
                restart = True

            if Answer == -999:
                print ("You prodcued", x , "numbers higher than zero and", y , "numbers smaller than zero")
                restartp = input("Do you want to start again?  (yes/no)   ")

                if restartp == 'yes':
                    restartp = True

                else: print("Thank you for using the programm   ")
                
        else: print("Please only input numbers   ")
        restart = True
                

        

