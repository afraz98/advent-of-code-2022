data = [line.strip("\n") for line in open("tree_house.txt", "r")]
width = len(data[0])
height = len(data)


def trees_visible():
    visible_trees = 0
    visible = [[False for i in row] for row in data]

    for i in range(width):
        tallest = '-1'
        for j in range(height):
            if data[i][j] > tallest:
                tallest = data[i][j]
                visible[i][j] = True
        tallest = '-1'
        for j in reversed(range(height)):
            if data[i][j] > tallest:
                tallest = data[i][j]
                visible[i][j] = True
            pass

    for j in range(height):
        tallest = '-1'
        for i in range(width):
            if data[i][j] > tallest:
                tallest = data[i][j]
                visible[i][j] = True
        tallest = '-1'
        for i in reversed(range(width)):
            if data[i][j] > tallest:
                tallest = data[i][j]
                visible[i][j] = True

    for i in range(height):
        for j in range(width):
            if visible[i][j]:
                visible_trees += 1
    return visible_trees

for x in range(width):
        print(data[x])


def calculate_scenic_score(data_entry, x, y):
    left = 0
    right = 0
    up = 0
    down = 0

    print("left")
    for i in reversed(range(0, x)):
        left += 1
        print(i, y)
        print("%s ? %s" % (data_entry, data[i][y]))
        if data_entry <= data[i][y]:
            break

    print("down")
    for j in reversed(range(0, y)):
        down += 1
        print("%s ? %s" % (data_entry, data[x][j]))
        if data_entry <= data[x][j]:
            break

    print("right")
    for k in range(x+1, width):
        right += 1
        print("%s ? %s" % (data_entry, data[k][y]))
        if data_entry <= data[k][y]:
            break

    print("up")
    for w in range(y+1, height):
        up += 1
        print("%s ? %s" % (data_entry, data[x][w]))
        if data_entry <= data[x][w]:
            break

    print("(%d, %d) = %s -> %d * %d * %d * %d = %d" % (x, y, data_entry, up, down, left, right, up * down * left * right))
    return up * down * left * right


def scenic_score():
    scenic_scores = []

    for i in range(height):
        for j in range(width):
            scenic_scores.append(calculate_scenic_score(data[i][j], i, j))

    max = -1
    for score in scenic_scores:
        if score > max:
            max = score
    return max


print(scenic_score())