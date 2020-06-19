3-3. [5] We have seen how dynamic arrays enable arrays to grow while still achieving
constant-time amortized performance. This problem concerns extending dynamic
arrays to let them both grow and shrink on demand.
(a) Consider an underflow strategy that cuts the array size in half whenever the
array falls below half full. Give an example sequence of insertions and deletions
where this strategy gives a bad amortized cost.
(b) Then, give a better underflow strategy than that suggested above, one that
achieves constant amortized cost per deletion.

Sure, so if my array is right on the cusp...

Length is 8 for example. And I have 4 items. 

I delete an item. Now I have 3 items. 
Now the array size gets nommed to 4 items.
I add another item. Array is full.
Add another item. Now I copy it over to a new array. need to copy 5 items and allocate 8 array space. 

Do it again! Delete two items. reduction of array size. Add two. Need to copy it over again.
4 -> 3 -> 5 -> 3 -> 5
So really I just removed 1 item, added 2, removed 2 items, added 2. That's 7 item operations. 

For those ops I had to drop array size 2x and increase array size 2x. Let's say dropping costs like nothing. Well, the increase was still needing to copy 4 items and add the 5th, twice! so I did work equal to 10 things there. 7 + 10 is 17! double the cost. 

As opposed to if I didn't need to change array size, I just would have done 7 item operations and 0 extra moving around. 

another ex:

4 items in 8 capacity array.
Remove 1 item. Capacity becomes 4. Add 2 items. Capacity becomes 8. Remove 2. Cap 4. Add 2. Cap 8. 

So I did 7 item operations, but had to move 10 things, total 17. 

What's a better underflow strategy? Hey, I did think of this but I second guessed myself. When the array is less than 1/4th full, shrink it by half. 

Example:

4 items in 8 capacity array. 
Remove 3 items. Now it shrinks to 4 cap. 
Add 4 items, it expands to 8. Remove 4 items, it shrinks to 4 cap. Add 4 items, grows back to 8 cap. 

I did 15 item operations. I had to move 10 things. The item operation per movement is better. 

Is this the right way to think of it? 
