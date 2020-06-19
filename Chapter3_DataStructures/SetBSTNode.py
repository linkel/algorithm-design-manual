# From the 3-8 problem, separated out for use in other files

class SetBSTNode():
    def __init__(self, val = None):
        self.val = val 
        self.left = None 
        self.right = None
        self.left_children = 0
        self.right_children = 0

class SetBST():
    def __init__(self, val=None):
        self.root = SetBSTNode()
        self.root.val = val

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

# myTree = SetBST(7)
# insertBST(3, myTree)
# insertBST(14, myTree)
# insertBST(10, myTree)

# print_BST(myTree)


def delete_kth(k, root: SetBST):
    if not root:
        return
    curr = root.root
    if curr:
        delete_kth_helper(k, root.root, curr.left_children + 1)

def find_min_node(node):
    curr = node
    while curr.left:
        curr = curr.left
    return curr

def delete_kth_helper(k, node: SetBSTNode, position):
    if not node:
        return node
    if position == k:
        # delete happens here
        if not node.left:
            temp = node.right
            node = None
            return temp
        elif not node.right:
            temp = node.left
            node = None
            return temp
        else: # it has two children so we have to replace with successor
            temp = find_min_node(node.right)
            node.val = temp.val
            node.right = delete_kth_helper(k + 1, node.right, position + 1 + node.right.left_children)
    elif position > k:
        # k's smaller so we will go left
        if node.left:
            node.left = delete_kth_helper(k, node.left, position - 1 - node.left.right_children)
        else:
            print("k was outside the range of this tree's elements")
            node.left = None
    else: # position < k
        if node.right:
            node.right = delete_kth_helper(k, node.right, position + 1 + node.right.left_children)
        else:
            print("k was outside the range of this tree's elements")
            node.right = None
    return node

def member_of_BST(x, root: SetBST):
    curr = root.root
    if not curr:
        return
    return member_of_BST_helper(x, curr)

def member_of_BST_helper(x, node: SetBSTNode):
    if not node:
        return False
    if x == node.val:
        return True
    elif x < node.val:
        return member_of_BST_helper(x, node.left)
    else:
        return member_of_BST_helper(x, node.right)