from helper_functions.io import read_input_file
from collections import defaultdict
from math import ceil

DAY = '14'
input_list = read_input_file(DAY, output_type='list')


def get_chemical_quantity(s):
    n, chem = s.split(' ')
    return int(n), chem


def parse_reaction(r):
    inputs, output = r.split('=>')
    n_output, chem_output = get_chemical_quantity(output.strip())
    inputs_dict = dict()
    for i in inputs.split(', '):
        n, chem = get_chemical_quantity(i.strip())
        inputs_dict[chem] = int(n)
    return chem_output, (n_output, inputs_dict)


def parse_input(reaction_list):
    reactions = defaultdict(tuple)
    for r in reaction_list:
        o, i = parse_reaction(r)
        reactions[o] = i
    return reactions


def compute_ore(to_make):
    leftover = defaultdict(int)
    ore_used = 0
    while len(to_make):
        c, N = next(iter(to_make.items()))
        num_per_reaction, materials = all_reactions[c]
        num_reactions = ceil((N - leftover[c]) / num_per_reaction)
        # print(f' Need {N}, get {num_per_reaction} per, times {num_reactions}, leftover {num_per_reaction * num_reactions - N}')
        leftover[c] += num_per_reaction * num_reactions - N
        for mat, n_mat in materials.items():
            if mat == 'ORE':
                ore_used += n_mat * num_reactions
            else:
                to_make[mat] += n_mat * num_reactions
        del to_make[c]
    return ore_used, leftover


all_reactions = parse_input(reaction_list=input_list)
# part one
to_make = defaultdict(int, {'FUEL': 1})
ore_per_fuel, _ = compute_ore(to_make)
print(f'Used {ore_per_fuel} ORE to make 1 FUEL.')

# part two
ore_supply = 1000000000000
max_fuel = ore_supply / ore_per_fuel
ore_used, leftover = compute_ore(to_make=defaultdict(int, {'FUEL': int(max_fuel)}))
print(ore_used)
