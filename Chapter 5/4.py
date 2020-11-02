# the definitions of next smallest and next largest are weird in the actual question, but the idea that you've used in this solution is well enough


def next_smallest(num):
    #swap the first zero after the first one
    temp = num
    one_cnt = 0
    cntr = 0
    while temp > 0:
        digit = temp & 1
        if digit == 0:
            if one_cnt > 0:
                #return flip_bits(num, first_one_index, cntr)
                #set the bit in cnt to one and the following to zero
                # and set one_cnt-1 most right bits to 1 as well
                n = pow(2,cntr) + pow(2,one_cnt-1)-1
                return (num >> cntr) << cntr | n

        else:
            one_cnt += 1
        temp = temp >> 1
        cntr += 1
    return num * 2


def flip_bits(num, i, j):
    #first to zero, second to 1
    mask_i = -1 ^ pow(2,i)
    flipped_i = num & mask_i
    return flipped_i | 1<<j


def next_largest(num):
    #count number of 1s
    cnt_one = 0
    cnt_bin = 0
    while num>0:
        if num & 1 == 1:
            cnt_one += 1
        num = num >> 1
        cnt_bin += 1

    res = 0
    for i in range(cnt_one):
        res = res << 1 | 1
    for i in range(cnt_bin-cnt_one):
        res = res << 1
    return res



#print(bin(next_largest(0b11100001001)))
#n = 0b1110000111100
n = 0b11100101100100
print(bin(n))
print(bin(next_smallest(n)))
