# Basic Data Structures 
## Three fundamental abstract data types

1. Containers
2. Dictionaries
3. Priority Queues 

See how they can be implemented with lists!

## Contiguous vs Linked Data Structures 

1. Contiguously-allocated structures are composed of single slabs of memory, and include arrays, matrices, heaps, and hash tables. 
Arrays, like []! Matrices, like [[]]! Heaps like...a pile of stuff. With the biggest stuff on top, or the smallest stuff on top? I forget, they're like tree-ish? Hash tables, mapping with a hash function.

2. Linked data structures are composed of distinct chunks of memory bound together by pointers, and include lists, trees, and graph adjacency lists. Lists like a linked list. Trees having left or rights or an array of children (more pointers).

# Arrays

The fundamental contiguously-allocated data structure. Fixed-size data records such that each element can get located by its index. O(1) for getting a value out of the index. 

Space efficiency is pretty good since it's just in order and fixed-size. 

Memory locality -- all the memory bits are local, so since it's continuous and can get iterated through, it makes better use of cache memory on computers which are fast. 

But we can't adjust their size in the midst of program execution. Just allocating really big arrays is a waste of space if you use less of it. 

We can do dynamic arrays, though. So maybe we double size of the array from m to 2m each time we run out of space. Making a new array, and then copying the old array to the new one, then deallocating the old array. 

It will take lg n doublings until the array has n positions. Total work of managing the dynamic array is still O(n) huh. Gotta think a bit more about this. It's because on average, each of the n elements move only two times on adverage, and so technically it's like O(2n), but that's still the same O(n). 

What we lose when we use dynamic arrays is that we no longer know that every array access takes constant time on the worst case. On the worst case, the ones that trigger array doubling, those will end up taking linear time. 

So we get a promise that the nth array access will be completed fast enough that the total effort expended so far is O(n). It's an amortized guarantee. 

### Pointers and Linked Structures

Pointers represent the address of a location in memory. So a variable storing it to a given data item can provide more freedom than storing the copy of the item itself. A pointer p in C gives the address in memory where a chunk of data is located. *p is the item that is pointed to by pointer p, and &x is the address of a variable x. 

So if I make myself an object x, and I want its address it's gonna be &x. But if I have a pointer p and I want the item it points to, I do *p. 

typedef struct list {
item_type item;
struct list *next;
} list;

Hence in the above, that *next is a struct list! And next would be the pointer that points to it. 

Each node in this structure contains one or more data fields that contain the data I want to store. 

Each node contains a pointer field to at least one other node. So there's a lot of space used that stores pointers. 

And I need a pointer to the head of the structure so I can access it.

In doubly linked lists, each node points to predecessor and successor element. 

## searching a list

Searching can be done iteratively or recursively. 

If x is in the list, it's either the first element or located in the rest of it. This gets reduced to searching in an empty list which can't contain x. 

Remember the SML stuff? It's like that!

Here's my bastardized python mixed with C pseudocode.

def search_list(list l, element x):
	if l == NULL return NULL;
	if l.item == x:
		return l;
	else:
		return search_list(l.next, x);

It's like the SML 

fun search_list([], item) = []
	| search_list(x::xs, item) =
		if x == item
		then x
		else search_list(xs, item)

## Insertion into a list

Each new item can just get updated into the front if we don't care about any order. Then we have to update the pointer to the head of the structure, but don't have to traverse the list. 

void insert_list(list **l, item_type x)
{
	list *p; // temp pointer
	p = malloc(sizeof(list));
	p -> item = x;
	p -> next = *l;
	*l = p;
}

def insert_list(ls, x):
	head = new ListNode()
	head.item = x
	head.next = ls
	return head

Since Python doesn't really have pointers, returning the head of the list is kinda the closer way of doing that assigning of the object getting pointed to. In the C code, insert_list takes a pointer to a pointer that points to a list object and an item x. Then it allocates new memory for a temp pointer, and the object p's item is x and its next is the original list. Then where the list originally was is set to be pointer p. 

## Deletion from a linked list

We have to find a pointer to the predecessor of the item being deleted. Once I get to the item, I can't easily go back to the previous and remove that node.

A naive translation of Skiena's example to Python:

def predecessor_list(l, x):
    if not l or not l.next:
        return None
    if l.next.item == x:
        return l
    else:
        return predecessor_list(l.next, x)

First he checks that the list isn't null. If the list or the list's next is null, then it returns there. 

Second, if it does have a next that isn't null and the item is equal to the x we're looking for in that pointer, we return our list, since we found the item. Wherever we're returning, that "l" is going to be the node we're currently on. 

Otherwise, we continue the search with the next node. 

Predecessor points to the node we want to delete, and we want to overwrite what the next pointer is. We want our next pointer to go to the element after the one that's "doomed".

Next, Skiena shows a delete_list function. 

Naive translation of his example to Python:
(Truly, it's so convenient that Python doesn't deal with pointers. But I guess I should go back eventually and think about this in C/C++ in case it ever matters.)

def delete_list(l, x):
    # declarations here that aren't really necessary in Python
    # basically, we're gonna want the actual item pointer
    # then the predecessor pointer
    ptr = search_list(l, x)
    if ptr:
        pred = predecessor_list(l, x)
        if not pred:
            l = p.next
        else:
            pred.next = p.next
        # ha it's python I don't gotta free anything

Okay, so we make use of the two functions we were previously talking about inside of delete_list. We search up the list for the node that contains the item x. Once we've found it (if it exists!) we can then store the predecessor to that node that contains the item into our variable pred. 

If we don't have pred then we would just go to the next thing in the 

Darn, was writing the above in the airplane and consequently lost track of my thinking. Let's start over...

So we search the list for the element x and if it exists, we store it into the pointer. If pointer doesn't exist then there's nothing to delete. If it does exist, then we want to find the predecessor node, the one just before where we found x, and store that. If there isn't a predecessor it means it's the first node, right? So then we will set our list to the next one and delete that first node. And if there is a predecessor, then the predecessor's next gets set to the pointer of interest's next. Get rid of that guy. 

Cool! 
And in C we deallocate the memory so we gotta pass in the original node we tossed. 

## Comparison

Overflow on linked structures can't happen unless memory is actually full--whereas on static arrays it can happen since you say how much space you're allocating in the first place. 

Insertions and deletions are simpler in linked lists than arrays. Since the ones in arrays are in order, we would have to allocate new memory in order to keep the indexes next to each other after we've deleted one. 

With large records, moving pointers is easier and faster than moving the items themselves. Why? I don't totally get this. 

Array advantages are that linked structures need more space to store the pointer fields. 

Linked lists don't allow efficient random access to items. So I'd always have to traverse from that first node in, whereas with the array I can just throw in that index and access. 

Arrays allow better memory locality and cache performance than random pointer jumping. This is because it's all next to each other. 

Lists are recursive objects where if you chop the first elment off a linked list you get a smaller linked list at the end. Hey, this is also true for strings. 

Arrays, if you split the first k elements off an n element array, you get two smaller arrays of size k and n - k. So these, too, are recursive objects. 

Divide and conquer by using stuff like quicksort or binary search is possible since the objects are recursive! 

# Stacks and Queues

So remember when we were talking about containers, dictionaries, and priority queues? Containers are a DS where we can store and retrieve data items independent of content. 

Dictionaries, on the other hand, are abstract data types that retrieve based on key values or content. 

So containers can be distinguished by the retrieval order they allow...

The two most important types of containers!

Stacks -- LIFO. Use 'em when retrieval order doesn't matter! Process those batch jobs! Push 'n pop! LIFO also tends to happen when executing recursive algos. 

Queues -- FIFO. Fairest. Minimize the maximum time spent waiting. Avg waitnig time will be the same regardless of which you use. These are trickier to implement so use them when order matters. Enqueue and dequeue. These are the fundamental DS that controls BFS in graphs. 

If we know an upper bound on the size of the container we can statically allocate it to an array. Otherwise, linked list time. 

# Dictionaries

Dictionaries support 

1. Search(D, k) - given a search key k, return a pointer to the elment in dictionary D whose key value is k, if one exists
2. Insert(D, x) - Given a data item x, add it to the set in dictionary D.
3. Delete(D, x) - Given a pointer to a data item x in the dictionary D, remove it from D. 

Some DS also supports Max(D) or Min(D) where you get the item with the largest or smallest key from D. Then you can use it as a priority queue. Python's collections.Counter kinda supports a bit of this--there's probably a better example. 

Predecessor(D, k) or Successor(D, k) - retrieve the item from D whosoe key is immediately before or after k in sorted order. Now we can iterate through the elements of the data structure...

What are some examples where we want to use these operations? 

What if we want to remove all duplicate names from a mailing list, and print the results in sorted order? We initialize the empty dictionary D... whose search key is the record name. 


## Comparing Dictionary Implementations 1

What are the asymptotic worst-case running times for each of the seven fundamental dictionary operations? 

Let's start with implementing a dictionary as an unsorted array. 

I did this in a notebook, not too keen on transcribing at the moment. 

Couple of fun things, I guess:

For finding the max element in an implementation that is a singly or doubly linked list that is sorted, naively since the max element is at the end of the list you'd have to take O(n) time, right? But then if you save a pointer to the tail, you can just update that pointer on insertion and deletion for doubly linked lists so it's still O(1) time. And furthermore for a singly linked list, we can instead make deletion cost O(2n) to update the tail pointer. So like if you delete the last node, go thru again to find the last item and save that memory location. So then deletion is still linear but the max is now constant since we saved it. 

A--B--C

A--C

Iterate through A then C and find that C is the last node now, so it's the one we save. 

A--B--C

A--B

Iterate through A then B and find that B is the last node, so it's the one we save. 