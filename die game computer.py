import sys
import random

HUMAN = 0
COMPUTER = 1
HOLD = False
ROLL = True


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


class Box:
    def __init__(self):
        self.value = 0

    def reset_box(self):
        self.value = 0

    def add_dice_value(self, dice_value):
        self.value = self.value + dice_value

    def __str__(self):
        return "Box total:" + str(self.value)


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
        Player.__init__(self, name="ELIZA")

    @staticmethod
    def make_decision(box):
        while box.value < 20:
            print("I will roll again.")
            return ROLL
        print("I will hold.")
        return HOLD


class HumanPlayer(Player):
    def __init__(self):
        Player.__init__(self, name="HUMAN")

    @staticmethod
    def make_decision():
        human_decision = int(input("Roll again (Press 1) or Hold (Press 0)? "))
        if human_decision == 1:
            return ROLL
        else:
            return HOLD


class Score:
    def __init__(self, human, computer, box):
        self.human = human
        self.computer = computer
        self.box = box

    def __str__(self):
        return "Current Score -->   " + str(self.human) + "\t" + str(self.computer) + "\n"


class GameManager:
    def __init__(self):
        self.computer_player = ComputerPlayer()
        self.human_player = HumanPlayer()
        self.die = Die()
        self.box = Box()
        self.score = Score(self.human_player, self.computer_player, self.box)
        self.computer = 0
        self.turn = None
        self.action = None

    @staticmethod
    def welcome():
        print("*" * 70)
        print("Welcome to Pig Dice!" .center(70))
        print("*" * 70)
        print("The objective is to be the first to reach 100 points." .center(70))
        print("On each turn, the computer will roll a die." .center(70))
        print("The die value will stored in a temporary score box." .center(70))
        print("(If the die value is 1, the player earns no points," .center(70))
        print("and the turn switches to the other player.)" .center(70))
        print("The player has option to either roll again," .center(70))
        print("or hold. If you hold, the score in the" .center(70))
        print("temprory box will be assigned to you." .center(70))
        print("Good luck!" .center(70, "*"))
        print("Remember" .center(70, "*"))
        print("(Fortune favors the brave...." .center(70, "*"))
        print("(but chance favors the smart!" .center(70, "*"))
        print()
        print("I will now flip a coin to decide who starts" .center(70, " "))
        print()

    def decide_first_player(self):
        self.turn = random.randint(1, 2) % 2
        if self.turn == HUMAN:
            print("Human starts!" .center(70, " "))
        else:
            print("Eliza starts!" .center(70, " "))
        print()

    def switch_turns(self):
        if self.turn == COMPUTER:
            self.turn = HUMAN
        else:
            self.turn = COMPUTER

    def print_turn(self):
        if self.turn == HUMAN:
            print("Your turn.\n")
        else:
            print("My turn.\n")

    def check_score(self):
        if self.human_player.score > 99:
            print("Human wins!")
            sys.exit()
        elif self.computer_player.score > 99:
            print("Eliza win!")
            sys.exit()

    def assign_score(self):
        if self.turn == HUMAN:
            self.human_player.add_score(self.box.value)
        else:
            self.computer_player.add_score(self.box.value)

    def play_game(self):
        self.welcome()
        self.decide_first_player()
        while (self.human_player.score < 100) and (self.computer_player.score < 100):
            self.get_action()

    def get_action(self):
        self.action = ROLL
        self.box.reset_box()
        print(self.score)
        self.print_turn()
        while self.action == ROLL:
            self.keep_rolling()
        self.assign_score()
        self.check_score()
        self.switch_turns()

    def keep_rolling(self):
        self.die.roll()
        dice_value = self.die.value
        if self.turn == HUMAN:
            if dice_value == 1:
                self.die.rolled_one()
                self.box.reset_box()
                self.action = HOLD
                return
            else:
                self.box.add_dice_value(dice_value)
                print(self.die)
                print(self.box)
                self.action = self.human_player.make_decision()
                return
        else:
            if dice_value == 1:
                self.die.rolled_one()
                self.box.reset_box()
                self.action = HOLD
                return
            else:
                self.box.add_dice_value(dice_value)
                print(self.die)
                print(self.box)
                self.action = self.computer_player.make_decision(self.box)
                return


def main():
    game_manager = GameManager()
    game_manager.play_game()


main()