from helper_functions.io import read_input_file

DAY = '02'
input_string = read_input_file(DAY)
base_intcode = list(map(int, input_string.split(',')))


def run_program(base_intcode, noun, verb):
    intcode = base_intcode.copy()
    intcode[1] = noun
    intcode[2] = verb
    i = 0
    while True:
        op = intcode[i]
        if op == 99:
            break
        in_1, in_2, out = intcode[i + 1:i + 4]
        if op == 1:
            intcode[out] = intcode[in_1] + intcode[in_2]
        if op == 2:
            intcode[out] = intcode[in_1] * intcode[in_2]
        i += 4
    return intcode


# part one
print(run_program(base_intcode, 12, 2)[0])

# part two
target = 19690720
input_range = range(100)
for noun in input_range:
    for verb in input_range:
        result = run_program(base_intcode, noun, verb)
        if result[0] == target:
            print(100 * noun + verb)
            break
