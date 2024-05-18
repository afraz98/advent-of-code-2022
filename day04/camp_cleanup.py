def _range(start, stop):
    if start != stop:
        return list(range(start, stop+1))
    return [start]

def _find_pair_subset(line):
    assignments = [set(_range(int(i.split("-")[0]), int(i.split("-")[1]))) for i in line.split(",")]
    return assignments[0] <= assignments[1] or assignments[1] <= assignments[0]

def find_subsets(file_name):
    count = 0
    with open(file_name, "r") as input_file:
        for line in input_file:
            if _find_pair_subset(line.strip("\n")):
                count += 1
    return count

print(find_subsets("test_camp_cleanup.txt"))

def _find_pair_overlap(line):
    assignments = [set(_range(int(i.split("-")[0]), int(i.split("-")[1]))) for i in line.split(",")]
    return assignments[0] & assignments[1] != set()

def find_overlap(file_name):
    count = 0
    with open(file_name, "r") as input_file:
        for line in input_file:
            if _find_pair_overlap(line.strip("\n")):
                count += 1
    return count

print(find_overlap("camp_cleanup.txt"))