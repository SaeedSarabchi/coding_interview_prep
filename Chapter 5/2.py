from BitManipUtils import *

def float_to_bin(float_num):
    float_chars = []
    while float_num > 0:
        float_num *= 2
        if float_num >= 1:
            float_chars.append(1)
            float_num -= 1
        else:
            float_chars.append(0)
    return float_chars


a = .34
#b = a >> 1
#print(bin(b))
print(float_to_bin(.76))
