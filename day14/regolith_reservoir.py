import os, time

"""
--- Day 14: Regolith Reservoir ---

The distress signal leads you to a giant waterfall! Actually, hang on - the signal seems like it's coming from the waterfall itself, 
and that doesn't make any sense. However, you do notice a little path that leads behind the waterfall.

Correction: the distress signal leads you behind a giant waterfall! There seems to be a large cave system here, 
and the signal definitely leads further inside.

As you begin to make your way deeper underground, you feel the ground rumble for a moment. 
Sand begins pouring into the cave! If you don't quickly figure out where the sand is going, you could quickly become trapped!

Fortunately, your familiarity with analyzing the path of falling material will come in handy here. 
You scan a two-dimensional vertical slice of the cave above you (your puzzle input) and discover that it is mostly air with structures made of rock.

Your scan traces the path of each solid rock structure and reports the x,y coordinates that form the shape of the path, 
where x represents distance to the right and y represents distance down. 
Each path appears as a single line of text in your scan. After the first point of each path, each point indicates the end of a straight horizontal or vertical line to be drawn from the previous point. For example:

498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9

This scan means that there are two paths of rock; 
the first path consists of two straight lines, and the second path consists of three straight lines. 
(Specifically, the first path consists of a line of rock from 498,4 through 498,6 and another line of rock from 498,6 through 496,6.)

The sand is pouring into the cave from point 500,0.

Drawing rock as #, air as ., and the source of the sand as +, this becomes:


  4     5  5
  9     0  0
  4     0  3
0 ......+...
1 ..........
2 ..........
3 ..........
4 ....#...##
5 ....#...#.
6 ..###...#.
7 ........#.
8 ........#.
9 #########.

Sand is produced one unit at a time, and the next unit of sand is not produced until the previous unit of sand comes to rest. 
A unit of sand is large enough to fill one tile of air in your scan.

A unit of sand always falls down one step if possible. If the tile immediately below is blocked (by rock or sand), 
the unit of sand attempts to instead move diagonally one step down and to the left. If that tile is blocked, the unit of sand 
attempts to instead move diagonally one step down and to the right. Sand keeps moving as long as it is able to do so, at each step trying to move down, 
then down-left, then down-right. If all three possible destinations are blocked, the unit of sand comes to rest and no longer moves, 
at which point the next unit of sand is created back at the source.

Using your scan, simulate the falling sand. How many units of sand come to rest before sand starts flowing into the abyss below?
"""
  
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
          self.grid[y][x] = "#"

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
    os.system('clear')
    
    # Recreate grid
    self.create_grid()

    for sand in self.dropped_sand:
      self.grid[sand[0]][sand[1]] = "o"

    for x in range(0, self.max_y+1):
      for y in range(0, self.max_x+1):
        print(self.grid[y][x], end="")
      print()
    pass

  def _drop_sand(self, x, y):
    
    while True:
      self.dropped_sand[-1] = (x,y)
      self.render()

      if y+1 > self.max_y:
        return (x, y+1)

      if self.grid[x][y+1] == ".":
        print("down")
        return self._drop_sand(x, y+1)
      elif self.grid[x-1][y+1] == ".":
        print("left")
        return self._drop_sand(x-1, y+1)
      elif self.grid[x+1][y+1] == ".":
        print("right")
        return self._drop_sand(x+1, y+1)
      else:
        print("cant move")
        return (x, y)

  def drop_sand(self):
    """
    Drop sand particle, updating grid to render particle as it drops

    Returns:
      (list, bool): Updated grid and completion status based on where the sand lands 
    """
    print("dropping new sand")
    self.dropped_sand.append((500 - self.min_x, 0))
    self.dropped_sand[-1] = self._drop_sand(self.dropped_sand[-1][0], self.dropped_sand[-1][1])
    if self.dropped_sand[-1][1] >= self.max_y:
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
      print(len(self.dropped_sand))
    return len(self.dropped_sand)-1

print(RegolithReservoir("test_regolith_reservoir.txt").simulate_sand())
