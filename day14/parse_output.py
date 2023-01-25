count = 0
for line in open("result.txt", "r"):
    for char in line:
        if char == "o":
            count += 1

print(count)