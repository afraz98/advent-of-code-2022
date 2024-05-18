import os, time

def _range(start, end):
  """
  Generate all values between start and end 

  Args:
    start (int): Start value
    end (int): End value

  Returns:
    (list): All values between [start, end]
  """
  return [i for i in range(end, start+1)] if start >= end else [i for i in range(start, end+1)]

class RegolithReservoir:
  """
  Simulator class for Regolith Reservoir problem.

  Attributes:
    min_x (int): Minimum x coordinate
    max_x (int): Maximum x coordinate
    min_y (int): Minimum y coordinate
    grid (list): Coordinate grid displaying reservoir
  """
  def __init__(self, filename):
    self.filename = filename

    self.grid = []
    self.dropped_sand = []
    self.create_grid()

    self.complete = False
    pass

  def _draw_lines(self, line):
    line_segments = list(zip(line, line[1:]))

    for point_a, point_b in line_segments:
      for x in _range(point_a[1], point_b[1]):
        for y in _range(point_a[0], point_b[0]):
          self.grid[x][y] = "#"

  def draw_lines(self, lines):
      for line in lines:
        self._draw_lines(line)

  def create_grid(self):
    lines = [[eval(point) for point in line.strip("\n").replace(" ", "").split("->")] for line in open(self.filename, "r")]

    self.min_x = int(min([min([point[0] for point in line]) for line in lines]))
    # Normalize x values
    for line in range(len(lines)):
      for point in range(len(lines[line])):
        lines[line][point] = (lines[line][point][0] - self.min_x, lines[line][point][1])

    self.min_y = int(min([min([point[1] for point in line]) for line in lines]))
    self.max_x = int(max([max([point[0] for point in line]) for line in lines]))
    self.max_y = int(max([max([point[1] for point in line]) for line in lines]))
    
    self.grid = [["." for x in range(0, self.max_x + 1)] for y in range(0, self.max_y + 1)]
    self.draw_lines(lines)

  def render(self):
    time.sleep(.2)
    # os.system('clear')
    
    # Recreate grid
    self.create_grid()

    for sand in self.dropped_sand:
      self.grid[sand[0]][sand[1]] = "o"

    for x in range(0, self.max_y+1):
      for y in range(0, self.max_x+1):
        print(self.grid[x][y], end="")
      print()
    pass

  def _drop_sand(self, x, y):
    while True:
      self.dropped_sand[-1] = (x,y)

      if x+1 > self.max_y:
        return (x, y)

      if self.grid[x+1][y] == ".":
        return self._drop_sand(x+1, y)
      elif self.grid[x+1][y-1] == ".":
        return self._drop_sand(x+1, y-1)
      elif self.grid[x+1][y+1] == ".":
        return self._drop_sand(x+1, y+1)
      return (x, y)

  def drop_sand(self):
    """
    Drop sand particle, updating grid to render particle as it drops

    Returns:
      (list, bool): Updated grid and completion status based on where the sand lands 
    """
    print("dropping new sand")
    self.dropped_sand.append((0, 500 - self.min_x))
    self.dropped_sand[-1] = self._drop_sand(self.dropped_sand[-1][0], self.dropped_sand[-1][1])
    if self.dropped_sand[-1][0] >= self.max_y:
      self.complete = True

  def simulate_sand(self):
    """
    Simulate sand particles falling, returning the number of particles that come to rest 
    before sand starts to fall out of the designated area.

    Args:
      filename (str): Filename of file containing input

    Returns:
      (int): The number of particles that come to rest before sand starts to fall out of the designated area
    """
    
    while not self.complete:
      self.drop_sand()
      if not self.complete:
        self.render()
      print(len(self.dropped_sand))
    return len(self.dropped_sand)-1

# print(RegolithReservoir("regolith_reservoir.txt").simulate_sand())

class RegolithContainer:
  """
  Simulator class for Regolith Reservoir problem (part 2).

  Attributes:
    min_x (int): Minimum x coordinate
    max_x (int): Maximum x coordinate
    min_y (int): Minimum y coordinate
    grid (list): Coordinate grid displaying reservoir
  """
  def __init__(self, filename):
    self.filename = filename

    self.grid = []
    self.dropped_sand = []
    self.create_grid()

    self.complete = False
    pass

  def _draw_lines(self, line):
    line_segments = list(zip(line, line[1:]))

    for point_a, point_b in line_segments:
      for x in _range(point_a[1], point_b[1]):
        for y in _range(point_a[0], point_b[0]):
          self.grid[x][y] = "#"

  def draw_lines(self, lines):
      for line in lines:
        self._draw_lines(line)

      for x in range(self.min_x, self.max_x):
        for y in range(self.max_y, self.max_y):
          self.grid[x][y] = "#"

  def create_grid(self):
    lines = [[eval(point) for point in line.strip("\n").replace(" ", "").split("->")] for line in open(self.filename, "r")]

    self.min_x = int(min([min([point[0] for point in line]) for line in lines])) - 34
    self.min_y = int(min([min([point[1] for point in line]) for line in lines]))
    self.max_x = int(max([max([point[0] for point in line]) for line in lines])) + 100
    self.max_y = int(max([max([point[1] for point in line]) for line in lines])) + 1
    
    self.grid = [["." for x in range(0, self.max_x + 1)] for y in range(0, self.max_y + 1)]
    self.draw_lines(lines)

  def render(self):
    time.sleep(.1)
    # os.system('clear')
    
    # Recreate grid
    self.create_grid()

    for sand in self.dropped_sand:
      self.grid[sand[0]][sand[1]] = "o"

    for x in range(0, self.max_y+1):
      for y in range(self.min_x, self.max_x+1):
        print(self.grid[x][y], end="")
      print()
    pass

  def _drop_sand(self, x, y):
    while True:
      self.dropped_sand[-1] = (x, y)

      if x+1 > self.max_y:
        return (x, y)

      if self.grid[x+1][y] == ".":
        return self._drop_sand(x+1, y)
      elif self.grid[x+1][y-1] == ".":
        return self._drop_sand(x+1, y-1)
      elif self.grid[x+1][y+1] == ".":
        return self._drop_sand(x+1, y+1)
      return (x, y)

  def drop_sand(self):
    """
    Drop sand particle, updating grid to render particle as it drops

    Returns:
      (list, bool): Updated grid and completion status based on where the sand lands 
    """
    self.dropped_sand.append((0, 500))
    self.dropped_sand[-1] = self._drop_sand(self.dropped_sand[-1][0], self.dropped_sand[-1][1])
    if self.dropped_sand[-1][0] == 0 and self.dropped_sand[-1][1] == 500:
      self.complete = True

  def simulate_sand(self):
    """
    Simulate sand particles falling, returning the number of particles that come to rest 
    before sand starts to fall out of the designated area.

    Args:
      filename (str): Filename of file containing input

    Returns:
      (int): The number of particles that come to rest before sand starts to fall out of the designated area
    """
    
    while not self.complete:
      self.drop_sand()
      if not self.complete:
        self.render()
    return len(self.dropped_sand)

print(RegolithContainer("regolith_reservoir.txt").simulate_sand())
