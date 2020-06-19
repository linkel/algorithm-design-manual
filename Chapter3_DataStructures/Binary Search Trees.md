# Binary Search Trees

Alright, so we see that we've got some structures with fast search (arrays) or flexible updates (linked lists). Unsorted doubly linked lists had O(1) time insertion and deletion but searching took linear time in worst case. 

Sorted arrays supported binary search and logarithmic query times, but the update became linear time. 

A binary search requires that we access quickly two elements. The median elements above and below a node. So what we want for both fast search and flexible update is a linked list that has two pointers per node. This is kinda like a sorted doubly linked list, right? But the difference is that instead of sorting it from min to max, we have the root node that we start from be the middle of the group. 

A rooted binary tree is recursively defined as either being 

1. Empty
2. Consisting of a root node, together with two rooted binary trees called the left and the right subtree. 

Order matters. 

A binary search tree is a binary tree where each node has a label such that all nodes in the left subtree of node x have keys < x while nodes in the right have keys > x.

For any binary tree on n nodes and any set of n keys, there's exactly 1 labelling that makes it a BST. 

