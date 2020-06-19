## Hashing and Strings 

Let's say we want to maintain a dictionary. 

Looking up an item in an array takes constant time when you have the index--so if we have a hash function mapping keys to integers, we can use the value that comes out of the hash function as an index into the array. Store the item at that position. 

If alpha's the size of the alphabet on which a given string S is written. 

Char(c) will be a function mapping symbols of the alphabet to a unique integer from 0 to alpha - 1. 

H(S) = sum from i = 0 to len(S) - 1: alpha to the power of len(S) - (i+1) * char(s sub i)

Creates real big numbers, they'll exceed the num of slots in hash table, let's call slots m. Reduce number to an integer between 0 and m - 1 via taking remainder of H(S) mod m. 

Ideally, m is a large prime not to close to 2^i - 1.

I have no idea why. 

## Collision Reduction 

Chaining is the easiest approach to collision reduction. We set up m linked lists and the ith list contains all the items that hash to the value of i. 

Chaining requires a lot of memory for pointers. If n keys are distributed uniformly in a table, each list contains roughly n/m elements. A constant size when m is about equal to n. 

Alternative: Open Addressing. 

Hash table is an array of elements, not buckets, each init to null. if the desired position is not empty, we would stick it in the next open spot. So the item should just be a few slots from the intended position. 