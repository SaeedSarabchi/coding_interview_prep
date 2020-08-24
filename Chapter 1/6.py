def compress_string(input_string): #Why So Serious?????? So many bugs, hence cleanup code. see the third version of how this question can be done consicely.
    new_string  = bytearray(input_string.encode())
    char_count = 0
    pointer_to_new_string = 0
    previous_char = ' '
    for current_char in input_string:
        # TODO: check for edge case for new_string out of index
        if current_char != previous_char and char_count>0:
            if pointer_to_new_string+1 >= len(input_string)-1:
                return input_string
            new_string[pointer_to_new_string] = ord(previous_char)
            new_string[pointer_to_new_string+1] = ord(str(char_count))
            char_count = 1
            pointer_to_new_string += 2
        else:
            char_count += 1
        previous_char = current_char
    if pointer_to_new_string + 1 >= len(input_string)-1:
        return input_string
    new_string[pointer_to_new_string] = ord(previous_char)
    new_string[pointer_to_new_string + 1] = ord(str(char_count))
    pointer_to_new_string += 2
    return new_string[:pointer_to_new_string].decode()


#print(compress_string("aaaabbbbcc"))

#Extremelyy Diry Code!!!
# if you go with !previous! you'll be doomed!!!
def compress_string2(input_string):
    new_string_list = []
    previous_char = '-'
    consecutive_chars = 0
    for char in input_string:
        if previous_char != char and consecutive_chars>0:
            new_string_list.append(previous_char)
            new_string_list.append(str(consecutive_chars))
            consecutive_chars = 1
        else:
            consecutive_chars += 1
        previous_char = char

    new_string_list.append(previous_char)
    new_string_list.append(str(consecutive_chars))

    if len(new_string_list)<len(input_string):
        return ''.join(new_string_list)
    else:
        return input_string

#print(compress_string2("aaaabbbbcc"))


#!!!! in if (i==len(input_string)-1 or input_string[i]!=input_string[i+1]):
    # input_string[i+1] won't raise an exception because i==len(input_string)-1 is being checked first!!!!
def compress_string3(input_string):
    new_string_list = []
    consecutive_chars = 0
    for i in range(len(input_string)):
        consecutive_chars += 1
        if (i==len(input_string)-1 or input_string[i]!=input_string[i+1]):
            new_string_list.append(input_string[i])
            new_string_list.append(str(consecutive_chars))
            consecutive_chars = 0

    if len(new_string_list) < len(input_string):
        return ''.join(new_string_list)
    else:
        return input_string


print(compress_string3("aaaabbbbcc"))