# [8] A concatenate operation takes two sets S 1 and S 2 , where every key in S 1
# is smaller than any key in S 2 , and merges them together. Give an algorithm to
# concatenate two binary search trees into one binary search tree. The worst-case
# running time should be O(h), where h is the maximal height of the two trees.

# Okay, here's the dealio--if like the author is saying, we restrict 
# the concatenate operation to where keys in one set are smaller than ANY key in the other set,
# then this is not so bad.

# otherwise it'd be a O(n log n) operation, since I'd have to go thru each
# key in one and insert it into the other. 

# but since we have the guarantee that the keys in one are smaller than the other
# we can first find which tree has the bigger bits,
# then we can just find the smallest key in the bigger guy 
# and make him get a kiddo that links to that other tree's root node.

def find_min_node(node):
    curr = node
    while curr.left:
        curr = curr.left
    return curr

# let's have t1 be the bigger one
def concat(t1, t2):
    if t1.val < t2.val:
        t1, t2 = t2, t1
    min_node = find_min_node(t1)
    min_node.left = t2 

# I would like to make use of the set BST nodes that I already created in the last problem

from SetBSTNode import SetBST
from SetBSTNode import SetBSTNode

def insertBST(x, T: SetBST):
    curr = T.root
    insertBSTHelper(x, curr)
    
def insertBSTHelper(x, node: SetBSTNode):
    if x < node.val:
        if not node.left:
            new_node = SetBSTNode(x)
            node.left = new_node
            node.left_children += 1
            return
        else:
            insertBSTHelper(x, node.left)
            node.left_children += 1

    else:
        if not node.right:
            new_node = SetBSTNode(x)
            node.right = new_node
            node.right_children += 1
            return
        else:
            insertBSTHelper(x, node.right)
            node.right_children += 1

def print_BST(setBST: SetBST):
    curr = setBST.root
    print_BST_helper(curr)

def print_BST_helper(node):
    if not node:
        return 
    print(node.val)
    # print("This node contains " + str(node.left_children) + " left kiddos and " + str(node.right_children) + " right kiddos!")
    print_BST_helper(node.left)
    print_BST_helper(node.right)


myTree = SetBST(7)
insertBST(3, myTree)
insertBST(14, myTree)
insertBST(10, myTree)

# print_BST(myTree)

smallTree = SetBST(4)
insertBST(2, smallTree)
insertBST(5, smallTree)

# print_BST(smallTree)

concat(smallTree.root, myTree.root)

print_BST(myTree)
