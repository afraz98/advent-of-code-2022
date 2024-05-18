class CPU:
    def __init__(self):
        self.counter = 1
        self.register = 1
        self.history = []
        self.instructions = []
        self.history.append(self.register)

    def parse_instructions(self, file_name):
        self.instructions = [line.strip("\n") for line in open(file_name, "r")]

    def execute_instructions(self):
        for instruction in self.instructions:
            instruction = instruction.split(" ")
            if instruction[0] == "noop":
                self.noop()
            elif instruction[0] == "addx":
                self.addx(int(instruction[-1]))

    def noop(self):
        self.counter += 1
        self.history.append(self.register)

    def addx(self, value):
        self.noop()
        self.noop()
        self.register += value
class CRT(CPU):
    def __init__(self):
        CPU.__init__(self)
        self.counter = 0
        self.crt = []

    def noop(self):
        self.render()
        self.counter += 1

    def addx(self, value):
        self.noop()
        self.noop()
        self.register += value

    def render(self):
        # print(self.sprite)
        # print(self.counter)

        if (self.counter % 40) - 1 <= self.register <= (self.counter % 40) + 1:
            print("#", end="")
        else:
            print(".", end="")
        
        if not self.counter % 40 and self.counter > 0:
            print("\n", end="")
        pass


crt = CRT()
crt.parse_instructions("crt.txt")
crt.execute_instructions()
