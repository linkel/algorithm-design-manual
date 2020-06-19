class bst:
    def __init__(self, parent=None, val:int =None, left=None, right=None):
        self.parent = parent
        self.val = val
        self.left = left
        self.right = right

# ouh my god you dingdong
# be careful about putting commas after stuff in your constructor
# you're thinking JS objects or something bizarre, but you turned your ints to tuples of (3,)

def search_tree(root, x):
    if not root:
        return None
    if root.val == x:
        return root
    if x < root.val:
        return search_tree(root.left, x)
    else:
        return search_tree(root.right, x)


holder = bst()
root = bst(None, 10, None, None)
lv2_right = bst(root,15,None,None)
lv2_left = bst(root,7,None,None)
lv3_first_right = bst(lv2_left,8,None,None)
root.left = lv2_left
root.right = lv2_right
lv2_left.right = lv3_first_right

print(search_tree(root,8))

# smallest key must live in the left subtree, and biggest must live in the right subtree.
# this makes life easier for me.

# iterative for this one, so no need to worry about the if none killing your return

def find_min(root):
    if not root:
        return None
    curr = root
    while curr.left: # the reason why we do curr.left here instead of my 
        # frequent curr stuff is because it'd give us None all the time otherwise.
        # I'd want to do curr.left so that I can get my cutey minimum back once there's no more left to go.
        curr = curr.left
    print(curr.val)
    return curr

# Damn, trying to write this from my head I still forked it up, worried about it being
# recursive when I knew I was writing an iterative one, and I wrote while curr instead of while curr.left

print(find_min(root))

def find_max(root):
    if not root:
        return None
    curr = root
    while curr.right:
        curr = curr.right
    print(curr.val)
    return curr

print(find_max(root))

# tree traversal dear me
# I want to traverse all the nodes in this tree. Let us do a recursive t r a v e r s e

# I need to write a way to stick an array into a BST format, dude. 

def traverse_tree(root):
    if root:
        traverse_tree(root.left)
        print(root.val)
        traverse_tree(root.right)

# traverse_tree(root)

def traverse_tree_with_depth(root, depth = 0):
    if root:
        traverse_tree_with_depth(root.left, depth + 1)
        print(root.val, depth)
        traverse_tree_with_depth(root.right, depth + 1)

# If I have an array, for example [3,6,2,56,3] is there a simple way to load this array up into a BST?
# First I need to sort the array. Doing it with an unsorted array would be a bodonka.
# Step one would be to find the middle element of the array, turn that into root
# Step two would be then to take the left side of the array and do the same for the left side
# Step three then you take the right side of the array and do the same on that side. 

# Pls go over how to set up merge sort again. 

test_arr = [3,2,1,4,5,8,7,6]
test_arr.sort()
print(test_arr)

# uhhh I wrote this shitty quick turning into bst code, does it work? 

def turn_into_bst(arr, parent=None):
    if len(arr) == 0:
        return None
    print(arr)
    curr = bst()
    low, high = 0, len(arr)-1
    mid = (low + high) // 2
    curr.parent = parent
    curr.val = arr[mid]
    curr.left = turn_into_bst(arr[0:mid], curr)
    curr.right = turn_into_bst(arr[mid+1:], curr)
    return curr

giveme = turn_into_bst(test_arr)

traverse_tree(giveme)

#find_min(giveme)
#find_max(giveme)

teeny = [1,2,4,5,8,14,34]
tryagain = turn_into_bst(teeny)
#find_min(tryagain)

# So for insertion, there's only one place to insert an item into
# such that we can find it again. We have to look for where they key would be,
# and when unsuccessful, stick that key there.

def insert(node, x):
    if x < node.val:
        if not node.left:
            new_node = bst()
            new_node.parent = node
            new_node.val = x
            node.left = new_node
            return
        else:
            insert(node.left, x)
    else:
        if not node.right:
            new_node = bst()
            new_node.parent = node
            new_node.val = x
            node.right = new_node
            return
        else:
            insert(node.right, x)
    
# I think this insertion code takes O(height) like the search code.
# Is that O(log n) where n is the number of entries? only if balanced I think

    
insert(tryagain, 19)
traverse_tree_with_depth(tryagain)

# Deletion from a tree is trickier because there's three cases.
# The three cases are as follows:
# 1. The node is a leaf node. Just remove the reference
# 2. The node has one child: parent node gets ref'd to that child, remove the one node
# 3. The node has two children: need to find next successor, stick it in where current node is.

def find_successor(node):
    if node.right:
        return find_min_node_and_parent(node.right)
    else:
        return None

def find_min_node_and_parent(node):
    parent = None
    curr = node
    while curr.left:
        parent = curr
        curr = curr.left
    return curr, parent

def delete(node, x, parent):
    if node.val == x:
        if not node.left and not node.right:
            if parent.left == node:
                parent.left = None
            else: # parent.right == node:
                parent.right = None
        elif not node.left:
            if parent.left == node:
                parent.left = node.right
            else: # parent.right == node
                parent.right = node.right
        elif not node.right:
            if parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left
        # it has two children
        else:
            successor_node, successor_parent = find_successor(node) # successor will always have no kids?
            node.val = successor_node.val
            successor_parent.left = None
        return
    if x < node.val:
        delete(node.left, x, node)
    else:
        delete(node.right, x, node)
        

# delete(tryagain, 14, None)

# traverse_tree_with_depth(tryagain)

# Yeah, this is really messy. I am needing to carry info around on the parent since I can't just
# set the successor node to None in Python--that successor node that is stored in the variable seems to be a copy!

# Why not just use the delete_node function I made? 

def find_min_node(node):
    curr = node
    while curr.left:
        curr = curr.left
    return curr

def delete2(node, x):
    if not node:
        return node
    if x < node.val:
        node.left = delete2(node.left, x)
    elif x > node.val:
        node.right = delete2(node.right, x)
    else: # key is same!
        if not node.left:
            temp = node.right
            node = None
            return temp
        elif not node.right:
            temp = node.left
            node = None
            return temp
        
        temp = find_min_node(node.right)

        node.val = temp.val

        node.right = delete2(node.right, temp.val) # finds that one that we pulled in
    return node

delete(tryagain, 14, None)

traverse_tree_with_depth(tryagain)

# That delete2 function I got from geeks for geeks is way nicer. 

# So an immediate successor node has to either be a leaf node, or else it is
# a node that has a right node but it's the immediate one on the .right of our node.
# because the righter you get, the bigger you get. 