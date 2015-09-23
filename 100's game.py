restart = True
while restart:


    player1 = input("What is Player One's name?   ")

    player2 = input("What is Player Two's name?   ")

    print ("Hello ",player1," and " ,player2,)
    print ("To play this game you need to input a number between 10 and 0, if you don't"
           "     follow this one rule you'll miss your turn")

    restart2 = True
    while restart2:

        x=0



        replay = True
        while replay:
            

                    answer1 = int(input(player1+ " input a positive number   "))
                    if 0< answer1 <10:
                        x = x+answer1
                        if x >= 100:
                                print (player1, " wins!")
                                answer = input("Would you like to play again?   (yes/no)   ")
                                if answer == 'yes':
                                    answer2 = input("Are "+ player1+ " and "+ player2+" still playing?   (yes/no)   ")
                                    if answer2 == 'yes':
                                        restart2 = True
                                        break
                                    else:
                                        restart = True
                                        break
                                else: print ("Okay")
                        else: print ("the number is" ,x,)
                    else: print ("Please only input numbers betweeb 0 and 10" , player1,)
                    answer2 = int(input(player2 +" input a positive number   "))
                    if 0< answer2 <10:
                        x = x+answer2
                        if x >= 100:
                            print (player2, " wins!")

                            answer = input("Would you like to play again?   (yes/no)   ")
                            if answer == 'yes':
                                answer2 = input("Are "+ player1+ " and "+ player2+" still playing?   (yes/no)   ")
                                if answer2 == 'yes':
                                    restart2 = True
                                    break
                                else: restart = True
                                break
                            else: print ("Okay")
                        else: print ("the number is" ,x,)

                    else: print ("Please only input numbers betweeb 0 and 10" , player2,)

                    replay = True
                
                              


