from helper_functions.io import read_input_file
from collections import defaultdict

DAY = '04'
input_string = read_input_file(DAY, output_type='string')
lower, upper = map(int, input_string.split('-'))


def test_part_one(pwd):
    s = list(str(pwd))
    return sorted(s) == s and len(set(s)) < len(s)


def test_part_two(pwd):
    s = list(str(pwd))
    return (sorted(s) == s) & any(s.count(c) == 2 for c in s)


# part one
print(len([p for p in range(lower, upper) if test_part_one(p)]))
# part two
print(len([p for p in range(lower, upper) if test_part_two(p)]))
