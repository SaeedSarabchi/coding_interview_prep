def print_bin16(num):
    print(bin(num & 0b1111111111111111))

def print_bin32(num):
    if num>=0:
        print(bin(num))
    else:
        print(bin(num & 0b11111111111111111111111111111111))