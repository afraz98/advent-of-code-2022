sizes = {}
stack = []

size_limit = 100000

def _parse_commands(file_name):
  for index, input in enumerate([line for line in open(file_name, "r")]):
    input = input.replace("$ ", "")
    if input[0:3] != "dir" and input[0:2] != "ls":
      if input[0:2] == "cd" and ".." in input:
        stack.pop()
      elif input[0:2] == "cd":
        stack.append(index)
        sizes[index] = 0
      else:
        for dir in stack:
          sizes[dir] += int(input.split(" ")[0])

_parse_commands("no_space.txt")
print(sum([sizes[i] for i in sizes if sizes[i] <= size_limit]))

total_space = 70000000
required_space = 30000000
free_space = total_space - max([sizes[i] for i in sizes])
needed_space = required_space - free_space
potential_deletes = [sizes[i] for i in sizes if sizes[i] >= needed_space]
print(min(potential_deletes))