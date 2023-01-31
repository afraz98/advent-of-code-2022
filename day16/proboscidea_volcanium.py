"""
--- Day 16: Proboscidea Volcanium ---

The sensors have led you to the origin of the distress signal: yet another handheld device, just like the one the Elves
gave you.

However, you don't see any Elves around; instead, the device is surrounded by elephants! They must have gotten lost in
these tunnels, and one of the elephants apparently figured out how to turn on the distress signal.

The ground rumbles again, much stronger this time. What kind of cave is this, exactly? You scan the cave with your
handheld device; it reports mostly igneous rock, some ash, pockets of pressurized gas, magma...

this isn't just a cave, it's a volcano!

You need to get the elephants out of here, quickly. Your device estimates that you have 30 minutes before the volcano
erupts, so you don't have time to go back out the way you came in.

You scan the cave for other options and discover a network of pipes and pressure-release valves. You aren't sure
how such a system got into a volcano, but you don't have time to complain; your device produces a report
(your puzzle input) of each valve's flow rate if it were opened (in pressure per minute) and the tunnels you could use
to move between the valves.

There's even a valve in the room you and the elephants are currently standing in labeled AA. 
You estimate it will take you one minute to open a single valve and one minute to follow any tunnel from one valve
to another. What is the most pressure you could release?

For example, suppose you had the following scan output:

Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II

All the valves begin closed. You start at valve AA, but it must be damaged or jammed or something: its flow rate is
0, so there's no point in opening it.

However, you could spend one minute moving to valve BB and another minute opening it;
doing so would release pressure during the remaining 28 minutes at a flow rate of 13, a total eventual pressure release
of 28 * 13 = 364.

Then, you could spend your third minute moving to valve CC and your fourth minute opening it, providing an additional
26 minutes of eventual pressure release at a flow rate of 2, or 52 total pressure released by valve CC.

Making your way through the tunnels like this, you could probably open many or all of the valves by the time 30 minutes
have elapsed. However, you need to release as much pressure as possible, so you'll need to be methodical.

Instead, consider this approach:

== Minute 1 ==
No valves are open.
You move to valve DD.

== Minute 2 ==
No valves are open.
You open valve DD.

== Minute 3 ==
Valve DD is open, releasing 20 pressure.
You move to valve CC.

== Minute 4 ==
Valve DD is open, releasing 20 pressure.
You move to valve BB.

== Minute 5 ==
Valve DD is open, releasing 20 pressure.
You open valve BB.

== Minute 6 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve AA.

== Minute 7 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve II.

== Minute 8 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve JJ.

== Minute 9 ==
Valves BB and DD are open, releasing 33 pressure.
You open valve JJ.

== Minute 10 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve II.

== Minute 11 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve AA.

== Minute 12 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve DD.

== Minute 13 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve EE.

== Minute 14 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve FF.

== Minute 15 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve GG.

== Minute 16 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve HH.

== Minute 17 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You open valve HH.

== Minute 18 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve GG.

== Minute 19 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve FF.

== Minute 20 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve EE.

== Minute 21 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You open valve EE.

== Minute 22 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You move to valve DD.

== Minute 23 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You move to valve CC.

== Minute 24 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You open valve CC.

== Minute 25 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 26 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 27 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 28 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 29 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 30 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

This approach lets you release the most pressure possible in 30 minutes with this valve layout, 1651.
Work out the steps to release the most pressure in 30 minutes. What is the most pressure you can release?
"""

# Maximize path quality in a given max_time minutes
# How many nodes can be reached in max_time minutes?
# Can you try every valid path?
# Depth-first search


class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.adj_list = []


def _parse_input(filename):
    return [line.split(";") for line in open(filename, "r")]


def build_graph(puzzle_input):
    adj_list = {}
    values = {}

    for line in puzzle_input:
        current_chamber = line[0][6:8]
        pressure_rate = int(line[0][23:].strip("=,;"))
        paths = line[1][23:].strip(" \n").split(",")

        # Add node to nodes list
        node = Node(current_chamber, pressure_rate)
        values[node.name] = node.value
        adj_list[node.name] = []

        for path in paths:
            adj_list[node.name].append(path.strip(" "))
    return adj_list, values


class Traversal:
    def __init__(self, filename, max_moves):
        self.filename = filename
        self.max_moves = max_moves
        self.value = -1

    def _depth_first_search(self, node, visited, gain, moves, values, adj_list):
        print(node, moves, self.value, gain)
        input()
        if node == "AA":
            self.value = max(self.value, gain)
        for neighbor in adj_list[node]:
            if moves - 1 >= 0:
                self._depth_first_search(
                    neighbor,
                    visited | set(neighbor),
                    gain + ((node not in visited) * values[neighbor] * (moves - 2)),
                    moves - 1 - (node not in visited),
                    values,
                    adj_list
                )
            else:
                break
        pass

    def traverse_graph(self, start_node, values, adj_list):
        visited = set(start_node)
        self._depth_first_search(start_node, visited, values[start_node], self.max_moves, values, adj_list)
        return self.value

    def open_valves(self):
        adj_list, values = build_graph(_parse_input(self.filename))
        self.traverse_graph("AA", values, adj_list)


Traversal("test_proboscidea_volcanium.txt", 30).open_valves()
