from helper_functions.io import read_input_file

DAY = '03'
input_string = read_input_file(DAY, output_type='list')
w1, w2 = input_string
DX = {
    'U': 0,
    'D': 0,
    'L': -1,
    'R': 1
}
DY = {
    'U': 1,
    'D': -1,
    'L': 0,
    'R': 0
}


def get_coords(w):
    x, y, length = 0, 0, 0
    ans = {}
    for cmd in w.split(','):
        d, n = cmd[0], cmd[1:]
        for _ in range(int(n)):
            x += DX[d]
            y += DY[d]
            length += 1
            if (x, y) not in ans.keys():
                ans[(x, y)] = length
    return ans


c1 = get_coords(w1)
c2 = get_coords(w2)

# part one
intersects = set(c1.keys()).intersection(c2.keys())
print(min([abs(x) + abs(y) for x, y in intersects]))
# part two
print(min([c1[k] + c2[k] for k in intersects]))
