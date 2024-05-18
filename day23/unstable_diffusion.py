class Elf:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.possible_moves = ['N', 'S', 'E', 'W']

    def attempt_to_move(self):
        pass


def parse_input(filename):
    return [line.strip("\n") for line in open(filename, "r")]


def render_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            print(grid[y][x], end="")
        print()


def find_elves(grid):
    elves = set()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "#":
                elves.add((y, x))
    return elves


def simulate_round(elves):
    pass


def solve(filename):
    grid = parse_input(filename)
    elves = find_elves(grid)
    render_grid(grid)


solve("test_unstable_diffusion.txt")

