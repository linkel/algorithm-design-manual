class ListNode():
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def arr_to_list(arr):
    new_node = None
    if len(arr) > 0:
        new_node = ListNode(arr.pop(0))
        new_node.next = arr_to_list(arr)
    return new_node

def arr_to_list_it(arr):
    temp = None
    for i in range(len(arr)-1, -1, -1):
        new_node = ListNode(arr[i])
        new_node.next = temp
        temp = new_node
    return temp

arr = [23,1,55,3,24]
fresh_arr = [12,3,66,4,3]
ll = arr_to_list(arr)
iterative_ll = arr_to_list_it(fresh_arr)

def print_list(node):
    curr = node
    while curr:
        print(curr.val)
        curr = curr.next

def print_list_r(node):
    if node:
        print(node.val)
        print_list_r(node.next)

# print_list(ll)
# print_list_r(ll)
# print_list(ll)

def search_list(node, x):
    if not node:
        return None
    if node.val == x:
        return node
    return search_list(node.next, x)

def insert_at_front(node, x):
    print(node.val)
    new_node = ListNode(x)
    new_node.next = node
    return new_node

# mod = insert_at_front(ll,100)
# print_list(mod)

# print_list(iterative_ll)

# this whole time I was popping the whole array and trying to use an empty one derp

def predecessor(node, x):
    if not node or not node.next:
        print("predecessor sought on null list")
        return None
    if node.next.val == x:
        return node
    return predecessor(node.next, x)

'''
We want to get rid of item x from LinkedList starting at node
'''
def delete(node, x):
    found_node = search_list(node, x)
    if found_node:
        pred = predecessor(node, x)
        if not pred: # if this is the starting node
            print("no pred node")
            return node.next
        else:
            pred.next = found_node.next
            return node
    print("not found")
    return node

# deleted_version = delete(iterative_ll,3)
# print_list(iterative_ll)

''' this one compares on the node '''
def predecessor_nodey(node, node_to_find):
    curr = node
    while curr and curr.next:
        if curr.next == node_to_find:
            return curr
        curr = curr.next
    return None

def delete_using_nodey(node, x):
    curr = node
    while curr:
        if curr.val == x:
            prev_node = predecessor_nodey(node, curr)
            if prev_node:
                prev_node.next = curr.next
                return node
            else:
                node = curr.next
                return node
        curr = curr.next
    return node

deleted_version = delete_using_nodey(iterative_ll,12)
print_list(deleted_version)

# my mistakes:
# I was not using predcessor_nodey for my delete_using_nodey, and as a result it was
# not able to find a value, and then returned None, and it went down the wrong code path.
# my baby saw that it got a none back so it then chopped everything in front of the rogue node off,
# including the rogue node 

