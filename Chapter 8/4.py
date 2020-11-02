def subset(input_set, curr_subset, result_subsets):
    if input_set == []:
        result_subsets.append(curr_subset)
    else:
        subset(input_set[1:], curr_subset + [input_set[0]], result_subsets)
        subset(input_set[1:], curr_subset, result_subsets)


a = [1, 2, 3, 4]
result=[]
subset(a, [], result)
for set in result:
    print(set)

