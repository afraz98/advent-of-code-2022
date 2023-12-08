import string

LETTERS = {letter: index for index, letter in enumerate(string.ascii_letters, start=1)}

def _find_common_item(rucksack):
    common_items = ""

    compartment_size = len(rucksack) // 2
    compartment_one = rucksack[:compartment_size]
    compartment_two = rucksack[compartment_size:]

    for item in compartment_one:
        if item in compartment_two and item not in common_items:
            common_items += item
    return common_items

def _find_priority(items):
    priority = 0
    for item in items:
        priority += LETTERS[item]
    return priority

def find_priority(file_name):
    priority = 0
    with open(file_name, "r") as input_file:
        for line in input_file:
            priority += _find_priority(_find_common_item(line))
    return priority

print(find_priority("rucksack_organization.txt"))

def _find_group_badge(group):
    for item in group[0]:
        if item in group [1] and item in group[2]:
            return item

def identify_group_badges(file_name):
    i = 0
    priority = 0
    group = []
    with open(file_name, "r") as input_file:
        for line in input_file:
            i += 1
            group.append(line)
            if i % 3 == 0:
                priority += _find_priority(_find_group_badge(group))
                group = []
    return priority

print(identify_group_badges("group_badge.txt"))