
# doubly linked, circular linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def build_list(cipher):
    nodes = []
    for element in cipher:
        current = Node(element)

        if current.value == 0:
            zero = current

        if nodes:
            nodes[-1].next = current
            current.prev = nodes[-1]
        nodes.append(current)

        # Make list circular
        nodes[0].prev = nodes[-1]
        nodes[-1].next = nodes[0]
    return zero, nodes

def mix(nodes):
    for node in nodes:
        steps = node.value % (len(nodes) - 1)
        if steps != 0:
            # Remove node from linked list
            node.prev.next = node.next
            node.next.prev = node.prev

            previous = node.prev
            
            # Look for new position
            for _ in range(steps):
                previous = previous.next

            node.prev = previous
            node.next = previous.next
            node.prev.next = node
            node.next.prev = node                
    pass

def solve(zero, nodes):
    ans = 0
    
    for _ in range(3):
        for _ in range(1000 % len(nodes)):
            zero = zero.next
        ans += zero.value
    return ans


cipher = [int(line.strip('\n')) for line in open("grove_positioning_system.txt", "r")]
zero, nodes = build_list(cipher)
mix(nodes)
print(solve(zero, nodes))

decryption_key = 811589153

def build_modified_list(cipher):
    nodes = []
    for element in cipher:
        current = Node(element * decryption_key)

        if current.value == 0:
            zero = current

        if nodes:
            nodes[-1].next = current
            current.prev = nodes[-1]
        nodes.append(current)

        # Make list circular
        nodes[0].prev = nodes[-1]
        nodes[-1].next = nodes[0]
    return zero, nodes

cipher = [int(line.strip('\n')) for line in open("grove_positioning_system.txt", "r")]
zero, nodes = build_modified_list(cipher)

for _ in range(10):
    mix(nodes)

print(solve(zero, nodes))