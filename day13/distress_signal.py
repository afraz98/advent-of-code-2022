from functools import cmp_to_key

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

print(sum([pairs.index(pair)+1 for pair in pairs if compare(eval(pair[0]), eval(pair[1])) == 1]))

packets = [line for line in lines if line != '']
packets.append('[[2]]')
packets.append('[[6]]')
packets = [eval(packet) for packet in packets]
packets = sorted(packets, key=cmp_to_key(compare), reverse=True)
print((packets.index([[2]])+1) * (packets.index([[6]])+1))