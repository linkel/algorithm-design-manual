# Big O Notation Stuff

There's 

1. O(g(n))
2. Omega(g(n))
3. Theta(g(n))

O is the worst case, upper bound. 

Omega is the best case, lower bound.

Theta is both, one where both O and Omega are satisfied. 

If an equation can be said to equal O(n), it means that for a chosen constant c, for some values of n more than an n0, the equation will be less than n. 

Ex:

3n^2 + 100n + 10 is O(n^2) because if I select a constant c = 4, then 3n^2 + 100n + 10 < 4n^2 for values of n greater than for example 1000 (the actual nvalue can be smaller here but I'm picking one that works for sure).

## Some neat problems thinking a little outside of the box

Rearrange equations and stuff to figure out whether an equation satisfies something! 

# Runtimes

Neat, linear and n lg n stuff is practical up to a billion items! 2^n and n! is useless really fast, like for 30 items. But they'd work for 10 items. 

n^2 is kinda tolerable to 10,000 items. 

lg n can handle items seemingly for ages. It's under a microsecond for everything up to a billion and probably a while on.

# Dominance Relations

When a faster growing relation grows faster than a slower one, we say it DOMINATES it. g dominates f when f(n) = O(g(n)) when they're in a different class, aka their theta is not the same. 

You know most of these already--

Constant - no dependence on n, adding, printing 
Logarithmic - binary search
Linear - looking at each item in an n-element array
Superlinear (n lg n) - quicksort mergesort
Quadratic n^2 - looking at pairs of items, insertion/selection sort
Cubic n^3 - these come up in some DP algos
Exponential 2^n - enumerating all subsets of n items
Factorial (n!) - generating all permutations or orderings of n items

# Adding Functions

Sum of two functions is governed by the dominant one. At least half the bulk of f(n) + g(n) is going to come from the larger one. So dropping the smaller one only reduces the value by at most a factor of 1/2, which is a multiplicative constant. 

# Multiplying Functions

Cannot affect a function by multiplying by a constant c since the big O stuff would just scale the c up to still be in the same class. But if functions multiply other functions, they're both important. O(n! log n) dominates n! just as much as log n dominates 1. 

# Big O relationships are transitive

If f(n) = O(g(n)) and g(n) = O(h(n)) then f(n) = O(h(n))

Hmm, I know for sure that they are. How to show it?

They're kind of like the greater than and less than relations. 

If equation 1 is < equation 2, and equation 2 < equation 3, then yeah equation 1 is < equation 3.