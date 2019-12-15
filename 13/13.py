from helper_functions.io import read_input_file
from helper_functions.intcode import Program
from collections import defaultdict

DAY = '13'
input_string = read_input_file(DAY)
program = list(map(int, input_string.split(',')))

game = Program(program=program)

tiles = {
    0: ' ',
    1: '#',
    2: 'x',
    3: '_',
    4: 'o'
}

# part one
game.run_until_dead()
game_tiles = game.get_output()
print(game_tiles[2::3].count(2))

# part two
program[0] = 2  # play for free
game = Program(program=program)
grid = defaultdict(int)
while game.is_alive():
    x = game.run()
    y = game.run()
    tile = game.run()
    grid[(x, y)] = tile
