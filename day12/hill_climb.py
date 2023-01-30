import math

"""
--- Day 12: Hill Climbing Algorithm ---

You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above broken into a grid; 
the elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation, b is the next-lowest, 
and so on up to the highest elevation, z.

Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E). 
Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.

You'd like to reach E, but to save energy, you should do it in as few steps as possible. 
During each step, you can move exactly one square up, down, left, or right. 
To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher than the elevation of your current square; 
that is, if your current elevation is m, you could step to elevation n, but not to elevation o. 
(This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

For example:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:

v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^

In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<), or right (>). The location that should get the best signal is still E, and . marks unvisited squares.

This path reaches the goal in 31 steps, the fewest possible.

What is the fewest steps required to move from your current position to the location that should get the best signal?
"""

class Cell:
    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data

        self.f = 999.0
        self.g = 999.0
        self.h = 999.0
        self.parent_x = -1
        self.parent_y = -1
        pass

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)


grid = [[str(i) for i in line.strip("\n")] for line in open("hill_climb.txt", "r")]
width = len(grid[0])
height = len(grid)

start_x = 0
start_y = 0

for i in range(height):
    for j in range(width):
        if grid[i][j] == 'S':
            start_x = i
            start_y = j

end_x = 0
end_y = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'E':
            end_x = i
            end_y = j

def trace_path(cells, end_x, end_y):
    """
    Trace A* algorithm path, returning path length

    Args:
        cells (list): Cell data matrix
        end_x (int): Ending x coordinate
        end_y (int): Ending y coordinate

    Returns:
        (int): Path length
    """
    path_len = 0
    
    row = end_x
    col = end_y
    path = []
    while not (cells[row][col].parent_x == row and cells[row][col].parent_y == col):
        path.insert(0, cells[row][col])

        new_row = cells[row][col].parent_x 
        new_col = cells[row][col].parent_y

        row = new_row
        col = new_col

    path.insert(0, cells[row][col])
    while path != []:
        path.pop(0)
        path_len += 1
    
    return path_len


def climb_hill(start_x, start_y, end_x, end_y):
    """
    Modified A* search algorithm.

    Args:
        start_x (int): Starting x coordinate
        start_y (int): Starting y coordinate
        end_x (int): End x coordinate
        end_y (int): End y coordinate

    Returns:
        (int): Path length
    """
    grid[start_x][start_y] = 'a'
    grid[end_x][end_y] = 'z'

    open = []
    closed = [[False for i in range(width)] for i in range(height)]
    cells = [[None for i in range(width)] for i in range(height)]
    
    for i in range(height):
        for j in range(width):
            cells[i][j] = Cell(i, j, grid[i][j])

    cells[start_x][start_y].f = 0.0
    cells[start_x][start_y].g = 0.0
    cells[start_x][start_y].h = 0.0
    cells[start_x][start_y].parent_x = start_x
    cells[start_x][start_y].parent_y = start_y

    open.append(cells[start_x][start_y])

    while open != []:
        cell = open.pop(0)
        closed[cell.x][cell.y] = True

        # 'North' successor
        # Cell within grid bounds
        if 0 <= cell.x - 1 < height and 0 <= cell.y < width:

                # 'North' successor is destination cell?
                if cell.x - 1 == end_x and cell.y == end_y and ord(grid[cell.x - 1][cell.y]) - ord(grid[cell.x][cell.y]) <= 1:
                    # print("Found destination")
                    cells[cell.x - 1][cell.y].parent_x = cell.x
                    cells[cell.x - 1][cell.y].parent_y = cell.y
                    return trace_path(cells, end_x, end_y)

                # Successor not in closed list and path is 'unblocked'
                elif closed[cell.x - 1][cell.y] == False and ord(grid[cell.x - 1][cell.y]) - ord(grid[cell.x][cell.y]) <= 1:
                    g_new = cells[cell.x][cell.x].g + 1.0
                    h_new = math.sqrt((cell.x - end_x)*(cell.x - end_x)+(cell.y - end_y)*(cell.y - end_y))
                    f_new = g_new + h_new
                    
                    if cells[cell.x - 1][cell.y].f == 999.0 or cells[cell.x - 1][cell.y].f > f_new:
                        cells[cell.x - 1][cell.y].f = f_new
                        cells[cell.x - 1][cell.y].g = g_new
                        cells[cell.x - 1][cell.y].h = h_new
                        cells[cell.x - 1][cell.y].parent_x = cell.x
                        cells[cell.x - 1][cell.y].parent_y = cell.y
                        open.append(cells[cell.x - 1][cell.y])
        
        # 'South' successor
        # Cell within grid bounds
        if 0 <= cell.x + 1 < height and 0 <= cell.y < width:
                
                # 'South successor is desination cell?
                if cell.x + 1 == end_x and cell.y == end_y and ord(grid[cell.x + 1][cell.y]) - ord(grid[cell.x][cell.y]) <= 1:
                    # print("Found destination") 
                    cells[cell.x + 1][cell.y].parent_x = cell.x
                    cells[cell.x + 1][cell.y].parent_y = cell.y
                    return trace_path(cells, end_x, end_y)
                
                # Successor not in closed list and path is 'unblocked'
                elif closed[cell.x + 1][cell.y] == False and ord(grid[cell.x + 1][cell.y]) - ord(grid[cell.x][cell.y]) <= 1:
                    g_new = cells[cell.x][cell.x].g + 1.0
                    h_new = math.sqrt((cell.x - end_x)*(cell.x - end_x)+(cell.y - end_y)*(cell.y - end_y))
                    f_new = g_new + h_new
                    
                    if cells[cell.x + 1][cell.y].f == 999.0 or cells[cell.x + 1][cell.y].f > f_new:
                        cells[cell.x + 1][cell.y].f = f_new
                        cells[cell.x + 1][cell.y].g = g_new
                        cells[cell.x + 1][cell.y].h = h_new
                        cells[cell.x + 1][cell.y].parent_x = cell.x
                        cells[cell.x + 1][cell.y].parent_y = cell.y
                        open.append(cells[cell.x + 1][cell.y])

        # 'East' successor
        # Cell within grid bounds
        if 0 <= cell.x < height and 0 <= cell.y + 1 < width:
                
                # 'South successor is desination cell?
                if cell.x == end_x and cell.y + 1 == end_y and ord(grid[cell.x][cell.y + 1]) - ord(grid[cell.x][cell.y]) <= 1:
                    # print("Found destination")
                    cells[cell.x][cell.y + 1].parent_x = cell.x
                    cells[cell.x][cell.y + 1].parent_y = cell.y
                    return trace_path(cells, end_x, end_y)
                
                # Successor not in closed list and path is 'unblocked'
                elif closed[cell.x][cell.y + 1] == False and ord(grid[cell.x][cell.y + 1]) - ord(grid[cell.x][cell.y]) <= 1:
                    g_new = cells[cell.x][cell.x].g + 1.0
                    h_new = math.sqrt((cell.x - end_x)*(cell.x - end_x)+(cell.y - end_y)*(cell.y - end_y))
                    f_new = g_new + h_new
                    
                    if cells[cell.x][cell.y + 1].f == 999.0 or cells[cell.x][cell.y + 1].f > f_new:
                        cells[cell.x][cell.y + 1].f = f_new
                        cells[cell.x][cell.y + 1].g = g_new
                        cells[cell.x][cell.y + 1].h = h_new
                        cells[cell.x][cell.y + 1].parent_x = cell.x
                        cells[cell.x][cell.y + 1].parent_y = cell.y
                        open.append(cells[cell.x][cell.y + 1])

        # 'West' successor
        # Cell within grid bounds
        if 0 <= cell.x < height and 0 <= cell.y - 1 < width:
                
                # 'South successor is desination cell?
                if cell.x == end_x and cell.y - 1 == end_y and ord(grid[cell.x][cell.y - 1]) - ord(grid[cell.x][cell.y]) <= 1:
                    # print("Found destination") 
                    cells[cell.x][cell.y - 1].parent_x = cell.x
                    cells[cell.x][cell.y - 1].parent_y = cell.y
                    return trace_path(cells, end_x, end_y)
                
                # Successor not in closed list and path is 'unblocked'
                elif closed[cell.x][cell.y - 1] == False and ord(grid[cell.x][cell.y - 1]) - ord(grid[cell.x][cell.y]) <= 1:
                    g_new = cells[cell.x][cell.x].g + 1.0
                    h_new = math.sqrt((cell.x - end_x)*(cell.x - end_x)+(cell.y - end_y)*(cell.y - end_y))
                    f_new = g_new + h_new
                    
                    if cells[cell.x][cell.y - 1].f == 999.0 or cells[cell.x][cell.y - 1].f > f_new:
                        cells[cell.x][cell.y - 1].f = f_new
                        cells[cell.x][cell.y - 1].g = g_new
                        cells[cell.x][cell.y - 1].h = h_new
                        cells[cell.x][cell.y - 1].parent_x = cell.x
                        cells[cell.x][cell.y - 1].parent_y = cell.y
                        open.append(cells[cell.x][cell.y - 1])
    return 999

"""
--- Part Two ---

As you walk up the hill, you suspect that the Elves will want to turn this into a hiking trail. The beginning isn't very scenic, though; perhaps you can find a better starting point.

To maximize exercise while hiking, the trail should start as low as possible: elevation a. The goal is still the square marked E. However, the trail should still be direct, taking the fewest steps to reach its goal. So, you'll need to find the shortest path from any square at elevation a to the square marked E.

Again consider the example from above:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

Now, there are six choices for starting position (five marked a, plus the square marked S that counts as being at elevation a). If you start at the bottom-left square, you can reach the goal most quickly:

...v<<<<
...vv<<^
...v>E^^
.>v>>>^^
>^>>>>>^

This path reaches the goal in only 29 steps, the fewest possible.

What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal?
"""
starting_positions = []

for i in range(height):
    for j in range(width):
        if grid[i][j] == 'a':
            starting_positions.append((i,j))

print(min([climb_hill(start[0], start[1], end_x, end_y) for start in starting_positions]))
