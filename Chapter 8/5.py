def multiply(a,b):
    #identifing the smaller and larger number
    smaller = a
    larger = b
    if a > b:
        smaller = b
        larger = a

    return rec_multiply(larger, smaller)


def rec_multiply(larger, smaller):
    #base case
    if smaller == 1:
        return larger
    multiply_result = rec_multiply(larger, smaller >> 1) << 1
    #check if smaller is odd
    if smaller & 1 == 1:
        multiply_result += larger
    return multiply_result



print(multiply(11,10))