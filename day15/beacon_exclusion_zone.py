import re

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

