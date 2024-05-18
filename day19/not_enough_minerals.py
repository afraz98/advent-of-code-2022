def parse_input(filename):
  return [line for line in open(filename, 'r')]

def parse_blueprint(blueprint):
  ore, clay, obsidian, geode = (0, 0, 0, 0)
  ore_robots, clay_robots, obsidian_robots, geode_robots = 1, 0, 0, 0
  for minute in range(1,25):
    print("=== Minute %d === " % minute)
    if ore_robots > 0:
      ore += ore_robots
      print("%s ore-collecting robot collects 1 ore; you now have %d ore" % (ore_robots, ore))
  print()
  return 0

def solve_part_one(filename):
  return max([parse_blueprint(blueprint) for blueprint in parse_input(filename)])

print(solve_part_one("day19.txt"))