"""
NAME: KORIR ROBERT KIPNGENO
STUDENT ID: 148989
STATEMENT OF WORK: I followed youtube tutorials on python and class work exercises given.
1. https://www.geeksforgeeks.org/python-exercises-practice-questions-and-solutions/
2. https://www.w3resource.com/python-exercises/python-basic-exercises.php


"""
import random as random

#Self-Defined Functions
#Return a integer input, the function will keep running until the input is an integer
def get_the_input():
    
    while True:
        try:
            return int(input())
        except:
            print('Please input an integer number!!')
#print the bricks in the tower from top to bottom
def print_tower(tower):	
	print('Your tower is:',tower)
	print('----------------------------')
#Execute the player's action on the discard pile, return true is the brick is taken
def take_discard_pile(tower, discard):

#Get the top brick in the disard pile
    new_brick=get_top_brick(discard)
    while True:
# print the current tower
        print('Your tower is:',tower)
#print the retrived brick and the instruction
        print('The top of the discard pile is: '+str(new_brick))
        print('Please enter the integer number of the brick in your \
              tower you want to replace,')
        print('or enter 0 to see the top brick of the main pile:')
        scanner=get_the_input()

#Try to replace the brick if the player choose so
        if scanner!=0:
            ## return True if the replacement succeed
            if find_and_replace(new_brick, scanner, tower, discard):
                return True
# when the player chooses not selecting the discard pile
        else:
            add_brick_to_discard(new_brick,discard)
            return False
#Execute the player's action on the main_pile, no return     
def take_main_pile(tower, main_pile,discard):
    new_brick=get_top_brick(main_pile)
    while True:
# print the current tower
        print('Your tower is:',tower)
#print the current main pile's top and the instruction
        print('The top of the main pile is: '+str(new_brick))
        print('Please enter the integer number of the brick in your \
              tower you want to replace,')
        print('or enter 0 to place it on the top of the discard pile:\n') 
        scanner=get_the_input()

#Try to replace the brick if the player choose so
        if scanner!=0:
# break the recurrence if the replacement succeed
            if find_and_replace(new_brick, scanner, tower, discard):
                break

#if the player inputs 0, break the recurrence
        else:
            print('There is no change on your tower in this move.')
            add_brick_to_discard(new_brick, discard)
            break
#Display the information to the player, and take actions           
def player_play(tower, main_pile, discard):
    

    print('============================')
    print('YOUR TRUN')
#go to 'discard_pile' stage,
    if not take_discard_pile(tower, discard):
#if the player opts out, go to the main pile process
        take_main_pile(tower, main_pile,discard)
#print the result of the play
    print('Now your tower is:',tower)
    print('Now the top of discard pile is',discard[0])

def check_main_pile(main_pile,discard):
    '''check if the main pile is empty,
    take the shuffled discard pile as the new main pile if so'''

    if len(main_pile)==0:
        shuffle(discard)
        main_pile[0:]=discard
        discard.clear()
        add_brick_to_discard(get_top_brick(main_pile), discard)

#Beginning of functions

def shuffle(bricks):
    ''' Shuffle the bricks (represented as a list)'''
    random.shuffle(bricks)
	
def check_tower_blaster(tower):
    ''' Return True if the tower's stability has been achieved, else False'''

    expectation=tower.copy()
    expectation.sort()
    return True if tower==expectation else False
    
def get_top_brick(brick_pile):
    ''' Return the top brick from the given pile of bricks'''
    return int(brick_pile.pop(0))

def deal_initial_bricks(main_pile):
    ''' Return two lists to initial the game'''

#Functio to create an empty tower
    computer_pile=list()
    player_pile=list()
# distribute the bricks to two towers in turns
    for time in range(10):
        computer_pile.insert(0,main_pile.pop(0))
        player_pile.insert(0,main_pile.pop(0))
    
    return (computer_pile, player_pile)
	
def add_brick_to_discard(brick, discard):
    ''' Add the brick to the top of the discard pile'''
    discard.insert(0,brick)
    

def find_and_replace(new_brick, brick_to_be_replaced, tower, discard):
    ''' Replace the chosen brick by new_brick in the tower
    and put the old brick on the top of the discard pile,
    return a Boolean tells if the replacement has been successfully done'''
#try to replace the brick, and put the old brick on the top of the discard pile, return True if succeed

    try:
        tower[tower.index(brick_to_be_replaced)]=new_brick
        add_brick_to_discard(brick_to_be_replaced,discard)
        return True
# if failed, print the warning and turn False
    except:
        print('====Wrong brick number, please try again====')
        return False

def computer_play(tower, main_pile, discard):
    if tower[0]>60:
# put the top discard brick to the tower top if it is less than 21
        if discard[0]<=60:
                find_and_replace(get_top_brick(discard),\
                                 tower[0], tower, discard)
# if the discard pile has a large top, try the main pile,
        else: 
            new_brick=get_top_brick(main_pile)
# put its top brick to the tower top if it is less than 21
            if new_brick<=60:
                find_and_replace(new_brick, tower[0], tower, discard)
# if none of the conditions are satisfies, skip this turn
            else: 
                add_brick_to_discard(new_brick, discard)
                
    else:
# take the brick from the top of the discard pile,
        new_brick=get_top_brick(discard)
        
# find the length of the ordered sequence from the top of the tower
        i=1
        while tower[i-1]<tower[i]:
            i+=1
            if i==9:
                break
# if it is larger than any brick in the sequence
        if new_brick>max(tower[:i]):
# put the brick under the bottom of the ordered sequence 
             find_and_replace(new_brick, tower[i], tower, discard)
# else, replace the first brick from top that is larger than it 
        else:
            j=0
#find and replace the first larger one
            while True: 
                if new_brick<tower[j]:
                    find_and_replace(new_brick, tower[j], tower, discard)
                    break
                j+=1
        
#Main function of the game
def main():
#environment setup
    discard=[]
    main_pile=list(range(1,61))
    shuffle(main_pile)
    (computer_tower, player_tower)=deal_initial_bricks(main_pile)
    add_brick_to_discard(get_top_brick(main_pile), discard)
    print('============================')
    print('Game starts!')

    while True:
#computer's move and evaluation
        check_main_pile(main_pile,discard)
        print('============================')
        print('Computer is taking its move.')
        computer_play(computer_tower,main_pile,discard)
        if check_tower_blaster(computer_tower):
            print('============YOU LOSE. ===========')
            break
            
#player's move and evaluation
        check_main_pile(main_pile,discard)
        player_play(player_tower,main_pile,discard)
        if check_tower_blaster(player_tower):
            print('===========YOU WIN!!!=============')
            break
        
#print the computer's tower
    print('The computer\'s tower now is:',computer_tower)

if __name__ == '__main__':
    main()