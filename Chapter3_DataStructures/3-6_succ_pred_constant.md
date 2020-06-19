My thought was that we can modify the tree so that the tree node also carries the pointer info on its predecessor and its successor. Uses more space but now we have O(1) finding predecessor and successor.  

Whenever we insert now we have to track if this item is placed on the left or the right of its parent node. If left, then the parent node is the successor and you set this new node's predecessor to the parent's predecessor and the node's successor to its parent node and update the parent node's predecessor to be this node. 

If right, then the parent node is the predecessor and you set the new node's predecessor to the parent and set the new node's successor to the parent's successor, and then modify the parent so that its successor is now this node. 

Whenever we delete we have to make sure we go to the to-be-deleted node's predecessor and set that pointer to be the to-be-deleted node's successor, and do the same for the to-be-deleted node's successor (setting its predecessor to the to-be-deleted node's predecessor). 

Anyway that's my answer! Let's see. s