
"""
NAME: KORIR ROBERT KIPNGENO
STUDENT ID: 148989
STATEMENT OF WORK: I followed youtube tutorials on python and class work exercises given.


"""

import random
from random import randint
import datetime
from prettytable import PrettyTable


# # Kinldy note that the print() method is used for debugging purposes in this system 
# # Create a txt file by the name output.txt and append to the text file on every output
# f = open('output.txt','w')

def ask_user_their_balance():
    # current_balance = input("Kindly input your current balance : ") # must be less than or equal to 400
    purchase_lottery = (f" Your Current balance is : ksh. {current_balance}, would you like to purchase a lottery ticket ? (answer Y or y for yes or N or n for No...)  ")
    # if (current_balance <= 400):
    #     user_want_lottery = input("Would you liek to purchase a lottery ticker ? answer Y or y for yes or N or n for No..")
    if(purchase_lottery == "y" or purchase_lottery == "Y"):
        current_balance -=200 # cost of the ticket
        select_lottery()
        print()
    elif(purchase_lottery == "n" or purchase_lottery == "N"):
        print("n")
    else:
        print("No no lottery tickets were purchased. Select Items to Purchase :")
        purchase_other_items()                 
    # else:
    #     print("Current balance is out of range, kindly input correct amount. ")


item_count = 0
def purchase_other_items():
    # /Current amount checked
    if( intial_money<=400 ):
        print(f"Your current balacne is : {intial_money}")
             # Prompt if ned to bu bread 
        purchase_bread = input("Purchase bread ? y or Y for yes of N or n for No")
        if( purchase_bread == 'n' or purchase_bread == 'N'):
            item_count +=1
            check_item_type(item_count)
        elif( purchase_bread == 'y' or purchase_bread == 'Y'):
            purchase_bread_item() # purchases bread


    elif(intial_money < 95):
        print("Amount not enough")

    check_item_type(2) # id 2 represents Bread

    # print("*************** Available Items ****************\n")
    # print("(A).lottery_tickets : 200 \n (B).bread  : 95  \n (C).milk :70 \n (D).sodas : 60 ")
    # print("\n************************************")
    # first_item = input("Which item would you like ? ")
    # items_in_cart.append(first_item)
    # add_item = input(" Purchase another item ? respond with y or Y if yes and n ir N if No")
    # # while(add_item == "y" or add_item == "Y"):
    #     print("*************** Available Items ****************\n")
    #     print("1.lottery_tickets : 200 \n 2.bread  : 95  \n 3.milk :70 \n 4.sodas : 60 ")
    #     print("\n************************************")
    #     first_item = input("Which item would you like ? kindly input eg 1,2,3 or 4 ..  ")



def purchase_bread_item():
    intial_money = intial_money - 95
    bread_item_purchase +=1
    quantity = input("How many loaves would you like ? ")
    if( type(quantity.isdigit() != True)):
        print("Kindly input numerical values only")

    else: 
       if(quantity >1):
           amount =  95*quantity    #kindly revesit

           print(f"Loaves : {quantity}  \ntotal : {amount}")
           if(intial_money < amount):
               print("Not enough money")
           else:
               intial_money = intial_money - amount    
           check_current_amount()      



def check_item_type(id):
    if(id == 1):
        print("lottery ticket purchased")
    if(id == 2):
        print("bread purchased")
        # Logic to 
    if(id == 3):
        print("milk purchased")


def check_current_amount():
    value = False
    if(intial_money >=100 and intial_money >0):
        return True
    else:
        return False 


def select_lottery(winnings, current_balance,name, bread_price,lottery_ticket_num,lottery_ticket_price,f):
    lottery_tickets_purchased = 0
    print("getting lottery ticket status")
    f.write("\n\ngetting lottery ticket value ....\n\n")
    win = 2 #randint(0, 2)
    user_ticket =  randint(0, 2)
    if(user_ticket == win):
        winnings += (random.randint(2, 10)*100 )
        current_balance += winnings
        print(f"Congratulations {name} the value of your lottery ticket is {user_ticket*100}, your new balance is now ksh.{current_balance}")
        f.write(f"Congratulations {name} the value of your lottery ticket is {user_ticket*100}, your new balance is now ksh.{current_balance}\n\n") #print out ot the txt file if user has won 
        lottery = {
                    "quantity":lottery_ticket_num,
                    "price":lottery_ticket_price
                }
        get_bread(current_balance, name, bread_price,lottery,f)

    else:
        print("Unfortunately you have lost ....")
        f.write(f"Unfortunately {name}, you have lost ....\n\n") #print out ot the txt file if user has lost 
        # print("\n Kindly select another item this shopping list : \n")
        lottery = {
                    "quantity":0,
                    "price":0
                }
        get_bread(current_balance, name, bread_price,lottery,f)


def get_milk(current_balance, name, milk_price,bread,lottery,f):
    soda_price = 60 
    response = []
    # Tell client how much they currently have 
    print(f"\n ** Hi {name}, your current balance is ksh.{current_balance} **")
    user_want_milk = input (f"\n\n Would you like to purchase milk ? (answer Y or y for yes or N or n for No...) :  ")
    num_of_milk_pkts = input(f"How many pkts of milk would you like ? ")
    if(num_of_milk_pkts.isdigit()):
        if(current_balance >= int(num_of_milk_pkts)*milk_price):
            if(user_want_milk == "y" or user_want_milk == "Y"):
                current_balance -= milk_price
                response.append(current_balance)
                response.append(num_of_milk_pkts)
                milk = {
                    "quantity":int(num_of_milk_pkts),
                    "price":int(num_of_milk_pkts)*milk_price
                }
                get_soda(current_balance, name, soda_price,bread,milk,lottery,f)
                return response
            elif(user_want_milk == "n" or user_want_milk == "N"):
                print("\n** No milk was purchased **\n")
                milk = {
                    "quantity":0,
                    "price":0
                }
                get_soda(current_balance, name, soda_price,bread,milk,lottery,f)
            else:
                print("\n\nOoops! Wrong input kindly start over. ")         
        else:
            print("Not enough money !")  
    else:
        print("Sorry we only accept numerical values")  
 # gemerate user receipt .

def get_final_bill(bread,milk,soda,current_balance,lottery,f):
# using now() to get current time
    current_time = datetime.datetime.now()
    print("\n\n*******************************\n")
    print("         YOUR RECEIPT           \n")
    print("*******************************\n")
    print(f" Date : {current_time.day}/{current_time.month}/{current_time.year} at {current_time.hour}:{current_time.minute}")
    print("\nItems :")
    print("_____________________________") 
    print(f"Lottery x {lottery['quantity']} : {lottery['price']}")
    print(f"Bread x {bread['quantity']} :  {bread['price']}  ")
    print(f"Milk x {milk['quantity']} :  {milk['price']}  ")
    print(f"Soda x {soda['quantity']} :  {soda['price']}  ")
    
    #Sales recipt using PrettyTable
def sales_recipt(bread,milk,soda,initial_balance,lottery):
    PTables = PrettyTable()
    PTables.field_names = ["Item.", "Quantity", "Price"]
    PTables.add_row([ "Lottery", lottery['quantity'], lottery['price']])
    PTables.add_row([ "Bread", bread['quantity'], bread['price']])
    PTables.add_row([ "Milk", milk['quantity'], milk['price']])
    PTables.add_row([ "Soda", soda['quantity'], soda['price']])
    print(PTables)
            


    print("\nTotal Price :")
    print("----------------------------")
    print(f"Current Balance : {current_balance}")
    print(f"Total Expense : : {bread['price'] +milk['price']+soda['price']+lottery['price']}")
    print("----------------------------\n\n")
    print("***************************\n")
    print("Thank you for shopping with us \n")
    print("***************************\n")

    # Writing to the txt file 
    f.write("\n\n*******************************\n")
    f.write("         YOUR RECEIPT           \n")
    f.write("*******************************\n")
    f.write(f" Date : {current_time.day}/{current_time.month}/{current_time.year} at {current_time.hour}:{current_time.minute}")
    f.write("\nItems :")
    f.write("_____________________________") 
    f.write(f"Lottery x {lottery['quantity']} : {lottery['price']}")
    f.write(f"Bread x {bread['quantity']} :  {bread['price']}  ")
    f.write(f"Milk x {milk['quantity']} :  {milk['price']}  ")
    f.write(f"Soda x {soda['quantity']} :  {soda['price']}  ")

    f.write("\nTotal Price :")
    f.write("----------------------------")
    f.write(f"Current Balance : {current_balance}")
    f.write(f"Total Expense : : {bread['price'] +milk['price']+soda['price']+lottery['price']}")
    f.write("----------------------------\n\n")
    f.write("***************************\n")
    f.write("Thank you for shopping with us \n")
    f.write("***************************\n")



def get_soda(current_balance, name, soda_price,bread,milk,lottery,f):

    response = []
    # Tell client how much they currently have 
    print(f"\n ** Hi {name}, your current balance is ksh.{current_balance} **")
    user_want_soda = input(f"\n\n Would you like to soda? (answer Y or y for yes or N or n for No...) :  ")
    num_of_soda_btles = input(f"How many bottles of soda would you like ? ")
    if(num_of_soda_btles.isdigit()):
        if(current_balance >= int(num_of_soda_btles)*soda_price):
            if(user_want_soda == "y" or user_want_soda == "Y"):
                current_balance -= int(num_of_soda_btles)*soda_price
                response.append(current_balance)
                response.append(num_of_soda_btles)
                soda = {
                    "quantity":int(num_of_soda_btles),
                    "price":int(num_of_soda_btles)*soda_price
                }
                get_final_bill(bread,milk,soda,current_balance,lottery,f)
                return response
            elif(user_want_soda == "n" or user_want_soda == "N"):
                print("\n** No soda was purchased **\n")
                soda = {
                    "quantity":0,
                    "price":0
                }
                get_final_bill(bread,milk,soda,current_balance,lottery,f) 
            else:
                print("\n\nOoops! Wrong input kindly start over. ")
        else:
            print("Not enough money !")     
    else:
        print("Sorry we only accept numerical values")




def get_bread(current_balance, name, bread_price,lottery,f):
    bread_price= 95
    milk_price = 70 
    response = []
    # Tell client how much they currently have 
    print(f"\n ** Your current balance is ksh.{current_balance} **")
    user_want_bread = input (f"\n\n Would you like to purchase bread ? (answer Y or y for yes or N or n for No...) :  ")
    # writing to txt file 
    f.write(f"\n\n Would you like to purchase bread ? (answer Y or y for yes or N or n for No...) :  \n")
    f.write(f"Your current choice is  : {user_want_bread}")

    num_of_loaves = input(f"How many loaves of bread would you like ? ")
    f.write(f"\n\n How many loaves of bread would you like ? \n")
    f.write(f"Loaves needed : {num_of_loaves}")
    if(num_of_loaves.isdigit()):
        if(current_balance >= int(num_of_loaves)*bread_price):
            if(user_want_bread == "y" or user_want_bread == "Y"):
                current_balance -= int(num_of_loaves)*bread_price
                response.append(current_balance)
                response.append(num_of_loaves)
                bread = {
                    "quantity":int(num_of_loaves),
                    "price":int(num_of_loaves)*bread_price
                }
                get_milk(current_balance,name,milk_price, bread,lottery,f)
                return response
            elif(user_want_bread == "n" or user_want_bread == "N"):
                print("\n** No bread was purchased **\n")
                f.write(f"\n** No bread was purchased **\n")
                bread = {
                    "quantity":0,
                    "price":0
                }
                get_milk(current_balance,name,milk_price, bread,lottery,f)
            else:
                print("\n\nOoops! Wrong input kindly start over. ")
                f.write("\n\n Ooops! Wrong input kindly start over !!! ")  
        else:
            print("Not enough money !")     
            f.write("\n\n Not enough money !")   
    else:
       print("Sorry We only accept numerical values.")
       f.write("\n\n Sorry We only accept numerical values !")  


# function to allow client ot select the ite they need 
def available_items():
    items_on_sale = "(A). lottery_tickets : 200 \n (B).bread  : 95  \n (C).milk :70 \n (D).sodas : 60 "
    # print(f"Welcome to our shop {name}, you currently have ksh. {current_balance}.00 in your account.\n\n These are the current items at the store:\n ")
    print("*************** INVENTORY ****************\n")
    print(" 1. Lottery Tickets : 200/= \n 2. Bread  : 95/=  \n 3. Milk : 70/= \n 4. Sodas : 60/=\n ")
    print("************************************************\n")

    # Write to txt file 
    f.write("*************** INVENTORY ****************\n")
    f.write(items_on_sale)
    f.write("************************************************\n")

    choice = input("Enter Item you would like to purchase (e.g 1,2,3 or 4 ...) :")
    f.write("Enter Item you would like to purchase (e.g 1,2,3 or 4 ...) :\n")
    f.write(f"Your current choice is  : {choice}")
    return choice


# functions to pass the total amount used,
def current_bill(value):
    total = 0 
    total += value
    return total



# Main Supermarket application

def play_shopping_game():

    # Kinldy note that the print() method is used for debugging purposes in this system 
    # Create a txt file by the name output.txt and append to the text file on every output
    f = open('output.txt','w')

initial_money = 400
current_balance = 400
lottery_ticket_num = 0

    # variables storing the unit price the following: 
    # - an individual lottery ticket
    # - the unit price of a loaf of bread, 
    # - the unit price of an individual packet of milk 
    # - and the unit price of an individual soda.

    #These are the current Item prices
bread_price= 95
milk_price = 70
soda_price = 60
lottery_ticket = 200

    # Variables storing: 
    # - initial money the user has 
    # - the money the user has spent

    #Money spent and initial amount 
initial_money = 400
current_balance = 400

    # variables storing the amounts of : 
    # - lottery tickets
    # - bread
    # - milk
    # - sodas 
    # the user has

    # Variables storing quantitites of eacch item purchased
lottery_ticket_num = 0
bread_quantity = 0
milk_quantity = 0
soda_quantity = 0

    # global variabl that will be overriden
name =""

winnings = 0 
intial_money = 400


    # shopping list array
items_in_cart = [] 

    # current 
win =  randint(0, 2)
print("\nShopping app loading.....\n")

#  Task :
# - Ask user their name
# - print a welcome message
# - print a list of products and their unit prices.
# - tell the user how much money they have available. 
# - log to the output.txt

name = input("Kindly input your name : ")
welcome_note = f"Welcome to our shop {name}, you currently have ksh. {initial_money}.00 in your account.\n\n These are the current items at the store:\n\n "
items_on_sale = " 1. Lottery Tickets : 200/= \n 2. Bread  : 95/=  \n 3. Milk : 70/= \n 4. Sodas : 60/=\n "
print("\n*************** The Shop ****************")
print(welcome_note) 
f = open('output.txt','w')
f.write(welcome_note) 
f.close()
print(items_on_sale )
print("************************************************\n")
    # print to txt file 
f = open('output.txt','a')
f.write("*************** The Shop ****************")
f.write(items_on_sale )
f.write("************************************************************\n")


# Ask user if they want to purchase a lottery ticket
user_want_lottery = input (f" Your Current balance is : ksh. {initial_money}, would you like to purchase a lottery ticket ? (answer Y or y for yes or N or n for No...) :   ")
    # Write to txt file 
f.write(f" Your Current balance is : ksh. {initial_money}, would you like to purchase a lottery ticket ? (answer Y or y for yes or N or n for No...) :   \n") # write to txt file on the inputed amount 
f.write(f"Your Current choice is :{user_want_lottery} \n\n") # write to txt file on the inputed amount 
# Handling the purchase of lottery ticket request
if(user_want_lottery == "y" or user_want_lottery == "Y"):
      # charge client cost of the ticket
        current_balance -=200 
        lottery_ticket_num +=1
        select_lottery(winnings,current_balance,name, 95, lottery_ticket_num,200,f)
        print()
elif(user_want_lottery == "n" or user_want_lottery == "N"):
        print("\n** No lottery tickets were purchased **\n")
        print("Kindly select another item this shopping list : \n")
        lottery = {
                    "quantity":0,
                    "price":0
                }
        get_bread(current_balance, name, 95,lottery,f)

else:
        print("Ooops! Wrong input kindly start over. ")

f.close() # purposed with closing of the txt file 
if __name__ =='__main__':
    play_shopping_game()