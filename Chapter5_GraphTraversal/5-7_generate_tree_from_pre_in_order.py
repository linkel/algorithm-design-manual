import unittest

# Given pre-order and in-order traversals of a binary tree, is it possible to recon-
# struct the tree? If so, sketch an algorithm to do it. If not, give a counterexample.
# Repeat the problem if you are given the pre-order and post-order traversals.


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Example tree:
#          1
#       2     6
#    3
#       4
#          5
# Preorder: 1,2,3,4,5,6
# Inorder: 3,4,5,2,1,6
# Postorder (for info): 5,4,3,2,6,1

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)

four.right = five
three.right = four
two.left = three
one.left = two
one.right = six

# Can use preorder to determine current root
# And use inorder to determine the left and right subtree

preorder = [1,2,3,4,5,6]
inorder = [3,4,5,2,1,6]


def recreate_tree(preorder, inorder):
    if len(preorder) == 0 or len(inorder) == 0:
        return
    print(preorder, inorder)
    curr_root = Node(preorder[0])
    root_idx = inorder.index(preorder[0])
    preorder.pop(0)
    curr_root.left = recreate_tree(preorder, inorder[:root_idx])
    curr_root.right = recreate_tree(preorder, inorder[root_idx + 1:])

    return curr_root


class TestCode(unittest.TestCase):

    def test_generate_tree(self):
        root = recreate_tree(preorder, inorder)
        self.assertEqual(root.val, one.val)
        self.assertEqual(root.left.val, one.left.val)
        self.assertEqual(root.left.left.val, one.left.left.val)
        self.assertEqual(root.left.left.right.val, one.left.left.right.val)
        self.assertEqual(root.left.left.right.right.val, one.left.left.right.right.val)
        self.assertEqual(root.right.val, one.right.val)


unittest.main()

# For pre and post order traversals, you cannot differentiate between certain trees. So it isn't possible.
#   1          1
# 2     and       2
#   3          3
#
# Have the same pre and postorder traversal (1,2,3 and 3,2,1)

