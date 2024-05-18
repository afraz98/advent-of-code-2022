import math

radix_base_5 = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
radix_base_10 = {2: '2', 1: '1', 0: '0', -1: '-', -2: '='}

def base_10(snafu):
    return sum([radix_base_5[snafu[i]] * (5 ** (len(snafu)-1-i)) for i in range(len(snafu))])


assert base_10('0') == 0
assert base_10('1') == 1
assert base_10('2') == 2
assert base_10('1=') == 3
assert base_10('1-') == 4
assert base_10('10') == 5
assert base_10('11') == 6
assert base_10('12') == 7
assert base_10('2=') == 8
assert base_10('2-') == 9
assert base_10('20') == 10
assert base_10('21') == 11
assert base_10('1121-1110-1=0') == 314159265


def base_5(decimal):
    max_power = math.floor(math.log(decimal, 5))
    value = [0 for i in range(max_power+1)]
    for i in range(max_power):
        print(max_power - i)
        print(decimal - (5 ** (max_power - i)))
        while decimal - (5 ** (max_power - i)) > 0:
            decimal -= (5 ** (max_power - i))
            value[max_power] += 1
    return ''.join([str(value) for value in value])


def parse_input(filename):
    return [line.strip("\n") for line in open(filename, 'r')]


print(base_5(sum([base_10(value) for value in parse_input("hot_air.txt")])))
