def question1(input_string):
    alphabet_hash_table = {}
    for ch in input_string:
        char = ch.lower()
        if 'a' <= char <= 'z':
            if char in alphabet_hash_table:
                alphabet_hash_table[char] += 1
            else:
                alphabet_hash_table[char] = 1

    if len(alphabet_hash_table) == 26:
        for char in alphabet_hash_table:
            if alphabet_hash_table[char] != 1:
                return False
        return True
    return False

#print(question1("qwertyuiopasdfghjkzxcvbnm"))


def has_all_unique_characters(input_string):
    hash_table = {}
    for char in input_string:
        if char not in hash_table:
            hash_table[char] = 1
        else:
            hash_table[char] += 1

    for char in hash_table:
        if hash_table[char] > 1:
            return False
    return True

print(has_all_unique_characters("assd"))