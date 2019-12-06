from helper_functions.io import read_input_file

DAY = '06'
orbit_map = read_input_file(DAY, output_type='list')


def get_orbits(direct_orbits, obj):
    orbits = [obj]
    while direct_orbits[obj] != 'COM':
        obj = direct_orbits[obj]
        orbits.append(obj)
    return orbits


orbits_dict = {b: a for a, b in map(lambda o: o.split(')'), orbit_map)}
indirect_orbits = {obj: get_orbits(orbits_dict, obj) for obj in orbits_dict.keys()}
# part one
print(sum([len(o) for o in indirect_orbits.values()]))
# part two
print(len(set(indirect_orbits[orbits_dict['YOU']]).symmetric_difference(indirect_orbits[orbits_dict['SAN']])))
