import time
import sys
import random
import operator
total_score2 = 0
total_score1 = 0
rounds = 0
playerOnePoints = 0
playerTwoPoints = 0
counter = 0

print("*****************Welcome To The DICE Game*******************")
print("Please enter 'n' if you are a new user and 'e' if you are a exsiting user and enter 's' to display scores")
ens=input("")
while ens not in ('e', 'n', 's'): # if anything else but these characters are entered it will loop until it is correct
    print("Please enter 'n' if you are a new user and 'e' if you are a exsiting user and enter 's' to display scores")
    ens = input()

if ens == "s":
    s = open("scores.txt","r")
    file_content = s.read().splitlines()
    users_points = {i.split()[0]: int(i.split()[2]) for i in file_content}
    best_player = max(users_points.items(), key=operator.itemgetter(1))[0]
    print("LeaderBoard: ")
    print("\n")
    print('player with maximum points is {}, this player has {} points'.format(best_player, users_points[best_player]))
    best_players = sorted(users_points, key=users_points.get, reverse=True)
    for bp in best_players:
        print('{} has {} points'.format(bp, users_points[bp])) # This prints all players scores
    print("\n")
    print("Please enter 'n' if you are a new user and 'e' if you are a exsiting user and enter 's' to display scores")
    ens=input("")

if ens == "n":
    file = open("accountfile.txt","r+")
    text = file.read().strip().split()
    check = True
    while check:
        username=input("Please enter appropiate username: ") #Takes input of a username from user
        if username == "": #if no value is entered for the username
            continue
        if username in text: #username in present in the text file
            print("Username is taken please try another one")
        else: #username is absent in the text file
            print("Username has been accepted")
            check = False
            check = True
            # while check:
            #     password1=input("Please enter password: ")
            #     password2=input("Please re-enter password: ")
            #     if password1 == password2:
            #         if password2 in text:
            #             print("Password has been taken please try another one")
            #         else:
            #             print("Username and Password have sucessfully been made Thankyou")
            #             file.write("username: " + username + " " + "password: " + password2 + "\n")
            #             file.close()
            #             check = False
            #     else:
            #         print("passwords do not match please try again")                         
#     file.close()

# def write1():
#     print("Player 1 ",username1," Wins!")
#     file = open("scores.txt","a")
#     file.write(username1 + " has " + str(total_score1) + " points" + "\n")
#     file.close()
#     sys.exit()
# def write2():
#     print("Player 2 ",username2," Wins!")
#     file = open("scores.txt","a")
#     file.write(username2 + " has " + str(total_score2) + " points" + "\n")
#     file.close()
#     sys.exit()
# def validation():
#     global counter
#     print("Sorry, this username or password does not exist please try again")
#     counter = counter + 1
#     if counter == 3:
#         print("----------------------------------------------------")
#         print("You have been locked out please restart to try again")
#         sys.exit()
def game():
    global total_score1
    global total_score2
    global rounds
    global number
    global number2
    global playerOnePoints
    global playerTwoPoints
    total_score2 = total_score2 + playerTwoPoints
    total_score1 = total_score1 + playerOnePoints
    rounds = rounds + 1
    number = random.randint(1,6)
    number2 = random.randint(1,6)
    playerOnePoints = number + number2
    print("-------------------------------------------")
    print("Round",rounds)
    print("-------------------------------------------")
    print("Player 1's turn    Type 'roll' to roll the dice")
    userOneInput = input(">>> ")
    if userOneInput == "roll":
        time.sleep(1)
        print("Player 1's first roll is", number)
    print("Player 1's second roll    Type 'roll' to roll the dice")
    userOneInput = input(">>> ")
    if userOneInput == "roll":
        time.sleep(1)
        print("player 1's second roll is", number2)
    if playerOnePoints % 2 == 0:
        playerOnePoints = playerOnePoints + 10
        print("Player 1's total is even so + 10 points")
        print("-------------------------------------------")
        print("Player 1 has",playerOnePoints, "points")
    else:
        playerOnePoints = playerOnePoints - 5
        print("player 1's total is odd so -5 points")
        print("-------------------------------------------")
        print("Player 1 has",playerOnePoints, "points")
    number = random.randint(1,6)
    number2 = random.randint(1,6)
    playerTwoPoints = number + number2
    print("-------------------------------------------")
    print("Player 2's turn    Type 'roll' to roll the dice")
    userTwoInput = input(">>> ")
    if userTwoInput == "roll":
        time.sleep(1)
        print("Player 2's first roll is", number)
    print("Player 2's second roll    Type 'roll' to roll the dice")
    userTwoInput = input(">>> ")
    if userTwoInput == "roll":
        time.sleep(1)
        print("player 2's second roll is", number2)
    if playerTwoPoints % 2 == 0:
        playerTwoPoints = playerTwoPoints + 10
        print("Player 2's total is even so + 10 points")
        print("-------------------------------------------")
        print("Player 2 has",playerTwoPoints, "points")
    else:
        playerTwoPoints = playerTwoPoints - 5
        print("player 2's total is odd so -5 points")
        print("-------------------------------------------")
        print("Player 2 has",playerTwoPoints, "points")

if ens == "e":
    counter = 0 
    check_failed = True
    while check_failed:
        print("Could player 1 enter their username and password")
        username1=input("Please enter your username ")
        password=input("Please enter your password ")
        with open("accountfile.txt","r") as username_finder:
            for line in username_finder:
                if ("username: " + username1 + " password: " + password) == line.strip(): 
                    print("you are logged in")
                    check_failed = False
                    check_failed = True
                    while check_failed:
                        print("Could player 2 enter their username and password")
                        username2=input("Please enter your username ")
                        password=input("Please enter your password ")
                        with open("accountfile.txt","r") as username_finder:
                            for line in username_finder:
                                if ("username: " + username2 + " password: " + password) == line.strip():
                                    print("you are logged in")
                                    check_failed = False
                                    time.sleep(1)
                                    print("Welcome to the dice game")
                                    time.sleep(1)
                                    while rounds < 5:
                                        game()
                                    print("-------------------------------------------")
                                    print("Total score for player 1 is", total_score1)
                                    print("-------------------------------------------")
                                    print("Total score for player 2 is", total_score2)
                                    print("-------------------------------------------")
                                    # if total_score1 > total_score2:
            #                             write1()
            #                         if total_score2 > total_score1:
            #                             write2()
            #                         if total_score1 == total_score2:
            #                             print("Its a draw!")
            #                             game()
            #                             if total_score1 > total_score2:
            #                                 write1()
            #                             if total_score1 < total_score2:
            #                                 write2()
            #                 else:
            #                     validation()

            # else:
            #     validation()      