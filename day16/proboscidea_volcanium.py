# Maximize path quality in a given <max_time> minutes
# How many nodes can be reached in <max_time> minutes?
# It takes one minute to move between nodes, one minute to open a valve
# Can you try every valid path?
# Depth-first search

def traverse_nodes(current_node, moves, flow_rate, pressure):
    pass

def solve_part_one(filename):
    nodes = {}
    input = [line.split() for line in open(filename, 'r')]
    for line in input:
        name = line[1]
        flow_rate = int(line[4].replace(";", "").split("=")[1])
        neighbors = [elem.replace(",", "") for elem in line[9:]]
        nodes[name] = {} 
        nodes[name]["flow-rate"] = flow_rate
        nodes[name]["neighbors"] = neighbors
    print(nodes)
    traverse_nodes("AA", 30, 0, 0)

solve_part_one("test_proboscidea_volcanium.txt")
