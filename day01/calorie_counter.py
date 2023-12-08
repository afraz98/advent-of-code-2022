def find_calories(file_name):
    calories = []
    with open(file_name, "r") as input_file:
        i = 0
        calories.append(0)
        for line in input_file:
            if line != "\n":
                calories[i] += int(line)
            else:
                i += 1
                calories.append(0)
    return calories

def find_max_calories(calories):
    return max(calories)

print(find_max_calories(find_calories("calories.txt")))

def find_top_three_calories(file_name):
    calories = find_calories(file_name)
    return calories.pop(calories.index(find_max_calories(calories))) + calories.pop(calories.index(find_max_calories(calories))) + calories.pop(calories.index(find_max_calories(calories)))

print(find_top_three_calories("calories.txt"))