It says without mucking about with pointers... Is storing the max and min location in a variable okay, or does that also count as mucking about with pointers? 

Like if we delete the min or max node, and at that point we make sure to update the min or max to the next highest or next lowest node... 

Deletion takes log n time because we have to find the node to delete in the binary tree--so if we find the node to delete and find the next largest during the delete operation, that's O(log n) isn't it? Even if it's O(2 log n) still counts.

Likewise upon insertion if we see that it's larger than the max or smaller than the current min, we should update that. 