from helper_functions.io import read_input_file, print_binary_grid

DAY = '08'
pixels_raw = read_input_file(DAY, output_type='string')
H = 6
W = 25


def chunk(x, size):
    return [x[i:i + size] for i in range(0, len(x), size)]


def get_pixel(layers, i, depth=0):
    return get_pixel(layers, i, depth + 1) if layers[depth][i] == '2' else layers[depth][i]


layers = chunk(pixels_raw, H * W)
# part one
check_layer = layers[min(map(lambda x: x.count('0'), layers))]
print(check_layer.count('1') * check_layer.count('2'))
# part two
pixels_list = list(map(lambda i: get_pixel(layers, i), range(H * W)))
pixels_grid = chunk(pixels_list, W)
print_binary_grid(pixels_grid, target_val='1')
