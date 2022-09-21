# Define a list
basket = ["orange", "apple", "banana", "mango", "grapes", "mango"]
def less_than_6(my_list):
    for item in my_list:
        if len(item) < 6:
            print(item)
output = []
basket.append('watermelon')
basket.pop(0)


less_than_6(basket)
   
print(basket)
print('We found {} items'.format(len(output)))

"""
Assignment
Create a function with two lists
Lists of students names(6)
Lists of student grades (6)
Your function should return the name of the student with highest grade
    
"""

    
            
        
        