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
            print(instruction)
            instruction = instruction.split(" ")
            if instruction[0] == "noop":
                cpu.noop()
            elif instruction[0] == "addx":
                cpu.addx(int(instruction[-1]))

    def noop(self):
        self.counter += 1
        self.history.append(self.register)
        print("cycle %d: X = %d" % (self.counter, self.register))

    def addx(self, value):
        self.noop()
        self.noop()
        self.register += value


cpu = CPU()
cpu.parse_instructions("crt.txt")
cpu.execute_instructions()
print([i*cpu.history[i] for i in [20, 60, 100, 140, 180, 220]])
print(sum(i * cpu.history[i] for i in [20, 60, 100, 140, 180, 220]))
