# *1) Use the print statement
# print("Hello World\n")
# print()
# print("My Name Is Korir Robert")
# *2) Use python as a calculator

'''
# Addition
# Subtraction
# Multiplication
# Division
# Modulas
# Quotient
# '''
#
# print("Addition: " ,10+56) #Addition
# print("Subtraction: ", 78-99)#Subtraction
# print("Multiplication: ", 78*99)#Multiplication
# print("Division: ", 100/100)#Division
# print("Quotient" ,47//5)#Quotient
# print("Remainder" ,47%5)#Remainder
# print("Multiplication: ", 9**2)#Power of or 9squared
#
# print("My name is %s. My age is %s. " %("Robert", 50))#Using multiple placeholders
# print('70%% - 20%% is:  %s'%(70-20))#Printing % sign
# print("{}%".format(70-20))#Using format function
# print(f'{0.7-0.2:.0%}')#using format dtring
#
# #Assigning variables and use inputs
# a=30
# b='Robert'
# c=5
# a
# d='is cool'
# e= a+c
# print(c*a)
# print(a)
# print(e)

# name = input("Enter your name:")
# print('welcome {}'.format(name))




#
# a=12
# b=44
# print(a, b) [a>b]))

#Assignment
'''
Write a program that does the following:
1. Asks the user to enter a number  "x"
2. Asks the user to enter a number "y"
3. Prints out number "x" raised to the power of "y"
4. Prints out the log (base 2) of "x"
'''
# import math

#Python code with bonus points
# from math import log2


# x =2
# y =4
# x = int(input("Enter number x:"))
# y = int(input("Enter number y:"))
# print(pow(x,y))
# log_x = log2(x)
# print("log (base2) of "x" is :", log x)
# print("The solution to x raised to power y is:(x**y")


#log_b(a) = log(a)/log(b)
# def power(x,y):
#     res=0
#     for i in range(e):
#         res *= x
#     return res
# print(pow(x,y))

# def solve(a,b):
#     return b if a == 0 \
#     else solve(b % a, a)
# print(solve(20, 50))

# x, y = 67, 80

# x, y, z= 1, 2, 3

# print(x, y, z)
# output = math.log2(x)
# print(output)
# list1 = [11, 2, 23]

# list2 = [2, 11, 23]
#
#
# print(list1 == list2)

# from random import sample
#
# def auto_pick():
#     pick = sample(range(1,43),6)
#     return pick
#
# def compare_pick(pick_1, pick_2):
#     n = 0
#     for num in pick_1:
#         if num in pick_2:
#             n +=1
#             return n
#
# def main():
#     user_pick = []
#     counter = 0
#     user_input = int(input("Enter a number(1 to 42): "))
#     user_pick.append(user_input)
#     counter +=1
#     while counter !=6:
#         user_input = int(input("Enter another number (1 to 42):"))
#     if user_input in user_pick:
#      print("Number should not be repeated. Try again.")
#     else:
#         user_pick.append(user_input)
#     counter +=1
#     print(user_input)
#
#
# if __name__ == '__main__':
#     main()

#01/07/2022

"""
Grading system

Create a single function that takes in inputs of distance and speed and return the time taken in hours and speed
########## Excercise 2: Distance Calculation ################
Consider three vehicles traveling to different locations. Details of there journey 
is given below:

Car A - 118KM : 89KM/H
Car B - 75Miles : 90KM/H
Car C - 50KM : 40Miles/HR

Which vehicle arrived at its destination last?

Required:
Create a single function that takes in inputs of distance and speed
and return the time take in hours and minutes.

HINT: Your function should consider the units of the input

"""
# average_speed = int(input('Average speed: ')) 
# distance = int(input('Total distance: ')) 
# hours = int(input('KM/HR: ')) 
# t = int(input('time'))


# print(f'{average_speed} km/h') 
# print(f'{distance} km') 
# print(str(t + 1) + ':' + str(distance))



# def calc_speed(): 
#     speed = distance / hours 
#     print(f'your total speed id {speed}km/h')

# def calc_distance(): # 11
#    distance = average_speed * hours # 12
#    print(f'total distance is {distance} km')

# def calc_time():
#     time = distance / average_speed
#     print(f'your total time is {time} hr')

# meter=input( 
# '''speed1(s)
# time(t)
# distance(d):''' 
# )
# if meter == 's': 
#     calc_speed() 
# elif meter == 't': 
#     calc_time()
# elif meter == 'd': 
#     calc_distance()
"""
python code to create a lambda function that takes in the amount, period and interest rate and returns the future amount after the period
    
"""
# fv = lambda amount, period, interest: amount*(1+interest)**period
# fv_output = fv(100,2,1.2)
# print(fv_output)

#22/07/2022
#
#print(ord('foo'))
print(
   list((b'abcde' + 'fghi')[3:6])
)








