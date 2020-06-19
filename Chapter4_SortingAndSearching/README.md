# Sorting and Searching Sloppy Notes
Stop And Think:
Finding the intersection

Whether two sets are disjoint. 
The sloppy way is to go through all elements of one and store into a hash table and then go thru all elements of the other and if none match then they're disjoint. So that's N + M right?

This is the chapter on sorting--am I supposed to sort the items from biggest to smallest? So then I have to do an N log N sort and then M log M sort. And I can search thru stuff in N and M together in the range where they line up. How would I do that though? Binary search thru both?
Lol, it turned out that expected linear time through hashing was at the bottom. 

Okay, so the book says...

1. Sort the big set first. O( N log N) and binary search with each of the m elements in the other set to see if it exists in the big guy. O((n + m) log n)

2. Sort the small set first. O( m log m) and binary search the big set to see if it exists in the tiny guy. O((n + m) log m).

3. Sort both sets. No binary search needed. Compare smallest elements of both and discard smaller if they're not identical. Keep doing it til there's no more or til they match. O(n log n + m log m + n + m).

So the third is better if m and n add up to a big num that multiplies real hard for the first two, right?  Uhhh maybe not.
Small set sorting first is better since log m < log n when m < n. 
Sorting small set is apparently the best. 

## Cool sorting considerations:

1. Are we sorting ASC or DESC? 
2. Are we sorting the key or a whole record? We better keep track of record linkage. 
3. What do we do with equal keys? Secondary sort? Stable sorts are those that leave the items in same relative order, which usually needs a secondary key on the initial position. Skiena says most fast algos are not stable. 
4. What about non-numerical data? Collating sequence for punctuation?

You gotta think about the comparison function here. They can get passed as an argument to our sort procedure. Pretty common in many languages to have a comparator lambda or named function to pass in to a sort function.
Semi-related thought: Lodash library differenceWith has a comparator you pass in to detail what you're basing the difference on. 

## Heap Sort:

Heap sort is an implementation of selection sort using the right data structure! Cool! Because in selection sort you just grab the smallest in A which takes O(N) time and then you do it again for all elements in the array, so it is O(N^2). But if I am using a priority queue then look at that! Now the loop takes O(log N) time instead because getting the highest priority small thing from a priority queue takes log N. So now it's N log N, look at that. 

Heaps maintain a partial order on a set of elements. It's weaker than the sorted order but stronger than the random order. Makes it efficient to maintain (weak orders) and quick to find them mins. 

A Heap labeled tree is a binary tree where the key labelling of a node dominates the key labelling of its kiddos. 

Min heap is the smaller key dominates, max heap is the bigger key dominates. 

You can possibly store keys in a node with pointers to children in binary trees, but then the memory used by the pointers start outweighing size of keys. 

So instead if you store data as an array of keys and use the position of the keys to satisfy the pointe r roles, we do the whole 2 to the lth level from left to right with 2 to the l - 1 to 2 to the l minus 1. Array starts at index 1 then.

Left child of k is in position 2k, right child of k is in 2k + 1 then. Parent is in floor div n // 2. 

Move around the tree now sans pointers. 

If the tree is sparse though, then onw we have a bunch of gaps in our array. 

For a heap we better not have holes. We'll pack elements on the last level as far to the left as possible. So this array idea works well for heaps, not for binary search trees. We gotta move a bunch of elements in the subtree when we want things moved, no pointer magic here. 

### Stop and think:
How can we efficiently search for a particular key in a heap?

I guess we better just pull the item out until we find it!!!

Aw, solution says no searching possible, heap not a BST, relative order of everything is not known. So I guess I was right, gotta O(N) pull EVERYTHING OUT. 

[CONSTRUCT ME SOME HEAPS](kthsmallest.py)

## Sorting by Incremental Insertion

Select an arbitrary element from an unsorted set and put it in the proper position in the sorted set. 









