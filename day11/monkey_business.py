"""
--- Day 11: Monkey in the Middle ---

As you finally start making your way upriver, you realize your pack is much lighter than you remember.
Just then, one of the items from your pack goes flying overhead. Monkeys are playing Keep Away with your missing things!

To get your stuff back, you need to be able to predict where the monkeys will throw your items. After some careful
observation, you realize the monkeys operate based on how worried you are about each item.

You take some notes (your puzzle input) on the items each monkey currently has, how worried you are about those items,
and how the monkey makes decisions based on your worry level.

Each monkey has several attributes:

    1. Starting items lists your worry level for each item the monkey is currently holding in the order they will be
        inspected.
    2. Operation shows how your worry level changes as that monkey inspects an item. (An operation like new = old * 5
        means that your worry level after the monkey inspected the item is five times whatever your worry level was
        before inspection.)
    3. Test shows how the monkey uses your worry level to decide where to throw an item next.
        - If true shows what happens with an item if the Test was true.
        - If false shows what happens with an item if the Test was false.

After each monkey inspects an item but before it tests your worry level, your relief that the monkey's inspection didn't
 damage the item causes your worry level to be divided by three and rounded down to the nearest integer.

The monkeys take turns inspecting and throwing items. On a single monkey's turn, it inspects and throws all of the items
 it is holding one at a time and in the order listed. Monkey 0 goes first, then monkey 1, and so on until each monkey
 has had one turn. The process of each monkey taking a single turn is called a round.

When a monkey throws an item to another monkey, the item goes on the end of the recipient monkey's list. A monkey that
starts a round with no items could end up inspecting and throwing many items by the time its turn comes around.
If a monkey is holding no items at the start of its turn, its turn ends.
"""

class Monkey():
    def __init__(
        self,
        id = 0, 
        items=[], 
        operation="", 
        test=1,
        is_true=0,
        is_false=0
    ):
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        
        self.is_true = is_true
        self.is_false = is_false
        self.items_inspected = 0
        pass

    def increase_worry(self, index):
        self.items_inspected += 1
        old = self.items[index]
        self.items[index] = eval(self.operation)
    
    def decrease_worry(self, index, factor):
        # Part 1
        # self.items[index] = self.items[index] // 3

        # Part 2
        self.items[index] = self.items[index] % factor

    def test_item(self, index):
        return self.items[index] % self.test == 0

    def find_throw_target(self, index):
        if self.test_item(index):
            return self.is_true
        return self.is_false

    def perform_round(self):
        pass

    def __str__(self):
        return "Monkey %s: %s" % (str(self.id), str(self.items)) 

    
monkeys = []

# Divide item worry level by common denominator of 'inspection' numbers for part 2
common_denominator = 1

# Parse input for monkeys
input = [line.strip("\n\t ") for line in open("monkey_business.txt", "r")]

for line in input:    
    if line[:6] == "Monkey":
        monkeys.append(Monkey(id=len(monkeys)))
    if line[:14] == "Starting items":
        monkeys[-1].items = [int(i) for i in line[15:].strip(" \n").split(",")]
    if line[:9] == "Operation":
        monkeys[-1].operation = line[17:]
    if "Test" in line:
        denom = int(''.join(c for c in line if c.isdigit()))
        monkeys[-1].test = denom
        common_denominator = common_denominator * denom
    if "true" in line:
        monkeys[-1].is_true = int(''.join(c for c in line if c.isdigit()))
    if "false" in line:
        monkeys[-1].is_false = int(''.join(c for c in line if c.isdigit()))

print(common_denominator)

def perform_round():
    for monkey in monkeys:
        print("Monkey %d:" % monkey.id)
        items_to_remove = []
        for index in range(len(monkey.items)):
            # Inspect item
            print("\tMonkey %d inspects an item with worry level of %d." % (monkey.id, monkey.items[index]))
            monkey.increase_worry(index)

            # Perform operation on item
            print("\t\tWorry level increases to %d." % monkey.items[index])

            # Decrease worry level
            monkey.decrease_worry(index, common_denominator)
            print("\t\tMonkey gets bored with the item. Worry level decreased to %d." % monkey.items[index])
            
            # Find throw target
            print("\t\tCurrent worry level is %s divisible by %d." % ("" if monkey.test_item(index) else "not", monkey.test))
            throw_target = monkey.find_throw_target(index)

            # Throw item
            print("\t\tItem with worry level %d is thrown to Monkey %d." % (monkey.items[index], throw_target))
            monkeys[throw_target].items.append(monkey.items[index])
            items_to_remove.append(index)
        
        monkey.items = [i for j, i in enumerate(monkey.items) if j not in items_to_remove]
    
    for monkey in monkeys:
        print(str(monkey))
    pass


rounds = 10000
for _ in range(rounds):
    perform_round()

for monkey in monkeys:
    print("Monkey %d inspected %d items" % (monkey.id, monkey.items_inspected))
