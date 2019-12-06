from helper_functions.io import read_input_file
from collections import defaultdict

DAY = '06'
orbit_map = read_input_file(DAY, output_type='list')

def get_orbits(orbits, obj):
    orb = [obj]
    while orbits[obj] != 'COM':
        obj = orbits[obj]
        orb.append(obj)
    return orb


direct_orbits = {b: a for a, b in map(lambda o: o.split(')'), orbit_map)}
indirect_orbits = [get_orbits(direct_orbits, obj) for obj in direct_orbits]
# part one
print(sum([len(o) for o in indirect_orbits]))
# part two
you = get_orbits(direct_orbits, 'K')
print(you)
san = get_orbits(direct_orbits, 'I')
print(len(you) + len(san) - 2*len(set(you).intersection(san)) + 2)
