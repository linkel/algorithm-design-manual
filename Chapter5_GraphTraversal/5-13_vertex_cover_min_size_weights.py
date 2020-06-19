# A vertex cover of a graph G = (V, E) is a subset of vertices V  such that each
# edge in E is incident on at least one vertex of V  .
# (a) Give an efficient algorithm to find a minimum-size vertex cover if G is a tree.
# (b) Let G = (V, E) be a tree such that the weight of each vertex is equal to the
# degree of that vertex. Give an efficient algorithm to find a minimum-weight
# vertex cover of G.
# (c) Let G = (V, E) be a tree with arbitrary weights associated with the vertices.
# Give an efficient algorithm to find a minimum-weight vertex cover of G.

# let me set up the class and write a function that creates a tree from a list.

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

# I guess I should do this to make my life easier.

l = [1,2,3,None,None,None,6,7,8]

def generate_tree_from_list(l):
    if not l:
        return None
    nodes = [None if i is None else Node(i) for i in l] # made a mistake here, not if None but if i is None. I was loading up all the Nones into nodes.
    children = nodes[::-1] # reversed nodes so we can pop
    root = children.pop()
    for node in nodes:
        if node:
            if len(children):
                node.left = children.pop()
            if len(children):
                node.right = children.pop()
    return root

ex_tree = generate_tree_from_list(l)

# (a) Give an efficient algorithm to find a minimum-size vertex cover if G is a tree.

# for a vertex cover of minimal size of a tree, we can pick all parents of leaves.
# when we find a leaf, we will note that we will pick the parent. Recursive solution.

def vertex_cover_min_size(tree):
    """Returns a min size list of vertices that cover the tree."""

    def helper(node, l):
        if not node.left and not node.right:
            return True

        print(node.val)
        left = False
        right = False
        if node.left:
            left = helper(node.left, l)
        if node.right:
            right = helper(node.right, l)
        if left or right:
            l.append(node.val) # save this node if we get the signal to mark it
            return False # and don't mark the parent of this
        return True # if we don't mark this node then its parent should get marked

    res = []
    helper(tree, res)
    return res

print(vertex_cover_min_size(ex_tree))

# (b) Let G = (V, E) be a tree such that the weight of each vertex is equal to the
# degree of that vertex. Give an efficient algorithm to find a minimum-weight
# vertex cover of G.

# I notice that if the weight of each vertex is equal to the degree of the vertex, you can pick all alternating
# levels either starting from the root or the root's children's level and the total weight ends up the same. I think
# both are minimums since you're guaranteeing you're grabbing one of the vertexes from each edge.

# not sure how to prove it though...

#          4       ____
#      /   |    \      \
#    1     4      2      2
#         /|\      \      \
#        1 1 1     2      1
#                  |
#                  1
# Like try counting the above! Each level adds up to 10.
# Same for the binary tree version below.
#      3
#   2     1
#     1
#

listweighttree = [3, 2, 1, None, 1]
weighttree = generate_tree_from_list(listweighttree)

def vertex_cover_min_weight_for_degree_node(root):
    """
    Returns a minimum weight list of nodes that are a vertex cover for the tree
    if the tree's nodes's degree is the node's weight.
    """
    res = []
    def helper(node, res, pick):
        if not node:
            return
        if pick:
            res.append(node.val)
            helper(node.left, res, False)
            helper(node.right, res, False)
        else:
            helper(node.left, res, True)
            helper(node.right, res, True)

    if not root:
        return []
    helper(root, res, True)
    return res

print(vertex_cover_min_weight_for_degree_node(weighttree))

# (c) Let G = (V, E) be a tree with arbitrary weights associated with the vertices.
# Give an efficient algorithm to find a minimum-weight vertex cover of G.


#         2
#     5      4
#  2     40     6
# 10 2   4  13
#             6
# For this example, because there's a 40 the algo should avoid picking that 40 on that level.

another = [2,5,4,2,40,None,6,10,2,4,13, None, None, None, None, None, None, None, 6]
ex_nother = generate_tree_from_list(another)

def vertex_cover_min_weight(root):
    """
    Returns a minimum weight list of nodes that are a vertex cover for the tree.
    :param root: Node
    :return: List
    """
    def helper(node):
        if not node:
            return [0, []], [0, []]
        left = helper(node.left)
        right = helper(node.right)
        return [node.val + left[1][0] + right[1][0], left[1][1] + right[1][1] + [node.val]], [left[0][0] + right[0][0], left[0][1] + right[0][1]]


    res = helper(root)
    if res[0][0] < res[1][0]:
        return res[0][1]
    else:
        return res[1][1]

    # There must be a nicer way to write this. Right now I have a tuple that saves info about whether we pick the current or don't pick him.
    # And there's another part in the tuple that saves the path chosen so far.

print(vertex_cover_min_weight(ex_nother))