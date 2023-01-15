from functools import cmp_to_key

"""
--- Day 13: Distress Signal ---

You climb the hill and again try contacting the Elves. However, you instead receive a signal you weren't expecting: a distress signal.

Your handheld device must still not be working properly; the packets from the distress signal got decoded out of order. You'll need to re-order the list of received packets (your puzzle input) to decode the message.

Your list consists of pairs of packets; pairs are separated by a blank line. You need to identify how many pairs of packets are in the right order.

For example:

[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]


If both values are integers, the lower integer should come first. If the left integer is lower than the right integer, the inputs are in the right order. 
If the left integer is higher than the right integer, the inputs are not in the right order. Otherwise, the inputs are the same integer; continue checking 
the next part of the input.

If both values are lists, compare the first value of each list, then the second value, and so on. 
If the left list runs out of items first, the inputs are in the right order. If the right list runs out of items first, the inputs are not in the right order. 
If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.

If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison. 
For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2].
"""

def _compare(a,b):
    if a < b:
        return 1
    if a > b:
        return -1
    return 0

def compare(data, other):
    print("Compare %s, %s" % (data, other))
    if type(data) == type(other) == int:
        return _compare(data, other)

    if type(data) != type(other):
        print("Type mismatch. Casting non-list type")
        if type(data) == int:
            return compare([data], other)
        return compare(data, [other])
    
    for l, r in zip(data, other):
        result = compare(l, r)
        if result != 0:
            return result
    return compare(len(data), len(other))

lines = [line.strip("\n") for line in open("distress_signal.txt", "r")]
lines = [line for line in lines if line != '']
pairs = [(lines[i], lines[i+1]) for i in range(0, len(lines)-1, 2)]

"""
What are the indices of the pairs that are already in the right order? 
(The first pair has index 1, the second pair has index 2, and so on.) 
In the above example, the pairs in the right order are 1, 2, 4, and 6; the sum of these indices is 13.
"""
print(sum([pairs.index(pair)+1 for pair in pairs if compare(eval(pair[0]), eval(pair[1])) == 1]))

"""
--- Part Two ---

Now, you just need to put all of the packets in the right order. Disregard the blank lines in your list of received packets.

The distress signal protocol also requires that you include two additional divider packets:

[[2]]
[[6]]

Using the same rules as before, organize all packets - the ones in your list of received packets as well as the two divider packets - into the correct order.

For the example above, the result of putting the packets in the correct order is:

[]
[[]]
[[[]]]
[1,1,3,1,1]
[1,1,5,1,1]
[[1],[2,3,4]]
[1,[2,[3,[4,[5,6,0]]]],8,9]
[1,[2,[3,[4,[5,6,7]]]],8,9]
[[1],4]
[[2]]
[3]
[[4,4],4,4]
[[4,4],4,4,4]
[[6]]
[7,7,7]
[7,7,7,7]
[[8,7,6]]
[9]

Afterward, locate the divider packets. To find the decoder key for this distress signal, 
you need to determine the indices of the two divider packets and multiply them together. (The first packet is at index 1, 
the second packet is at index 2, and so on.) In this example, the divider packets are 10th and 14th, and so the decoder key is 140.

Organize all of the packets into the correct order. What is the decoder key for the distress signal?
"""

packets = [line for line in lines if line != '']
packets.append('[[2]]')
packets.append('[[6]]')
packets = [eval(packet) for packet in packets]
packets = sorted(packets, key=cmp_to_key(compare), reverse=True)
print((packets.index([[2]])+1) * (packets.index([[6]])+1))