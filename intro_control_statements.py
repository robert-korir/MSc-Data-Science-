# write a program that prevents users from entering non-integer values
# x = input("Enter your age:")
# while type(x) is not int:
#     print("Kindly enter an integer") 
#     print(x)
#While loop
# while True:
#     try:
#         x = int(input("Enter a value for x: "))
#         y = int(input("Enter a value for y: "))
#         break
#     except:
#         print("That is not a valid option!")

# print("your answer is correct")
#How to make sure the user enters a number (integer) - www.101computing.net

# def inputNumber(message):
#   while True:
#     try:
#        userInput = int(input(message))       
#     except ValueError:
#        print("Not an integer! Try again.")
#        continue
#     else:
#        return userInput 
#        break 
     

# #MAIN PROGRAM STARTS HERE:
# age = inputNumber("How old are you?")

# if (age>=18):
#   print("You are old enough to vote.")
# else:
#   print("You will be able to vote in " + str(18-age) + " year(s).")
#While loop using break
# count = 0
# while count < 5:
#     count = count +1
#     print("You are at :", count)
#     if count == 3:
#             break

#Age
# age = input("Enter your age:")
# if age < 18:
#     if 12 <age <18:
#         print("You get a 5%% discount")
#     elif age < 12:
#      else:
#           print("You are too old for a discount. Sorry!!!")


  

"""
Grading system
Ask the user to input the marks received
Print the grade of the input given by the user
A = 81
A- = 74-80
B+ = 67-73
B =  60-65
B- = 44-59
C =  37-43
C- =  26-36
Fail < 20

"""
# print("Enter Marks Obtained in 7 Subjects: ")
# A = int(input())
# A- = int(input())
# B+ = int(input())
# B = int(input())
# B- = int(input())
# C = int(input())
# C- = int(input())
# Fail<C

# tot = A+A-+B++B+C+C-+C+Fail
# avg = tot/5

# if mark>=80 and mark<=100:
#     print("Your Grade is A")
# elif avg>=81 and avg<91:
#     print("Your Grade is A2")
# elif avg>=71 and avg<81:
#     print("Your Grade is B1")
# elif avg>=61 and avg<71:
#     print("Your Grade is B2")
# elif avg>=51 and avg<61:
#     print("Your Grade is C1")
# elif avg>=41 and avg<51:
#     print("Your Grade is C2")
# elif avg>=33 and avg<41:
#     print("Your Grade is D")
# elif avg>=21 and avg<33:
#     print("Your Grade is E1")
# elif avg>=0 and avg<21:
#     print("Pass")
# else:
#     print("Fail!")

while True:
    try:
        marks = int(input("Marks: "))
        if 0 < marks >= 100:
            print('Enter 1 - 100')
            continue
        else: 
            if marks >= 81:
                print('You got A')
            else:
                print("Fail")
        break
    except:
        print("Kindly enter int")

""""
      PART B:
      Ensure the input is an int. Ask the user to re-enter if not.
      Ensure the input is between 0 and 100. Ask to input the marks again if not.

"""
   #Grading system
# print("Enter Marks Obtained in 5 Subjects: ")
# markOne = int(input())
# markTwo = int(input())
# markThree = int(input())
# markFour = int(input())
# markFive = int(input())

# tot = markOne+markTwo+markThree+markFour+markFive
# avg = tot

# if avg>=80 and avg<=100:
#         print("Your Grade is A")
# elif avg>=73 and avg<80:
#         print("Your Grade is A-")
# elif avg>=74 and avg<80:
#         print("Your Grade is B")
# elif avg>=67 and avg<73:
#         print("Your Grade is B-")
# elif avg>=60 and avg<65:
#         print("Your Grade is C")
# elif avg>=44 and avg<50:
#         print("Your Grade is C-")
# elif avg<30:
#     print("Fail")

# else:
#      print("Invalid Input!")

