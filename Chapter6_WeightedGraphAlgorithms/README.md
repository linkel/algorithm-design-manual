# Skiena Chapter 6

## Minimum Spanning Trees
Minimum spanning tree algorithms: the two big guys
Prim's algorithm and Kruskal's algorithm. 

Prim's looks at the graph and at each node check the nearby weights and see which ones are smallest. Go down the smallest one and add it to the tree. Prim's works better for dense graphs than sparse ones. Why is that?

Minmum product spanning tree can be done by turning all the values into logarithms of the values, since lg(a * b) is equal to lg (a) + lg(b).

Also max sum spanning tree can be done by turning all the weights negative. 

A minimum bottleneck spanning tree, or a tree that minimizes the max edge weight over all such trees. Every MSt has this property. Can be proven using Kruskal's? 
