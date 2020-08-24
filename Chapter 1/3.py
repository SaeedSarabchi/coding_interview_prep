def URLify(input_string, true_size):
    char_array = list(input_string)
    char_array[true_size] = '\0'
    for i,char in enumerate(char_array):
        if char == ' ':
            char_array[i] = '%20'
        if char == '\0':
            break
    print(char_array)
    return ''.join(char_array)

#print(URLify("Mr John Smith    ", 13))


def URLify2(input_string, true_size):
    input_byte_array = bytearray(input_string.encode())
    number_of_spaces = 0
    for char in input_byte_array:
        if chr(char) == ' ':
            number_of_spaces += 1
    for i in range(number_of_spaces*2):
        input_byte_array.append(ord(' '))
    end_index = true_size + 2 * number_of_spaces
    for i in range(end_index, len(input_string)):
        input_byte_array.pop()

    for i in range(true_size, -1, -1):

        if chr(input_byte_array[i - 1]) == ' ':
            input_byte_array[end_index - 1] = ord('0')
            input_byte_array[end_index - 2] = ord('2')
            input_byte_array[end_index - 3] = ord('%')
            end_index -= 3

        else:
            input_byte_array[end_index - 1] = input_byte_array[i -1]
            end_index -= 1



    return input_byte_array.decode()


print(URLify2("ab cd e", 7))