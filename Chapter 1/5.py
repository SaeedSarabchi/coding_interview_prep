#DEBUGGING WAS EFTEZAAAAH!!!!
#WHILE CONDITION!!! EDGE CASE!!

def is_one_way(str1, str2):
    pointer_to_str1=0
    pointer_to_str2=0
    number_of_differences=0
    while pointer_to_str1<len(str1) and pointer_to_str2<len(str2):
        if str1[pointer_to_str1] != str2[pointer_to_str2]:
            number_of_differences += 1
            if len(str1)>len(str2):
                pointer_to_str1 += 1
            elif len(str1) == len(str2):
                pointer_to_str1 += 1
                pointer_to_str2 += 1
            else: #len(str1)<len(str2)
                pointer_to_str2 += 1
        else:
            pointer_to_str2 += 1
            pointer_to_str1 += 1

    return number_of_differences<=1

print(is_one_way("pale","ple"))
print(is_one_way("pales","pale"))
print(is_one_way("pale","bale"))
print(is_one_way("pales","bake"))
