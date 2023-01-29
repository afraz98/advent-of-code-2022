import re

"""
--- Day 15: Beacon Exclusion Zone ---

You feel the ground rumble again as the distress signal leads you to a large network of subterranean tunnels. 
You don't have time to search them all, but you don't need to:  your pack contains a set of deployable sensors that you imagine were 
originally built to locate lost Elves.

The sensors aren't very powerful, but that's okay; your handheld device indicates that you're close enough to the source of the 
distress signal to use them. You pull the emergency sensor system out of your pack, hit the big button on top, and the sensors zoom off down the tunnels.

Once a sensor finds a spot it thinks will give it a good reading, it attaches itself to a hard surface
and begins monitoring for the nearest signal source beacon. Sensors and beacons always exist at integer coordinates. 
Each sensor knows its own position and can determine the position of a beacon precisely; 
however, sensors can only lock on to the one beacon closest to the sensor as measured by the Manhattan distance. 
(There is never a tie where two beacons are the same distance to a sensor.)

It doesn't take long for the sensors to report back their positions and closest beacons (your puzzle input). For example:

Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3

So, consider the sensor at 2,18; the closest beacon to it is at -2,15. For the sensor at 9,16, the closest beacon to it is at 10,16.
Drawing sensors as S and beacons as B, the above arrangement of sensors and beacons looks like this:

               1    1    2    2
     0    5    0    5    0    5
 0 ....S.......................
 1 ......................S.....
 2 ...............S............
 3 ................SB..........
 4 ............................
 5 ............................
 6 ............................
 7 ..........S.......S.........
 8 ............................
 9 ............................
10 ....B.......................
11 ..S.........................
12 ............................
13 ............................
14 ..............S.......S.....
15 B...........................
16 ...........SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....

This isn't necessarily a comprehensive map of all beacons in the area, though. Because each sensor only identifies its closest beacon, 
if a sensor detects a beacon, you know there are no other beacons that close or closer to that sensor. 
There could still be beacons that just happen to not be the closest beacon to any sensor. Consider the sensor at 8,7:

               1    1    2    2
     0    5    0    5    0    5
-2 ..........#.................
-1 .........###................
 0 ....S...#####...............
 1 .......#######........S.....
 2 ......#########S............
 3 .....###########SB..........
 4 ....#############...........
 5 ...###############..........
 6 ..#################.........
 7 .#########S#######S#........
 8 ..#################.........
 9 ...###############..........
10 ....B############...........
11 ..S..###########............
12 ......#########.............
13 .......#######..............
14 ........#####.S.......S.....
15 B........###................
16 ..........#SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....

This sensor's closest beacon is at 2,10, and so you know there are no beacons that close or closer (in any positions marked #).

None of the detected beacons seem to be producing the distress signal, so you'll need to work out where the distress beacon 
is by working out where it isn't. For now, keep things simple by counting the positions where a beacon cannot possibly be along just a single row.

So, suppose you have an arrangement of beacons and sensors like in the example above and, just in the row where y=10, 
you'd like to count the number of positions a beacon cannot possibly exist. The coverage from all sensors near that row looks like this:

                 1    1    2    2
       0    5    0    5    0    5
 9 ...#########################...
10 ..####B######################..
11 .###S#############.###########.

In this example, in the row where y=10, there are 26 positions where a beacon cannot be present.
Consult the report from the sensors you just deployed. In the row where y=2000000, how many positions cannot contain a beacon?
"""

# Set-based approach using manhattan distance in a single dimension to determine the number of points / beacons 
# fitting the line y = 2000000


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def parse_reports(filename):
    reports = []
    for input in [[int(i) for i in re.findall(r'-?[0-9]+', line.strip("\n"))] for line in open(filename, "r")]:
        sensor_x, sensor_y, beacon_x, beacon_y = input
        reports.append((sensor_x, sensor_y, beacon_x, beacon_y))
    return reports


def find_positions_no_beacon(reports, y):
    beacons_not_found = set()
    beacons_found = set()

    for report in reports:
        sensor_x, sensor_y, beacon_x, beacon_y = report
        _manhattan_distance = manhattan_distance(sensor_x, beacon_x, sensor_y, beacon_y)
        if sensor_y - _manhattan_distance <= y <= sensor_y + _manhattan_distance:
            if beacon_y == y:
                beacons_found.add((beacon_x, beacon_y))
            for x in range(sensor_x - (_manhattan_distance - abs(y - sensor_y)),
                           sensor_x + (_manhattan_distance - abs(y - sensor_y)+1)):
                beacons_not_found.add((x, y))
        pass
    return beacons_not_found - beacons_found


# Part 1 solution
print(len(find_positions_no_beacon(parse_reports("beacon_exclusion_zone.txt"), 2000000)))

"""
--- Part Two ---

Your handheld device indicates that the distress signal is coming from a beacon nearby. 
The distress beacon is not detected by any sensor, but the distress beacon must have x and y coordinates each no lower than 0 and no larger than 4000000.

To isolate the distress beacon's signal, you need to determine its tuning frequency, which can be found by multiplying its 
x coordinate by 4000000 and then adding its y coordinate.

In the example above, the search space is smaller: instead, the x and y coordinates can each be at most 20. 
With this reduced search area, there is only a single position that could have a beacon: x=14, y=11. The tuning frequency for this distress beacon is 56000011.

Find the only possible position for the distress beacon. What is its tuning frequency?
"""

# Check all circles existing in the Manhattan geometry of a given sensor.
# Look for points that lie outside all given Manhattan circles


def manhattan_edges(x: int, y: int, dist: int, limit: int):
    for offset in range(dist):
        inv_offset = dist - offset
        if any([x + offset < 0, x + offset > limit, x - offset < 0, x - offset > limit,
                x + inv_offset < 0, x + inv_offset > limit, x - inv_offset < 0, x - inv_offset > limit,
                y + offset < 0, y + offset > limit, y - offset < 0, y - offset > limit,
                y + inv_offset < 0, y + inv_offset > limit, y - inv_offset < 0, y - inv_offset > limit]):
            continue
        yield x + offset, y + inv_offset
        yield x + inv_offset, y - offset
        yield x - offset, y - inv_offset
        yield x - inv_offset, y + offset
    yield -1, -1


def in_range(x, y, reports):
    for report in reports:
        sensor_x, sensor_y, beacon_x, beacon_y = report
        if manhattan_distance(sensor_x, sensor_y, x, y) <= manhattan_distance(sensor_x, sensor_y, beacon_x, beacon_y):
            return True
    return False


def find_tuning_frequency(reports, max_coord):
    for report in reports:
        sensor_x, sensor_y, beacon_x, beacon_y = report
        outsiders = manhattan_edges(sensor_x, sensor_y,
                                    manhattan_distance(sensor_x, sensor_y, beacon_x, beacon_y) + 1, max_coord)

        for _ in range(manhattan_distance(sensor_x, sensor_y, beacon_x, beacon_y) * 4):
            test_coord_x, test_coord_y = next(outsiders)
            if (test_coord_x, test_coord_y) == (-1, -1):
                break
            if not (in_range(test_coord_x, test_coord_y, reports)):
                return (test_coord_x * max_coord) + test_coord_y
    return -1


print(find_tuning_frequency(parse_reports("beacon_exclusion_zone.txt"), 4000000))

