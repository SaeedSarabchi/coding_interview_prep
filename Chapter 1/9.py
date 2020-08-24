def is_rotation(str1, str2):
    pointer_to_str1 = 0
    pointer_to_str2 = 1
    common_char_found = False
    while pointer_to_str1 < len(str1):
        if str1[pointer_to_str1] == str2[pointer_to_str2]:
            if not common_char_found:
                common_char_found = True
            pointer_to_str2 += 1
        else:
            if common_char_found:
                break

        pointer_to_str1 += 1

    if str2[pointer_to_str2:] in str1:
        if len(str1) == len(str2):
            return True

    return False


print(is_rotation("waterbottle","erbottlewatt"))