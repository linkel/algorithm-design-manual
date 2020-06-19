3-4. [3] Design a dictionary data structure in which search, insertion, and deletion can
all be processed in O(1) time in the worst case. You may assume the set elements
are integers drawn from a finite set 1, 2, .., n, and initialization can take O(n) time.


I was thinking some hash function to calculate. Some kind of mask. Python has an array where when you insert a key value pair, it calculates a hash from it to decide where in the array to stick it in. If it collides then it compares the key and hash there with your key and hash and if they are different, it runs the probing algo to find the next spot to throw it in. 

Answer online says something about bit array! I need to better conceptualize this... will move on for now. 