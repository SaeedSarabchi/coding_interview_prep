from bitstring import BitArray, BitStream
from BitManipUtils import *

def insert(n, m, j, i):
    middle = m << i
    right = (1 << j - 1) & n
    left = ((n >> j) & -1 ) << j
    return left | middle | right

n = 0b10000000000
m = 0b10011
left = ((m >> 6) & -1 ) << 6
#print_bin32(left)
#print_bin32(insert(n, m, 6, 2))

print_bin32(-1)



