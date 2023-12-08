# Rock (A,X)
# Paper (B,Y)
# Scissors (C,Z)

ROUND = {
    'A X': 'D',
    'A Y': 'W',
    'A Z': 'L',
    'B X': 'L',
    'B Y': 'D',
    'B Z': 'W',
    'C X': 'W',
    'C Y': 'L',
    'C Z': 'D',
}

SCORES = {
    'W': 6,
    'D': 3,
    'L': 0,
}

SHAPES = {
    'X': 1, 'A': 1, # ROCK
    'Y': 2, 'B': 2, # PAPER
    'Z': 3, 'C': 3, # SCISSORS
}

def calculate_points_part_one(file_name):
    points = 0
    with open(file_name, "r") as strategy:
        for line in strategy:
            points += SCORES[ROUND[line.strip("\n")]] + SHAPES[line.strip("\n").split(" ")[-1]]
    return points

print(calculate_points_part_one("strategy.txt"))

OUTCOMES = {
    'X': 'L',
    'Y': 'D',
    'Z': 'W'
}

SHAPE_OUTCOMES = {
    'A': { # ROCK
        'W': 'Y', # PAPER
        'D': 'X', # ROCK
        'L': 'Z', # SCISSORS
    },

    'B': { # PAPER
        'W': 'Z', # SCISSORS
        'D': 'Y', # PAPER
        'L': 'X', # ROCK
    },

    'C': { # SCISSORS
        'W': 'X', # ROCK
        'D': 'Z', # SCISSORS
        'L': 'Y', # PAPER
    }
}

def calculate_points_part_two(file_name):
    points = 0
    with open(file_name, "r") as strategy:
        for line in strategy:
            opponent_choice, outcome = line.strip("\n").split(" ")
            choice = SHAPE_OUTCOMES[opponent_choice][OUTCOMES[outcome]]
            points += SCORES[ROUND[" ".join([opponent_choice, choice])]] + SHAPES[choice]
    return points

print(calculate_points_part_two("strategy.txt"))