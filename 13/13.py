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
    3: '-',
    4: 'o'
}

# part one
game.run_until_dead()
game_tiles = game.get_output()
print(game_tiles[2::3].count(2))


# part two
def print_game_grid(X=44, Y=25):
    print(['\n'.join([tiles[grid[(x, y)]] for x in range(X)]) for y in range(Y)])


def get_pos(grid, val):
    return list(grid.keys())[list(grid.values()).index(val)][0]


def follow_ball():
    # print_game_grid(grid)
    ball_pos = get_pos(grid, val=4)
    paddle_pos = get_pos(grid, val=3)
    return 1 if ball_pos > paddle_pos else (-1 if ball_pos < paddle_pos else 0)


program[0] = 2  # play for free
game = Program(program=program)
grid = defaultdict(int)
while game.is_alive():
    x = game.run(input_fn=follow_ball)
    y = game.run(input_fn=follow_ball)
    tile = game.run(input_fn=follow_ball)
    grid[(x, y)] = tile
print(grid[(-1, 0)])
