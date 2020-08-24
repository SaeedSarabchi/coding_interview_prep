def is_permutation(s1,s2):
    hash_table_1 = {}
    for char in s1:
        if char not in hash_table_1:
            hash_table_1[char] = 1
        else:
            hash_table_1[char] += 1

    hash_table_2 = {}
    for char in s2:
        if char not in hash_table_2:
            hash_table_2[char] = 1
        else:
            hash_table_2[char] += 1
    return hash_table_1==hash_table_2

print(is_permutation("abcc","abcc"))