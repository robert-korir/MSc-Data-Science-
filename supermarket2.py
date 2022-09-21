import random
from random import randint
import datetime
 




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


def select_lottery(winnings, current_balance,name, bread_price,lottery_ticket_num,lottery_ticket_price):
    lottery_tickets_purchased = 0
    print("getting lottery ticket status")
    win = 2 #randint(0, 2)
    user_ticket =  randint(0, 2)
    if(user_ticket == win):
        winnings += (random.randint(2, 10)*100 )
        current_balance += winnings
        print(f"Congratulations {name} the value of your lottery ticket is {user_ticket*100}, your new balance is now ksh.{current_balance}")
        lottery = {
                    "quantity":lottery_ticket_num,
                    "price":lottery_ticket_price
                }
        get_bread(current_balance, name, bread_price,lottery)

    else:
        print("Unfortunately you have lost ....")
        print("\n** No lottery tickets were purchased **\n")
        # print("\n Kindly select another item this shopping list : \n")
        lottery = {
                    "quantity":0,
                    "price":0
                }
        get_bread(current_balance, name, bread_price,lottery)


def get_milk(current_balance, name, milk_price,bread,lottery):
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
                get_soda(current_balance, name, soda_price,bread,milk,lottery)
                return response
            elif(user_want_milk == "n" or user_want_milk == "N"):
                print("\n** No milk was purchased **\n")
                milk = {
                    "quantity":0,
                    "price":0
                }
                get_soda(current_balance, name, soda_price,bread,milk,lottery)
            else:
                print("\n\nOoops! Wrong input kindly start over. ")         
        else:
            print("Not enough money !")  
    else:
        print("Sorry we only accept numerical values")  
 # gemerate user receipt .
def get_final_bill(bread,milk,soda,current_balance,lottery):
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

    print("\nTotal Price :")
    print("----------------------------")
    print(f"Current Balance : {current_balance}")
    print(f"Total Expense : : {bread['price'] +milk['price']+soda['price']+lottery['price']}")
    print("----------------------------\n\n")
    print("***************************\n")
    print("Thank you for shopping with us \n")
    print("***************************\n")

  

def get_soda(current_balance, name, soda_price,bread,milk,lottery):
 
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
                get_final_bill(bread,milk,soda,current_balance,lottery)
                return response
            elif(user_want_soda == "n" or user_want_soda == "N"):
                print("\n** No soda was purchased **\n")
                soda = {
                    "quantity":0,
                    "price":0
                }
                get_final_bill(bread,milk,soda,current_balance,lottery) 
            else:
                print("\n\nOoops! Wrong input kindly start over. ")
        else:
            print("Not enough money !")     
    else:
        print("Sorry we only accept numerical values")
        
 

    


def get_bread(current_balance, name, bread_price,lottery):
    bread_price= 95
    milk_price = 70 
    response = []
    # Tell client how much they currently have 
    print(f"\n ** Hi {name}, your current balance is ksh.{current_balance} **")
    user_want_bread = input (f"\n\n Would you like to purchase bread ? (answer Y or y for yes or N or n for No...) :  ")
    num_of_loaves = input(f"How many loaves of bread would you like ? ")
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
                get_milk(current_balance,name,milk_price, bread,lottery)
                return response
            elif(user_want_bread == "n" or user_want_bread == "N"):
                print("\n** No bread was purchased **\n")
                bread = {
                    "quantity":0,
                    "price":0
                }
                get_milk(current_balance,name,milk_price, bread,lottery)
            else:
                print("\n\nOoops! Wrong input kindly start over. ")  
        else:
            print("Not enough money !")        
    else:
       print("Sorry We only accept numerical values.")


# function to allow client ot select the ite they need 
def available_items():
    # print(f"Welcome to our shop {name}, you currently have ksh. {current_balance}.00 in your account.\n\n These are the current items at the store:\n ")
    print("*************** ROBERTS' INVENTORY ****************\n")
    print(" 1. Lottery Tickets : 200/= \n 2. Bread  : 95/=  \n 3. Milk : 70/= \n 4. Sodas : 60/=\n ")
    print("************************************************\n")
    choice = input("Enter Item you would like to purchase (e.g 1,2,3 or 4 ...) :")
    return choice


# functions to pass the total amount used,
def current_bill(value):
    total = 0 
    total += value
    return total



# Main Supermarket application

def play_shopping_game():
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
# - tell the user how much money they have available 

    name = input("Kindly input your name : ")
    print("\n*************** The Shop ****************")
    print(f"Welcome to our shop {name}, you currently have ksh. {initial_money}.00 in your account.\n\n These are the current items at the store:\n ")
    print("*************** ROBERTS' INVENTORY ****************\n")
    print(" 1. Lottery Tickets : 200/= \n 2. Bread  : 95/=  \n 3. Milk : 70/= \n 4. Sodas : 60/=\n ")
    print("************************************************\n")

# Ask user if they want to purchase a lottery ticket
    user_want_lottery = input (f" Your Current balance is : ksh. {initial_money}, would you like to purchase a lottery ticket ? (answer Y or y for yes or N or n for No...) :   ")

# Handling the purchase of lottery ticket request
    if(user_want_lottery == "y" or user_want_lottery == "Y"):
      # charge client cost of the ticket
        current_balance -=200 
        lottery_ticket_num +=1
        select_lottery(winnings,current_balance,name, 95, lottery_ticket_num,200)
        
        print()
    elif(user_want_lottery == "n" or user_want_lottery == "N"):
        print("\n** No lottery tickets were purchased **\n")
        print("Kindly select another item this shopping list : \n")
        lottery = {
                    "quantity":0,
                    "price":0
                }
        get_bread(current_balance, name, 95,lottery)

    else:
        print("Ooops! Wrong input kindly start over. ")    
  
  
if __name__ =='__main__':
    play_shopping_game()