from helper_functions.io import read_input_file
from math import pi, atan2, sqrt, cos, sin
from collections import defaultdict

DAY = '10'
input_map = read_input_file(DAY, output_type='list')


def to_polar(x, y):
    return sqrt(x * x + y * y), atan2(x, y)


def get_visible_asteroids(asteroids, center):
    xc, yc = center
    angles_dict = defaultdict(list)
    for x, y in asteroids:
        radius, angle = to_polar(x - xc, yc - y)  # yc -y reverses the y direction to offset the reversed axis
        angles_dict[angle].append((radius, (x, y)))
    # sort asteroids in order of radius; ensure angles are in [0, 2pi] rather than [-pi, pi]
    return {angle + 2 * pi if angle < 0 else angle: sorted(radii) for angle, radii in angles_dict.items()}


def get_winner(station, visible_asteroids):
    visible_from_station = visible_asteroids[station]
    winner_angle = sorted(visible_from_station.keys())[199]  # get angle of winning asteroid
    winner = visible_from_station[winner_angle][0]  # get the first asteroid in this angle
    return winner[1]  # return x, y coordinates of winner


asteroids = [(x, y) for y, row in enumerate(input_map) for x, c in enumerate(list(row)) if c == '#']
visible_asteroids = {a: get_visible_asteroids(asteroids.copy(), a) for a in asteroids}
# part one
num_visible = {k: len(v) for k, v in visible_asteroids.items()}
print(max(num_visible.values()))
# part two
station = max(num_visible, key=num_visible.get)
winner = get_winner(station, visible_asteroids)
print(100 * winner[0] + winner[1])
