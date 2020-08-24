
def is_palindrome_permutation(input_str):
    hash_table = {}
    input_str = input_str.replace(' ', '')
    for char in input_str:
        char = char.lower()
        if char in hash_table:
            hash_table[char] += 1
        else:
            hash_table[char] = 1

    number_of_chars_not_divisible_by_2 = 0
    for char in hash_table:
        if hash_table[char] % 2 == 1:
            number_of_chars_not_divisible_by_2 += 1

    if len(input_str) % 2 == 0:
        if number_of_chars_not_divisible_by_2 == 0:
            return True
        else:
            return False
    else:  # len(input_str)%2 == 1
        if number_of_chars_not_divisible_by_2 == 1:
            return True
        else:
            return False






def is_palindrome_permutation2(input_str):
    bit_vector = 0
    input_str = input_str.replace(' ', '')
    for char in input_str:
        char = char.lower()
        bit_vector ^= 1<<(ord(char)-ord('a'))

    if len(input_str) % 2 == 0: #input_str length is even
        if bit_vector == 0:
            return True
        else:
            return False
    else:  # #input_str length is odd
        if bit_vector in (pow(2,i) for i in range(32)):
            return True
        else:
            return False


print(is_palindrome_permutation2("Tact Cofa"))