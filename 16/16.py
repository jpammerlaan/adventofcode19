from helper_functions.io import read_input_file
from math import ceil

DAY = '16'
input_signal = list(map(int, str(read_input_file(DAY, output_type='string'))))
OUTPUT_LENGTH = 8
OFFSET_LENGTH = 7
BASE_PATTERN = (0, 1, 0, -1)


def create_patterns(n):
    patterns = []
    for i in range(1, n + 1):
        pattern = []
        reps = ceil((n + 1) / (len(BASE_PATTERN) * i))  # number of pattern repetitions
        for rep in range(reps):
            pattern.extend([j for j in BASE_PATTERN for _ in range(i)])
        patterns.append(pattern[1:(n + 1)])
    return patterns


def transform_signal(patterns, signal, t_max=100):
    signal_length = len(signal)
    transformed = [0 for _ in range(signal_length)]
    for t in range(t_max):
        for i in range(signal_length):
            transformed[i] = abs(sum(patterns[i][j] * signal[j] for j in range(signal_length))) % 10
        signal = transformed
    return transformed


# part one
patterns = create_patterns(n=len(input_signal))
output_signal = transform_signal(patterns, input_signal)
print(''.join(map(str, output_signal[:OUTPUT_LENGTH])))

# part two
num_reps = 10_000
offset = int(''.join(str(x) for x in input_signal[:OFFSET_LENGTH]))
large_input_signal = [input_signal[i] for _ in range(num_reps) for i in range(len(input_signal))]
large_input_signal = large_input_signal[offset:]


def decode_signal(encoded, t_max=100):
    signal_length = len(encoded)
    encoded = encoded[::-1]  # reverse the signal, makes for a simpler loop
    decoded = [0 for _ in range(signal_length)]
    for t in range(t_max):
        decoded[0] = encoded[0]  # init the new iteration with the first value
        for i in range(1, signal_length):
            decoded[i] = (encoded[i] + decoded[i - 1]) % 10
        encoded = decoded
    return decoded[::-1]  # reverse the signal back to the original direction


msg = decode_signal(large_input_signal, t_max=100)
print(''.join(map(str, msg[:OUTPUT_LENGTH])))
