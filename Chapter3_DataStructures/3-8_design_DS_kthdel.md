If we were to design a data structure that enables insertion of item x into set T, and enables deletion of the kth smallest element from T, and permits checking member iff x is in the set T...

1. insert(x,T) - insert item into set T
2. delete(k,T) - delete the kth smallest element from T
3. member(x, T) - return true if and only if x is in the set T

All operations must take O(log n) time on an n-element set. 

If I had a hash function and an array, I could insert an item into the array in O(1) time, right? But then the kth smallest element would be O(n) time I think... 

Checking if member would be O(n) time, I guess. 

So maybe that's not quite good. If the goal is to target log n time it seems kind of like the author wants me to use a tree of some sort. 

What if I did an implementation using a binary search tree? 

Thinking about it, it seems like an insertion into a binary search tree would take log n since it has to find the position that it should be inserted into. 

Deletion in my head is still taking O(n) time! I have to find the kth smallest, and how do I know how many elements are under the node? 

Dang, some dingdong online has a solution where he adds on information on each node as to its total number of children nodes. That makes sense! Reminds me a bit of the sum tree thing. 

So if a node has info on how many left children it has and how many right children it has, you know to find the kth smallest if it's only got 2 left kids we need to be searching in the right side. So I guess you'd be taking that k value and subtracting left nodes as you traverse. 

I should make an attempt to implement this...

so many things to implement. I wanted to implement a skip list, a circular array, a deque and use that to implement the queue and stack, and also to implement this mystery cool data structure. B L A H