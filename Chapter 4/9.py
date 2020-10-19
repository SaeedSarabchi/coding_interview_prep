from BSTree import BSTreeNode, BSTree


def bst_sequence(node) -> list:
    if node is None:
        return [[]]
    result_list = []
    left_seq = bst_sequence(node.left)
    right_seq = bst_sequence(node.right)
    #if left_seq != [] and right_seq != []:
    for s_left in left_seq:
        for s_right in right_seq:
            sorted_perm([node.data], s_left, s_right, result_list)
    return result_list
    # else:
    #     if left_seq == []:
    #         for r_seq in right_seq:
    #             result_list.append([node.data] + r_seq)
    #     if right_seq == []:
    #         for l_seq in left_seq:
    #             result_list.append([node.data] + l_seq)
    #     if left_seq == [] and right_seq==[]:
    #             result_list.append([node.data])
    #     return result_list


def weave(list1, list2):
    results = []
    sorted_perm([], list1, list2, results)
    return results


def sorted_perm(prefix, rem1, rem2, results):
    if len(rem1) == 0 and len(rem2) == 0:
        results.append(prefix)
    if len(rem1) > 0:
        sorted_perm(prefix + [rem1[0]], rem1[1:], rem2, results)
    if len(rem2) > 0:
        sorted_perm(prefix + [rem2[0]], rem1, rem2[1:], results)

tree = BSTree()
tree.insert_key(2)
tree.insert_key(1)
tree.insert_key(3)
#tree.insert_key(2.5)
tree.insert_key(4)
#tree.insert_key(0.5)
#tree.insert_key(1.5)
res = (bst_sequence(tree._root))
for r in res:
    print(r)
tree.insert_key(7)
tree.insert_key(5)
tree.insert_key(2)
tree.insert_key(6)
tree.insert_key(3)
tree.insert_key(1)
tree.insert_key(4)
tree.insert_key(5.5)


def perm(list):
    results = []
    recursive_permutation([], list, results)
    return results


def recursive_permutation(list_so_far, remaining, results):
    if len(remaining) == 0:
        results.append(list_so_far)
        return
    for elem in remaining:
        rem = [e for e in remaining]
        rem.remove(elem)
        recursive_permutation(list_so_far + [elem], rem, results)


#for elem in (perm([1, 2, 3])):
#    print(elem)





results = weave([1, 2], [3, 4])
#for elem in results:
    #print(elem)