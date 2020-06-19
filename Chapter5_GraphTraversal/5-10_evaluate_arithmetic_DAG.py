# Suppose an arithmetic expression is given as a DAG (directed acyclic graph)
# with common subexpressions removed. Each leaf is an integer and each internal5.11
# EXERCISES
# node is one of the standard arithmetical operations (+, −, ∗, /). For example, the
# expression 2 + 3 ∗ 4 + (3 ∗ 4)/5 is represented by the DAG in Figure 5.17(b). Give
# an O(n + m) algorithm for evaluating such a DAG, where there are n nodes and
# m edges in the DAG. Hint: modify an algorithm for the tree case to achieve the
# desired efficiency.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Ex: 2 + 3 * 4 + (3 * 4)/5
#              (+)
#            /     \
#         (+)       (/)
#       /    \     /    \
#    2         (*)        5
#             /   \
#           3       4


root = Node('+')
lvlone1 = Node('+')
lvlone2 = Node('/')
lvltwo1 = Node(2)
lvltwo2 = Node('*')
lvltwo3 = Node(5)
lvlthree1 = Node(3)
lvlthree2 = Node(4)

root.left = lvlone1
root.right = lvlone2
lvlone1.left = lvltwo1
lvlone1.right = lvltwo2
lvlone2.left = lvltwo2
lvlone2.right = lvltwo3
lvltwo2.left = lvlthree1
lvltwo2.right = lvlthree2

# I believe the solution for the DAG version to keep the algorithm at O(m+n) is to cache the result of a node if already calculated.
# The original algorithm for the non-DAG version still works fine but it would have revisited and recalculated nodes that got visited by another branch,
# which is some sort of O(x*N) where x is a factor representing how many nodes have multiple parents (factor is probably not more than 2 though).
# So caching gets rid of those extra Ns but we still have to traverse the edge to find out what node to check the cache on.

def evaluate_expression_tree_DAG(root):
    cache = {}
    if root:
        return helper(root, cache)

def helper(node, cache):
    if not node.left and not node.right:
        return node.val
    if not node.left or not node.right:
        raise Exception("Arithmetic expression must be balanced--inner nodes cannot only have one child")
    if node in cache:
        return cache[node]
    left = helper(node.left, cache)
    right = helper(node.right, cache)

    if node.val == '+':
        cache[node] = left + right
        return left + right
    elif node.val == '/':
        cache[node] = left / right
        return left / right
    elif node.val == '-':
        cache[node] = left - right
        return left - right
    elif node.val == '*':
        cache[node] = left * right
        return left * right

print(evaluate_expression_tree_DAG(root))