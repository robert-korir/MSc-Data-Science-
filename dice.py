"""
NAME: KORIR ROBERT KIPNGENO
STUDENT ID: 148989
STATEMENT OF WORK: I followed youtube tutorials on python and class work exercises given.


"""
import sys
import random

HUMAN_SCORE = 0
COMPUTER_SCORE = 1
HOLD = False
ROLL = True

# f = open('output.txt','w')
class Die:
    def __init__(self):
        self.value = random.randint(1, 6)

    def roll(self):
        self.value = random.randint(1, 6)

    @staticmethod
    def rolled_one():
        print("Rolled 1. \n")

    def __str__(self):
        return "Rolled " + str(self.value) + "."


class total_score:
    def __init__(self):
        self.value = 0

    def reset_total_score(self):
        self.value = 0

    def add_dice_value(self, dice_value):
        self.value = self.value + dice_value

    def __str__(self):
        return "total_score total:" + str(self.value)


class Player:
    def __init__(self, name=None):
        self.name = name
        self.score = 0

    def add_score(self, player_score):
        self.score = self.score + player_score

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return str(self.name) + ": " + str(self.score)


class ComputerPlayer(Player):
    def __init__(self):
        Player.__init__(self, name="COMPUTER")

    @staticmethod
    def make_decision(total_score):
        while total_score.value >= 50:
            print("I will not roll again.")
            return ROLL
            break
        print("I will not hold.")
        return HOLD


class HumanPlayer(Player):
    def __init__(self):
        Player.__init__(self, name="HUMAN")

    @staticmethod
    def make_decision():
        human_decision = (input("Roll again (input y or Y ) or Hold ( input n or N)? "))
        if (human_decision == "y" or human_decision == "Y" or human_decision[0] == "y" or human_decision[0] == "Y") :
            return ROLL
        elif (human_decision == "N" or human_decision == "n" or human_decision[0] == "n" or human_decision[0] == "N") :
            return HOLD


class Score:
    def __init__(self, human_score, computer_score, total_score):
        self.human = human_score
        self.computer = computer_score
        self.total_score = total_score

    def __str__(self):
        return "Current Score -->   " + str(self.human) + "\t" + str(self.computer) + "\n"


class GameManager:
    def __init__(self):
        self.computer_player = ComputerPlayer()
        self.human_player = HumanPlayer()
        self.die = Die()
        self.total_score = total_score()
        self.score = Score(self.human_player, self.computer_player, self.total_score)
        self.computer = 0
        self.turn = None
        self.action = None

    @staticmethod
    def welcome():
        f = open('output.txt','w')
        asterix = "*" * 70
        print("*" * 70)
        # Roll as many times as your wish
        print("Roll as many times as your wish." .center(70))
        f.write("\n\nRoll as many times as your wish....\n\n")
        f.write(asterix)
        print("*" * 70)
        # If the value/ result is 6 your score is zero plus the existing result/scorre and your turn ends same to the computer 
        print(" If the value/ result is 6 your score is zero plus the existing result/scorre and your turn ends same to the computer. " .center(70))
        f.write("\n\nIf the value/ result is 6 your score is zero plus the existing result/score and your turn ends same to the computer....\n\n")
        print("*" * 70)
        f.write(asterix)
        # At the end of each turn your score is added to your total score same to the computers
        print("At the end of each turn your score is added to your total score same to the computers" .center(70))
        f.write("\n\nAt the end of each turn your score is added to your total score same to the computers....\n\n")
        print("*" * 70)
        f.write(asterix)
        # The first player to reach or exceed 50 wins
        print("The first player to reach or exceed 50 wins" .center(70))
        f.write("\n\nThe first player to reach or exceed 50 wins....\n\n")
        print("*" * 70)
        f.write(asterix)
        print()
        f.close()
        
    def decide_first_player(self,f):
        self.turn = 1
        print("TURN --- > ", self.turn)
        if self.turn == HUMAN_SCORE:
            print("Human starts!" .center(70, " "))
            f.write("Human starts! .center(70, .....")
        else:
            print("COMPUTER STARTS!")
            f.write("\nCOMPUTER STARTS!" .center(70, " "))
        

    def switch_turns(self,f):
        if self.turn == COMPUTER_SCORE:
            self.turn = HUMAN_SCORE
        else:
            self.turn = COMPUTER_SCORE

    def print_turn(self,f):
        if self.turn == HUMAN_SCORE:
            print("Your turn.\n")
            f.write("Your turn.\n")
        else:
            print("My turn.\n")
            f.write("My turn.\n")

    def check_score(self,f):
        if self.human_player.score >=50:
            print("Human wins!")
            f.write("Human wins!.\n")
            f.close() 
            sys.exit()
        elif self.computer_player.score >= 50:
            print("COMPUTER win!")
            f.write("COMPUTER wins!.\n") 
            f.close()           
            sys.exit() 

    def assign_score(self):
        if self.turn == HUMAN_SCORE:
            self.human_player.add_score(self.total_score.value)
        else:
            self.computer_player.add_score(self.total_score.value)

    def play_game(self):
        f = open('output.txt','a')
        self.decide_first_player(f) # prints out who starts game computer starts the game by default
        while (not self.human_player.score >= 50) and (not self.computer_player.score >= 50 ):
            self.get_action(f) # play game 

    def get_action(self,f):
        print("Game has started ...................\n")
        self.action = ROLL
        self.total_score.reset_total_score()
        print("\n\nSCORES ==== > {self.score}\n\n")
        f.write(f"\n\nSCORES ==== > {self.score}\n")
        self.print_turn(f)
        # prompot human to make choice if to play or not play
        state = HumanPlayer.make_decision()
        self.keep_rolling(f)
        self.assign_score()
        self.check_score(f)
        self.switch_turns(f)

    def keep_rolling(self,f):
        self.die.roll()
        dice_value = self.die.value
        print("Dice Value  : ", dice_value)
        f.write(f"Dice Value  : { dice_value}\n")
        if self.turn == HUMAN_SCORE:
            print("Player  : ", self.turn)
            f.write(f"Player  :  {self.turn}\n")
            if dice_value == 1:
                self.die.rolled_one()
                # self.total_score.reset_total_score()
                self.action = HOLD
                return
            else:
                self.total_score.add_dice_value(dice_value)
                print(f"Die Pistion ---  {self.die}" .center(70),)
                f.write(f"Die Pistion --- {self.die}\n" .center(70) )
                print(self.total_score)
                self.action = self.human_player.make_decision()
                return
        else:
            if dice_value == 1:
                self.die.rolled_one()
                # self.total_score.reset_total_score()
                self.action = HOLD
                return
            else:
                self.total_score.add_dice_value(dice_value)
                f.write(f"Total score  : {self.total_score.value}\n")
                print(self.die)
                print(self.total_score)
                self.action = self.computer_player.make_decision(self.total_score)
               
                return


def main():
    game_manager = GameManager()
    game_manager.welcome()
    game_manager.play_game()
    #f.close() # purposed with closing of the txt file 


if __name__ =='__main__':
    main()