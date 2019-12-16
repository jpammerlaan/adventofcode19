from helper_functions.io import read_input_file
from collections import defaultdict

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
    reactions = defaultdict(dict)
    for r in reaction_list:
        o, i = parse_reaction(r)
        reactions[o] = i
    return reactions


reactions = parse_input(reaction_list=input_list)
to_make = defaultdict(int, {'FUEL': 1})
while len(to_make):
    c, N = next(iter(to_make.items()))
    reqs = reactions[c]
    for n in range(N):
        for req in reqs:
    del to_make[c]
