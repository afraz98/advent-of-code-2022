import math

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

starting_positions = []

for i in range(height):
    for j in range(width):
        if grid[i][j] == 'a':
            starting_positions.append((i,j))

print(min([climb_hill(start[0], start[1], end_x, end_y) for start in starting_positions]))
