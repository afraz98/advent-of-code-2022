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
        test=1
    ):
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test

        self.throw_test = False
        
        pass

    def test_item(self, item):
        # Perform throw test
        self.throw_test = (item % self.test == 0)

        # Increase worry
        self.increase_worry(item)

        # Divide item worry by 3
        item = item // 3

    def throw(self, monkey):
        pass

    def __str__(self):
        return "Monkey %s\nItems: %s\nTest: %s\nOperation: %s\n" % (str(self.id), str(self.items), str(self.test), str(self.operation)) 

    
monkeys = []

# Parse input for monkeys
input = [line.strip("\n\t ") for line in open("test_monkey_business.txt", "r")]

for line in input:
    if line[:6] == "Monkey":
        monkeys.append(Monkey(id=len(monkeys)))
        pass
    if line[:14] == "Starting items":
        monkeys[-1].items = [int(i) for i in line[15:].strip(" \n").split(",")]
    if line[:9] == "Operation":
        monkeys[-1].operation = line[11:]

for monkey in monkeys:
    print(str(monkey))

