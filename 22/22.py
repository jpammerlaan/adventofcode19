from helper_functions.io import read_input_file
from sympy import Symbol, simplify

DAY = '22'
ops_list = read_input_file(DAY, output_type='list')


def cut(deck, n):
    return deck[n:] + deck[:n]


def deal_with_increment(deck, inc):
    deck_size = len(deck)
    new_deck = [None for _ in range(deck_size)]
    for c in range(deck_size):
        new_deck[((c * inc) % deck_size)] = deck[c]
    return new_deck


def deal_into(deck):
    return deck[::-1]


def shuffle(m, n):
    deck = range(m)
    for _ in range(n):  # shuffle n times
        for op in ops_list:
            if op.startswith('deal into'):
                deck = deal_into(deck)
                continue
            val = int(op.split(' ')[-1])
            if op.startswith('cut'):
                deck = cut(deck, val)
            else:
                deck = deal_with_increment(deck, val)
    return deck


# part one
m1 = 10007
n1 = 1
deck = shuffle(m=m1, n=n1)
print(deck.index(2019))


# part two
# So as it turns out, all the shuffle operations only perform linear operations on the deck.
# This means we can write each shuffle operation as f(x) = ax + b % m for some values of a
# and b, where x is the current index of a card. For example, dealing into a new stack can
# be written as f(x) = (-1 * x + m-1) % m = (m - 1 - x) % m.
# Similarly, the other functions can be rewritten in this form as well.
# Deal into new stack: f(x) = (m - 1 - x) % m
# Deal with increment i: f(x) = (x * i) % m
# Cut c cards: f(x) = (x - c) % m
# We can simply add all these functions together to produce the result of one shuffle for a given card x.
# If we repeat this process n times, we can find the value of the 2020th card by linear exponentation.


# Source: https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def get_shuffle_function(m):
    x = Symbol('x', integer=True)
    for op in reversed(ops_list):  # we're undoing the shuffles back to front, so reverse the operation list as well
        if op.startswith('deal into'):
            x = m - 1 - x
        else:
            val = int(op.split(' ')[-1])
            if op.startswith('cut'):
                x = x + val
            else:
                x = x * modinv(val, m)
    return simplify(x % m)  # use modulo here rather than in the equations themselves to simplify further


m = 119315717514047
f = get_shuffle_function(m)
a = f.args[0].args[1].args[0]  # lol
b = f.args[0].args[0]

# We apply the function f(x) = ax + b with the parameters above N times. This produces something like:
# ax + b
# a(ax+b) + b = a^2x + ab + b
# a(a^2x + ab+ b) = a^3x + a^2b + ab + b
# a(a^3x + a^2b + ab + b) = a^4x + a^3b + a^2b + ab + b
# and so on, which is simply the geometric sum, so we can simplify it to: a^Nx + b * ((a^N)-1) / (a - 1)
# (a-1)^-1 can be inverted by Fermat's little theorem as (a-1)^(m-2) % m.
# Combined, this gives us: (a^Nx + b * (a^N - 1) * (a-1)^(m-2)) % m
# Add mod m to each pow function to ensure we don't end up with giant numbers and off we go:
n = 101741582076661
p = 2020
print((pow(a, n, m) * p + b * (pow(a, n, m) - 1) * (pow(a - 1, m - 2, m))) % m)
