3-5. [3] Find the overhead fraction (the ratio of data space over total space) for each
of the following binary tree implementations on n nodes:
(a) All nodes store data, two child pointers, and a parent pointer. The data field
requires four bytes and each pointer requires four bytes.
(b) Only leaf nodes store data; internal nodes store two child pointers. The data
field requires four bytes and each pointer requires two bytes.

Okay if I have a binary tree where all nodes have data, two child ptrs, and parent ptr, and the data field needs 4 bytes and each ptr needs 4 bytes, that is 4 + 4 + 4 + 4. 16 bytes total per node. 4 / 16 is 1/4 overhead fraction. 

If I have nodes where only leaf nodes store data, internal nodes have 2 kiddos and ptr is 2 bytes...

leaf node is 4 bytes, no parent right?
internal node is 4 bytes for the 2 kiddo pointers. Number of leaf nodes per tree times 4 bytes divided by (num leaf nodes times 4 bytes plus num internal leaf nodes times 4 bytes) 

I guess it's 4 bytes per node anyways so it's really leaf nodes divided by total nodes. In a full binary tree the num of leaf nodes is always just 1 more than half the nodes in the tree. So is this.... about 1/2? 