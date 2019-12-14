from helper_functions.io import read_input_file
import parse
import numpy as np
from math import gcd

DAY = '12'
input_string = read_input_file(DAY)
moon_coords = input_string.split('\n')


def parse_coords(c):
    r = parse.parse('<x={x:d}, y={y:d}, z={z:d}>', c)
    return np.array([r['x'], r['y'], r['z']], dtype=int)


def apply_gravity(m1, m2):
    return np.array([1 if m1[d] < m2[d] else (-1 if m1[d] > m2[d] else 0) for d in range(D)])


def process_tick(p, v):
    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            v[i] += apply_gravity(p[i], p[j])
    p = np.add(p, v)
    return p, v


def init_state(moon_coords):
    p = np.array([parse_coords(moon) for moon in moon_coords])
    v = np.zeros(shape=p.shape)
    return p, v


def lcm(a, b):
    return (a * b) // gcd(a, b)


# part one
M = len(moon_coords)  # num moons
D = 3  # dimensions
positions, velocities = init_state(moon_coords)
for _ in range(1000):
    positions, velocities = process_tick(positions, velocities)

pot = np.sum(np.abs(positions), axis=1)
kin = np.sum(np.abs(velocities), axis=1)
print(np.sum(np.multiply(pot, kin)))

# part two
# reset to initial state
positions_start, velocities_start = init_state(moon_coords)
t = 1000
cycle_lengths = [None, None, None]
while True:
    positions, velocities = process_tick(positions, velocities)
    t += 1
    for d in range(D):
        if cycle_lengths[d]:
            continue
        if np.all(positions[:, d] == positions_start[:, d]) and np.all(velocities[:, d] == velocities_start[:, d]):
            cycle_lengths[d] = t
    if None not in cycle_lengths:
        break

print(lcm(cycle_lengths[0], lcm(cycle_lengths[1], cycle_lengths[2])))
