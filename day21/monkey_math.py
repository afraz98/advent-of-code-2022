def parse_input(filename):
    return [line.replace(" ", "").strip("\n") for line in open(filename, "r")]

def evaluate(line, values):
    var, val = line.split(":")
    print(var, val)
    if "+" in val:
        if values.get(val.split("+")[0], None) and values.get(val.split("+")[1], None):
            values[var] = values.get(val.split("+")[0], None) + values.get(val.split("+")[1], None)
            return True

    if "-" in val:
        if values.get(val.split("-")[0], None) and values.get(val.split("-")[1], None):
            values[var] = values.get(val.split("-")[0], None) - values.get(val.split("-")[1], None)
            return True

    if "/" in val:
        if values.get(val.split("/")[0], None) and values.get(val.split("/")[1], None):
            values[var] = values.get(val.split("/")[0], None) / values.get(val.split("/")[1], None)
            return True

    if "*" in val:
        if values.get(val.split("*")[0], None) and values.get(val.split("*")[1], None):
            values[var] = values.get(val.split("*")[0], None) * values.get(val.split("*")[1], None)
            return True
    return False

def solve_expressions(input):
    lines = input
    values = {'root': None}

    # First pass -- collect values
    for line in lines:
        var, val = line.split(":")
        if val.isnumeric():
            values[var] = int(val)

    while values['root'] is None:
        for line in lines:
            evaluate(line, values)

    return values["root"]


print(solve_expressions(parse_input("monkey_math.txt")))
