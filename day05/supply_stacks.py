def _parse_stacks(line, n):
        return [line[i:i+n].strip(" ") for i in range(0, len(line), n)]

def _parse_supply_stacks(file_name):
        input = []
        stacks = []
        with open(file_name, "r") as input_file:
                for line in input_file:
                        if line == "\n":
                                break
                        input.append(_parse_stacks(line.strip('\n'), 4))
        for i in range (0,len(input[0])):
                stacks.append([])
        
        for line in input:
                for index, elt in enumerate(line):
                        if "[" in elt:
                                stacks[index].append(elt)
        return stacks

def _parse_instructions(file_name):
        instructions = []
        with open(file_name, "r") as input_file:
                for line in input_file:
                        if "move" in line:
                                instructions.append(line.strip())
        return instructions

def _parse_input(file_name):
        return _parse_supply_stacks(file_name), _parse_instructions(file_name)

def _perform_instruction(stacks, n, src, dst):
        # Put N elements from <src> stack into <dst> stack

        for i in range(n):
                stacks[dst].insert(0, stacks[src].pop(0))
        pass

def manipulate_stacks(stacks, instructions):
        for instruction in instructions:
                parsed_instruction = [int(c) for c in instruction.split() if c.isdigit()]
                _perform_instruction(stacks, parsed_instruction[0], parsed_instruction[1]-1, parsed_instruction[2]-1)
        return ''.join([stack[0].strip("[]") for stack in stacks])

stacks, instructions = _parse_input("supply_stacks.txt")
print(manipulate_stacks(stacks, instructions))

def _perform_instruction_part_two(stacks, n, src, dst):
        # Put N elements from <src> stack into <dst> stack (PRESERVING ORDER)
        stacks[dst] = [stacks[src].pop(0) for i in range(n)] + stacks[dst]
        pass

def manipulate_stacks_part_two(stacks, instructions):
        for instruction in instructions:
                parsed_instruction = [int(c) for c in instruction.split() if c.isdigit()]
                _perform_instruction_part_two(stacks, parsed_instruction[0], parsed_instruction[1]-1, parsed_instruction[2]-1)
        return ''.join([stack[0].strip("[]") for stack in stacks])

stacks, instructions = _parse_input("supply_stacks.txt")
print(manipulate_stacks_part_two(stacks, instructions))