from helper_functions.io import read_input_file
from numpy import exp, abs, angle

DAY = '10'
input_map = read_input_file(DAY, output_type='list')
# input_map = """.#..#
# .....
# #####
# ....#
# ...##""".split('\n')


# might need these later
def to_polar(z):
    return abs(z), angle(z)


def to_cartesian(r, theta):
    return r * exp(1j * theta)


def get_num_visible(ast, center):
    angles = [angle(a2 - center) for a2 in ast if a2 != center]
    return len(set(angles))


def vaporize(asteroids, station):
    i = 0
    prev_angle = 0
    polar_asteroids = [to_polar(a - station) for a in asteroids if a != station]
    sorted_asteroids = sorted(polar_asteroids, key=lambda x: (x[1], x[1]))
    print(sorted_asteroids)
    while i <= 200:
        break



asteroids = [(x + y*1j) for y, row in enumerate(input_map) for x, c in enumerate(list(row)) if c == '#']
num_visible = {a: get_num_visible(asteroids.copy(), a) for a in asteroids}
# part one
print(max(num_visible.values()))

# part two
station = max(num_visible, key=num_visible.get)
vaporize(asteroids.copy(), station)

