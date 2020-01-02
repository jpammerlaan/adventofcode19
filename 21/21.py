from helper_functions.io import read_input_file
from helper_functions.intcode import Program

DAY = '21'
input_string = read_input_file(DAY)
base_intcode = list(map(int, input_string.split(',')))
OUT_FILE = '21/21.out'


class SpringDroid(Program):
    def droid_walk(self):
        inputs = [
            # Jump as late as possible
            'NOT C J',
            # Make sure we can land on something
            'AND D J',
            # When landing on an island, always jump if you need to
            'NOT A T',
            'OR T J',
            'WALK'
        ]
        ascii_input = [ord(c) for s in inputs for c in s + '\n']
        self.run_until_dead(input_fn=lambda: ascii_input.pop(0))

    def droid_run(self):
        inputs = [
            # Same as walk, but make sure we can jump always off the island to H
            'NOT C J',
            'AND D J',
            'AND H J',
            # When landing on an island, jump 'early' when continuing to B might get you in trouble
            'NOT B T',
            'AND D T',
            'OR T J',
            # Always jump when the next tile is empty
            'NOT A T',
            'OR T J',
            'RUN'
        ]
        ascii_input = [ord(c) for s in inputs for c in s + '\n']
        self.run_until_dead(input_fn=lambda: ascii_input.pop(0))

    def draw_death(self):
        out = map(chr, self.get_output())
        with open(OUT_FILE, 'w') as f:
            f.write(''.join(out))


# part one
droid = SpringDroid(program=base_intcode.copy())
droid.droid_walk()
dmg = droid.get_output()[-1]
print(dmg)

# part two
droid.reset()
droid.droid_run()
dmg = droid.get_output()[-1]
print(dmg)
