from random import randint

game = ["rock", "paper", "scissors"]
pls_points = 0
comps_points = 0

def rps1(input_rps):
    global pls_points, comps_points
    while True:
        pl = input_rps
        comp = game[randint(0,2)]
        if pl == comp:
            return f"You have selected {pl} and computer has selected {comp}."
        elif pl == "rock":
            if comp == "paper":
                comps_points += 1
                return f"You Lost | You have selected {pl} and computer has selected {comp}."
            else:
                pls_points += 1
                return f"You Won | You have selected {pl} and computer has selected {comp}."
        elif pl == "paper":
            if comp == "scissors":
                comps_points += 1
                return f"You Lost | You have selected {pl} and computer has selected {comp}."
            else:
                pls_points += 1
                return f"You Won | You have selected {pl} and computer has selected {comp}."
        elif pl == "scissors":
            if comp == "rock":
                comps_points += 1
                return f"You Lost | You have selected {pl} and computer has selected {comp}."
            else:
                pls_points += 1
                return f"You Won | You have selected {pl} and computer has selected {comp}."
