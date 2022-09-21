#print(input('Enter your name:'))
# name = 'Robert Korir'
# print(f'my name is {name}')
#How to write a multi-line comments in python

"""
  kkkkkkkkk  
"""

'''
kkkkkkkkkkk
'''
#Create a variable named var and assign the value 123
# var = 123
# var2 = 256
# var = float(123)
# var2 = float(256)
# print(var)
# print(var2)

#programming tasks
#Write a function that calculates the area of a rectangle based on the given sides a, b.
#
  
#Write a function that gets the sides a and b of a rectangle from the user and
#then calculates the perimeter of the rectangle.
# def perimeter_of_Rectangle(length, width):
#     return 2 * (length + width)

# length = (input('Please Enter the Length of a Triangle: '))
# width = (input('Please Enter the Width of a Triangle: '))

# # calculate the perimeter
# perimeter = perimeter_of_Rectangle(length, width)
# print("Perimeter of a Rectangle using", length, "and", width, " = ", perimeter)
#Write a function that calculates the average of the elements in a list.
# def average(num):
#     sum_num = 0
#     for t in num:
#         sum_num = sum_num + t           

#     avg = sum_num / len(num)
#     return avg

# print("The average is", average([2,3,4,5,10]))

#Write a function that counts the occurrences of "6" number in a list.
# def countX(lst, x):
#     return lst.count(x)
 
 
# # Count the number of occurance on list
# list = [8, 6, 6, 10, 6, 20, 10, 6, 6]
# x = 6
# print('{} has occurred {} times'.format(x,countX(list, x)))
##Write a function that counts the occurrences of "6" number in a list.
# e_list =[1,2,3,4,5,6,7,89,10]
# e_tuple = (1,2,3,4,5,6,7,8,9,10)
# count = 0
# sum = 0
# for x in e_list:
#     count += 1
#     sum +=x
#     print(sum/count)
#     print()
"""Write a function whose input is an operator and two operands. The function
performs the specified operation on the operands.
"""
# from unittest import result


# def calculate(num1,num2,sign):
#     if sign == "+":
#         return num1 + num2
#     elif sign == "-":
#         return num1 - num2
#     elif sign == "*":
#         return num1 * num2 #multiplication
#     elif sign == "**":
#         return num1 ** num2 #powers
#     elif sign == "/" or sign == ":":
#         return float(num1) / float(num2) #division
#     elif sign == "%":
#         return num1 % num2
#     else:
#         raise Exception('Invalid operator in use') # handling invalid signs
# operator = input('Kindly input your operator:')
# result = calculate(20,30,40)
# print(f'your operator is:({operator}')

# def calculator():
# #match operator:
#     operator = input('Kindly input your operator:')
#     operator1 = input('Kindly input the first value:')
#     operator2 = input('Kindly input the second  value:')
#     return eval( operator1+ operator + operator2)
# operator = calculator()
# print(f'The result is {operator}')

"""
TOPIC FILES
"""
#Create a variable called text with the value “Hello World! Hello everyone!”. This is the string that we will use in the next few tasks.

# var = 'Hello World! Hello everyone!'
# #Print out the 3rd character in it, the one before the last one, using negative indexing to get it, then print out the one that has the highest ASCII value.
# print(var[3])
# print(var[-2])
# print(max(var))
# print(var[:2])
# #Print out a slice of the string, starting from the 2nd character and ending on the 5th.
# print(var[2:5])
# print(len(var[::3]))
# print(len(var[10:2:-2]))
# print(len(var[2:10:-2]))

"""
Check if the string contains the character which has the ASCII value of 72, then convert the result to string and print it out twice, using the multiplication of strings.
"""
# print(str(chr(72) in var(*2)))
# for x in var:
#   if ord(x) == 72:
#     print(x)
#Print out the ASCII code for every character of the string, that is larger than the average.
# Input: str =  "Hello World"
# print(var)

# # Function to find average
# sum = 0
# for ch in var:
# 		sum += ord(ch)
# average = sum/ len(var)

# print("Average is " + str(average))
"""
Write a function, that reads in the file data.txt and writes it to the standard output backwards. 
Do it both with string operations and indexing. While working with files, apply basic error-handling. 
Write another function, that reads the contents of the file and writes it to the standard output.
"""
# try:
#   f = open("data.txt" , "w")
# except:
#   print("couldn't open the file")
# exit()
#   finally:
#   print("OK")
#   name = input("What's your name? ")
#   neptune = input("What's your Neptune Code? ")
#   f.write(neptune)
#   f.close()
# def readFile():
#   f = open("data.text", "r")
#   ch = f.read(5)
#   f.close
#   print(ch)
#   readFile()
"""
Write a function, that reads in names from a file called people.txt, 
then writes them into people_organised.txt in ABC order.
While working with files, apply basic error-handling.
"""
# try:
#     f = open("people.txt", "r")
# except:
#   print("Error opening file!")
#   exit()
# text = f.read()
# print(text[::-1])
#Files 3
"""
Write a function, that takes the names from people.txt 
and saves the ones that start with S into a file called people_s.txt. 
While working with files, apply basic error-handling.
"""
# import string

# def read_people():
# try:
#   f = open("people.txt", "r")
# final_string = ''
# f.seek(0, 2)
# position = != 0:
# position = f.tell()
# while position != 0:
#     final_string+= f.read(1)
# position -= 1
# f.seek(position)
# print(final_string)


#Lists
"""
Write a function, that takes the forenames and stores them in a list. 
Write to the standard output, how many times each name occurred. 
While working with files, apply basic error-handling.
"""
# def writefile(fileName, items)
# try:
# f = open("people.text", "r")
# except:
#        print("Error opening file!")
#        exit()
#        people = f.readlines()    
#        f.close()
#        try:
#          f = open("people_ordered.txt", "w")   
#        except:
#          print("Error opening file!")
#          exit()
"""
Write a function, that reads the file data.txt and replaces the commas with tabs.
While working with files, apply basic error-handling.

"""


# try:
#   def createStation(Station name, Time, Air pressure, Humidity, UV index, Wind velocity, Wind direction):
#     f = open("data.txt", "r")
# except:
#   print("Error")
#   exit()
# while True:
#     humidity, temperature = (temperature)
#     if humidity is not None and temperature is not None:
#         print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
      
#         temperature = '%.2f'%(temperature)
#         humidity = '%.2f'%(humidity)
    
#     else:
#         print('Failed to get Reading, trying again in ', 'seconds')
  
  
  

  
    
"""
There are several stations, that provide measurements from their environment. These measurements are stored in a file, called measurements.txt in the following format:
Station name, Time, Air pressure, Humidity, UV index, Wind velocity, Wind direction
Each one of these values have a possible minimum and maximum values, but the stations can provide incorrect data.
Air pressure must be between 90.00 and 150.00 kPa.
Humidity must be between 0 and 100%.
UV index must be between 0 and 11.
Wind velocity must be between 0 and 410 km/h.
Wind direction could be any of the 4 cardinal directions, and the 4 in-between directions. (N, S, W, E, NW, NE, SW, SE)
Write a function, that can create a new e, conaining a filtt of th data, where the user an specify he name of the statwhich will have it’s data stred.
Write a unction,at can filtrout incorrect and calculate the arage of the correct oes,for echf the measurement points.

"""
def get_measurements():
    try:
        measurements_file = open('measurements.txt', 'r')
        measurements = measurements_file.readlines()
        return measurements
    except:
        print('Error')


def save_correct_data():
    # t2 = datetime.datetime.strptime("2022-09-12 15:13:06", "%Y-%m-%d %H:%M:%S")
    station = input('Enter station: ')
    measurements = get_measurements()
    measurements = list(filter(lambda measurement_to_filter: measurement_to_filter.startswith(station), measurements))
    for item in measurements:
        print(item, end="")
    print()
    # times = []
    readings = {
        'Air Pressure': [],
        'Humidity': [],
        'UV Indexes': [],
        'Wind Velocities': []
    }
    for measurement in measurements:
        actual_measurements = measurement.split(', ')
        air_pressure = float(actual_measurements[2])
        humidity = float(actual_measurements[3])
        uv_index = float(actual_measurements[4])
        wind_velocity = float(actual_measurements[5])
        if 90 < air_pressure < 150:
            readings['Air Pressure'].append(air_pressure)
        if 0 < humidity < 100:
            readings['Humidity'].append(humidity)
        if 0 < uv_index < 11:
            readings['UV Indexes'].append(uv_index)
        if 0 < wind_velocity < 410:
            readings['Wind Velocities'].append(wind_velocity)

    # print(readings)
    for reading, values in readings.items():
        print(f'Average {reading}: {sum(values) / len(values)}')

save_correct_data()
  


               
                                
                                
