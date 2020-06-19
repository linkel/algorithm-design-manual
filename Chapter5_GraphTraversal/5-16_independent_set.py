class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#          1
#       2     3
#                6
#              7   8
#
#

l = [1,2,3,None,None,None,6,7,8]

def generate_tree_from_list(l):
    if not l:
        return None
    nodes = [None if i is None else Node(i) for i in l]
    children = nodes[::-1]
    root = children.pop()
    for node in nodes:
        if node:
            if len(children):
                node.left = children.pop()
            if len(children):
                node.right = children.pop()
    return root

ex_tree = generate_tree_from_list(l)

# a) Give an algorithm to generate a max-size independent set if G is a tree.

# I think for a tree we can pick all the leaves, then exclude them and their parents and pick leaves again.

def independent_set_tree(root):
    res = []
    def helper(node, res):
        if not node:
            return False # not picked
        if not node.right and not node.left:
            res.append(node.val)
            return True # picked
        left = helper(node.left, res)
        right = helper(node.right, res)
        if left or right: # if the child was picked we don't pick the current one
            return False
        else:
            res.append(node.val)
            return True
    helper(root, res)
    return res

print(independent_set_tree(ex_tree))

# b) Let G = (V, E) be a tree with weights associated with the vertices such that
# the weight of each vertex is equal to the degree of that vertex. Give an efficient
# algorithm to find a maximum independent set of G.

# What we did for the minimum weight vertex cover of G last time will work too, if this question wants a maximum weight independent set AND the weight of each vertex is equal to the degree.
# We'll pick a level and alternate from it.
# The wording's kinda bad. If it wants a maximum size independent set then it's the same as before without the weights.

# c) Let G = (V, E) be a tree with arbitrary weights associated with the vertices.
# Give an efficient algorithm to find a maximum independent set of G.

#         2
#     5      4
#  2     40     6
# 10 2   4  13
#             6
# It should pick [10,2,6,40,2,6]

another = [2,5,4,2,40,None,6,10,2,4,13, None, None, None, None, None, None, None, 6]
ex_nother = generate_tree_from_list(another)

# When we pick the current node, we can get current node's value plus that of the children's nonpicked value.
# When we don't pick the current node, we can get either the children's picked value OR the children's nonpicked value. So grab the best out of that.

class Result:
    def __init__(self, picked_sum, picked_path, unpicked_sum, unpicked_path):
        self.picked_sum = picked_sum
        self.picked_path = picked_path
        self.unpicked_sum = unpicked_sum
        self.unpicked_path = unpicked_path

def max_weight_indep_set(root):

    def helper(node):
        if not node:
            return Result(0, [], 0, [])
        left = helper(node.left)
        print(left.unpicked_sum)
        right = helper(node.right)
        left_path_if_curr_unpicked = None
        right_path_if_curr_unpicked = None
        if left.unpicked_sum > left.picked_sum:
            left_path_if_curr_unpicked = left.unpicked_path
        else:
            left_path_if_curr_unpicked = left.picked_path
        if right.unpicked_sum > right.picked_sum:
            right_path_if_curr_unpicked = right.unpicked_path
        else:
            right_path_if_curr_unpicked = right.picked_path

        return Result(
            node.val + left.unpicked_sum + right.unpicked_sum,
            [node.val] + left.unpicked_path + right.unpicked_path,
            max(left.unpicked_sum, left.picked_sum) + max(right.unpicked_sum, right.picked_sum),
            left_path_if_curr_unpicked + right_path_if_curr_unpicked)

    final = helper(root)
    if final.picked_sum > final.unpicked_sum:
        return final.picked_path
    else:
        return final.unpicked_path


print(max_weight_indep_set(ex_nother))