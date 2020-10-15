from BSTree import BSTree


class Result:
    def __init__(self, is_balanced, height):
        self.is_balanced = is_balanced
        self.height = height


def is_balanced(tree):
    return recursive_is_balanced(tree._root)


def recursive_is_balanced(node):
    if node is None:
        return Result(True, -1)
    right_result = recursive_is_balanced(node.right)
    if right_result.is_balanced is False:
        return Result(False, None)
    left_result = recursive_is_balanced(node.left)
    if left_result.is_balanced is False:
        return Result(False, None)
    if abs(right_result.height - left_result.height) > 1:
        return Result(False, None)
    return Result(True, 1 + max(right_result.height, left_result.height))


tree = BSTree()
tree.insert_key(6)
tree.insert_key(7)
tree.insert_key(1)
tree.insert_key(5)
#tree.insert_key(3)
#tree.insert_key(2)
#tree.insert_key(3.4)
tree.insert_key(6.5)
tree.insert_key(7.5)
result = is_balanced(tree)
print(result.is_balanced, result.height)