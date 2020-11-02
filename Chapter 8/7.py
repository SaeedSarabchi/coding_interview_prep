def permutation_no_dup(perm_so_far, rem, all_perms):
    if len(rem) == 0:
        all_perms.append(perm_so_far)

    for i in range(len(rem)):
        permutation_no_dup(perm_so_far + [rem[i]], rem[:i] + rem[i + 1:], all_perms)

def permutation_with_dup(perm_so_far, rem, all_perms):
    if len(rem) == 0:
        all_perms.append(perm_so_far)

    visited = set()
    for i in range(len(rem)):
        if rem[i] not in visited:
            visited.add(rem[i])
            permutation_with_dup(perm_so_far + [rem[i]], rem[:i] + rem[i + 1:], all_perms)


def permutation(input_list):
    result_list = []
    permutation_with_dup([], input_list, result_list)
    return result_list

input_list = ["a", "b", "c"]
results = (permutation(input_list))
for r in results:
    print(r)