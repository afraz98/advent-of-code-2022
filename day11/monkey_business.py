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
