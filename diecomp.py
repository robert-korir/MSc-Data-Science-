import random
def roll_dice():
    return random.randint(1,6)

players = ['Player One', 'Player Two']
scores = {'Player One': 0, 'Player Two': 0}
random.shuffle(players)

while True:
    for i in players:
        if i == 'Player One':
            choice = input("Roll(r) or Hold(h)?: ")
            turn_score = 0
            final_score = 0
            if (choice=='r'):
                while(turn_score<=20):
                    dice_value = roll_dice()
                    turn_score += dice_value
                    if (dice_value==1):
                        turn_score = 0
                        print("-rolled a ",dice_value)
                        print("Pigged out!")
                        break
                    print("Turn score is: ",turn_score)
                    final_score += turn_score
                    print("Your final score is: ",final_score)
                    if (final_score>100):
                        break
        else:
            turn_score=0
            print("It is " +  str(i) + "'s turn.")
            while(turn_score<20):
                dice_value = roll_dice()
                if (dice_value==1):
                    turn_score = 0
                    scores[i] +=0
                    print("- rolled a ",dice_value)
                    print("Pigged out!")
                    break
                else:
                    turn_score+=dice_value
                    print("-rolled a ",dice_value)
        scores[i] += turn_score
        print("Turn score is: ",turn_score)
        print('{} score: {} {} score: {}'.format(players[0], scores[players[0]], players[1], scores[players[1]]))
        if scores[i]>100:
            break
    if scores[i]>100:
        break

winner = [winner for winner in scores if scores[winner] == max(scores.values())]
print(str(winner) + " is the winner!")