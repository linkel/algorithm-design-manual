# Suppose an arithmetic expression is given as a tree. Each leaf is an integer and
# each internal node is one of the standard arithmetical operations (+, −, ∗, /). For
# example, the expression 2 + 3 ∗ 4 + (3 ∗ 4)/5 is represented by the tree in Figure
# 5.17(a). Give an O(n) algorithm for evaluating such an expression, where there are
# n nodes in the tree.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Ex: 2 + 3 * 4 + (3 * 4)/5
#              (+)
#            /     \
#         (/)       (+)
#       /    \     /     \
#    (*)     5    2      (*)
#   /   \               /   \
#  3     4             3     4


root = Node('+')
lvlone1 = Node('/')
lvlone2 = Node('+')
lvltwo1 = Node('*')
lvltwo2 = Node(5)
lvltwo3 = Node(2)
lvltwo4 = Node('*')
lvlthree1 = Node(3)
lvlthree2 = Node(4)
lvlthree3 = Node(3)
lvlthree4 = Node(4)

root.left = lvlone1
root.right = lvlone2
lvlone1.left = lvltwo1
lvlone1.right = lvltwo2
lvlone2.left = lvltwo3
lvlone2.right = lvltwo4
lvltwo1.left = lvlthree1
lvltwo1.right = lvlthree2
lvltwo4.left = lvlthree3
lvltwo4.right = lvlthree4

def evaluate_expression_tree(root):
    if root:
        return helper(root)

def helper(node):
    if not node.left and not node.right:
        return node.val
    if not node.left or not node.right:
        raise Exception("Arithmetic expression must be balanced--inner nodes cannot only have one child")
    left = helper(node.left)
    right = helper(node.right)

    if node.val == '+':
        return left + right
    elif node.val == '/':
        return left / right
    elif node.val == '-':
        return left - right
    elif node.val == '*':
        return left * right

print(evaluate_expression_tree(root))