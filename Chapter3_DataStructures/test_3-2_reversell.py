class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

arr = [1,2,3,4]
def make_list(arr):
    next_node = None
    while len(arr) > 0:
        node = ListNode(arr.pop())
        node.next = next_node
        next_node = node
    return node

def print_list(node):
    if node:
        print(node.val)
        print_list(node.next)

ll = make_list(arr)
print_list(ll)

def rev(head):
    curr = head
    prev = None
    while head:
        head = head.next
        curr.next = prev
        prev = curr
        curr = head
    return prev

res = rev(ll)

print_list(res)
# I should also do an implementation that has a head and tail ll