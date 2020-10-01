# Skiena Ch 5 Problems

## 5-1a:
BFS starting from vertex A
G1: ABDICEGJFH
G2: ABECFIDGJMHKNLOP

By levels visited:
G1
```
A
BDI
CEGJ
FH
```

G2
```
A
BE
CFI
DGJM
HKN
LGP
```

## 5-1b:
DFS Starting from Vertex A:
G1
A -> B -> C -> E -> D -> G -> H -> F -> J -> I

G2
A -> B -> C -> D -> H -> G -> F -> E -> I -> J -> K - > L -> P -> O -> N -> M

## 5-2
Topological sort of following graph G
ABDECFHGIJ

## 5-3
Prove by induction that there's a unique path between any two vertices in a tree.

Base case where there's only one path in the tree is where you have a root and a child node.
That path is unique.
We could add another node to the tree. If we add a node to root, it's also a unique path from root to that new child.
If we add a node to that child node, it's the original unique path plus the path to that child, which is unique because it had the one path between the first child and the second child.
So as you keep adding nodes to this path it stays a unique path.

## 5-4
Prove that in a BFS search on an undirected graph G, every edge is either a tree edge or a cross edge where x is not an ancestor or descendant of y in cross edge (x,y)

If I'm BFS on undirected graph, then when we visit vertex u then vertex v, there's a time + n when we visit v compared to u.
When I go from vertex u to v in a step, u is ancestor of v. 

If I am at a vertex and I hit another vertex that's already been visited, that's a cross edge where the two are neither
ancestor nor descendant of each other. 

If we assume that we can have a BFS traversal on undirected graph where the edge is NOT a tree edge and NOT a cross edge, it means we need
two vertices to have an edge connecting them but it isn't a tree or a cross edge... 

But by the definition we laid out of all the edges possible, if an edge isn't a tree edge (not
an ancestor and not a descendant) but there is an edge between them, then it's a cross edge. There's only room for 2 edge types in our BFS undirected.
If we were directed we could have back and forward edges but in BFS we don't. How to prove this better?

## 5-5
Give a linear algo to compute the chromatic number of graphs (how many colors we need to color graphs so no vertexes next to each other are same color) where each vertex has degree
at most 2.

I could use BFS and traverse starting from a node. I will swap the colors back and forth as I go thru the graph and record a set or a list of what's been visited. If I hit a node that's already been visited we know that we've got the triangle
cycle somewhere and that means we need to use 3 colors. This is linear since it goes through all nodes in the tree.

### Must such graphs be bipartite?
No, we could have a triangle. That's not bipartite. Bipartite here I think means that you can color it with 2 colors (chromatic number 2).

## 5-6
Todo: scan a picture of graphs drawn for this

## 5-7
See py file in same folder.
Can use preorder to determine current root and use inorder to determine the left and right subtree.
But with just preorder and postorder there are tree types that cannot be differentiated. 

## 5-8
See py file in same folder.
I used a hashmap to represent the adjacency list. 

## 5-9
Recursive solution written in py file in same folder. 

## 5-10
> [5] Suppose an arithmetic expression is given as a DAG (directed acyclic graph)
with common subexpressions removed. Each leaf is an integer and each internal5.11
EXERCISES
node is one of the standard arithmetical operations (+, −, ∗, /). For example, the
expression 2 + 3 ∗ 4 + (3 ∗ 4)/5 is represented by the DAG in Figure 5.17(b). Give
an O(n + m) algorithm for evaluating such a DAG, where there are n nodes and
m edges in the DAG. Hint: modify an algorithm for the tree case to achieve the
desired efficiency.

This is a riff on the previous problem--in my head, I believe caching previous results reaches the time complexity desired.

## 5-11

> [8] The war story of Section 5.4 (page 158) describes an algorithm for constructing
> the dual graph of the triangulation efficiently, although it does not guarantee linear
> time. Give a worst-case linear algorithm for the problem.

To recap, this one is the dual graph triangle problem. Graph has a vertex for every triangle of the mesh, with an edge between
every pair of vertices representing adjacent triangles. 

The algorithm proposed by Skiena has a data structure that is an array with one object for each vertex in the data set.
The object is a list of all triangles that pass through the vertex. 
1. When reading in a new triangle, we array access via vertex the three
relevant vertices in the array to get the three lists and then compare each list against the new triangle. 
2. For every tirangle-pair that shares two vertices, add an adjacency to graph. 
3. Add new triangle to each of the three lists. 

## 5-12
>[5] The square of a directed graph G = (V, E) is the graph G 2 = (V, E 2 ) such that
(u, w) ∈ E 2 iff there exists v ∈ V such that (u, v) ∈ E and (v, w) ∈ E; i.e., there is
a path of exactly two edges from u to w.
Give efficient algorithms for both adjacency lists and matrices.

See the problem 5-12 in folder. For the adjacency list, I have an outer loop that accesses each item i in the hashmap. I have an inner loop going through each list
that the value for i contains. For each item j in that list I access it in the hashmap and append the values found in the list (j's values in hashmap)
to i's list if they're not already there. 

For the adjacency matrix, I can go through each item i, and for each node it's connected to j, grab j's row and OR it with i's row. 

## 5-13
>[5] A vertex cover of a graph G = (V, E) is a subset of vertices V  such that each
edge in E is incident on at least one vertex of V  .
>
>(a) Give an efficient algorithm to find a minimum-size vertex cover if G is a tree.
>
>(b) Let G = (V, E) be a tree such that the weight of each vertex is equal to the
degree of that vertex. Give an efficient algorithm to find a minimum-weight
vertex cover of G.
>
>(c) Let G = (V, E) be a tree with arbitrary weights associated with the vertices.
Give an efficient algorithm to find a minimum-weight vertex cover of G.

For part a, I can go through the tree recursively and find leafs. If it's a leaf, mark its parent for saving into the result array.
If a node got marked, then its parent shall not be marked. If a node didn't get marked, its parent should get marked. 
Since a node has a left subtree and a right subtree, if it gets info that the node should get marked from at least one of the subtrees,
the node will get marked (it means one kid's a leaf and the other isn't). 

(Originally I thought I could just mark all nodes that weren't leaves but that doesn't give us the min size vertex cover)

b)
The min weight vertex cover if all node weights are their degree is just pick alternating levels starting from root. 
The constraint of the degree to weight ensures that this is always the right answer. 

c)
The min weight vertex cover for arbitrary weights involves deciding whether to pick the current node or to pick its kids instead. 
We can track as we traverse the tree the weights if we had chosen our node or if we hadn't, as well as the vertexes chosen for each one.
At the end we compare the two and return the best. 

## 5-14
>[3] A vertex cover of a graph G = (V, E) is a subset of vertices V  ∈ V such that
every edge in E contains at least one vertex from V  . Delete all the leaves from any
depth-first search tree of G. Must the remaining vertices form a vertex cover of G?
Give a proof or a counterexample.

If I have a DFS search tree of G and delete the leaves I'm always keeping one end of all the edges that connected the now-gone-leaves with the other node.
So it is a vertex cover. If we try to make a counterexample and picture that we've deleted leaves but the remaining vertices are not vertex covers, that means
that in deleting some leaf we got rid of both ends of an edge. That could be possible if two leaves were connected to each other and weren't connected to the rest of the graph.
But then that wouldn't be a tree--it's some kinda disconnected graph chunk, and further more one of those nodes wouldn't be a leaf of a DFS search tree in the first place.

## 5-15

>[5] A vertex cover of a graph G = (V, E) is a subset of vertices V  ∈ V such that
every edge in E contains at least one vertex from V  . An independent set of graph
G = (V, E) is a subset of vertices V  ∈ V such that no edge in E contains both
vertices from V  .
>
>An independent vertex cover is a subset of vertices that is both an independent set
and a vertex cover of G. Give an efficient algorithm for testing whether G contains
an independent vertex cover. What classical graph problem does this reduce to?

Since a vertex cover can be up to all the nodes as long as everything's covered, and an independent set can be down to one node,
combining the two makes it so that we need exactly one node from each edge. 

We can perform a breadth-first-search where we track what we've seen and note whether it was selected or not. This is like
a 2-coloring problem--if the graph can be 2-colored then it's got an independent vertex cover! See python file. I should probably try more 
test cases for my code.

## 5-16

>[5] An independent set of an undirected graph G = (V, E) is a set of vertices U
such that no edge in E is incident on two vertices of U .
>
>(a) Give an efficient algorithm to find a maximum-size independent set if G is a
tree.
>
>(b) Let G = (V, E) be a tree with weights associated with the vertices such that
the weight of each vertex is equal to the degree of that vertex. Give an efficient
algorithm to find a maximum independent set of G.
>
>(c) Let G = (V, E) be a tree with arbitrary weights associated with the vertices.
Give an efficient algorithm to find a maximum independent set of G.

For a) we can pick all leaves, then exclude them and their parents, and pick all leaves again recursively til we have run over
all the nodes in the tree. 

I'm assuming b) wants maximum weight independent set? In which case I think it's actually the same as our minimum weight
vertex cover! 


> 5-17. [5] Consider the problem of determining whether a given undirected graph G =
(V, E) contains a triangle or cycle of length 3.
>
> (a) Give an O(|V | 3 ) to find a triangle if one exists.
>
> (b) Improve your algorithm to run in time O(|V |·|E|). You may assume |V | ≤ |E|.
Observe that these bounds gives you time to convert between the adjacency matrix
and adjacency list representations of G.

For a), for every node in the graph we can take 3 steps in a depth first search along all paths from the starting node and if we end up back
at the node we started at, it means there's a triangle. The subroutine would be a depth first search that quits after taking 3 steps and checking if the node we are at is the same
as the node we began on. For example if we have 
```
1 ---- 2 ----- 3
         \
           4
```           
And we began at 1, so when we're at 1 we find that there's 2. We go to 2, and this is one step. At two we find that it has 3 and 4, so we will have to 
traverse both. When we're at 3, that is 2 steps so far, and there's no other node to go to. So we're done. Back up, then go to 4, and that's 2 steps so far
with no other node to go to so we're done. Now we have to do the same subroutine for node 2. then 3, then 4. 


b) To get V * E time, we set up an adjacency list and an adjacency matrix. We can start at a vertex and look at the vertices that it is connected to (like values in its adjacency list entry).
We do a doubly nested loop here, comparing each vertex to another one to see if matrix[v1][v2] is equal to 1. If it is, then we have a triangle.
When we finish processing the vertex we add it to a set of "checked", because if we were at vertex 0 and found that none of vertices 1, 2, 3, and 4 it was
connected to are connected to each other, then when we look at vertex 1 we can skip over comparing 0 to anything since we've already exhausted it--it can't be part of a triangle because we would have seen it checking through earlier.
If we do this, then the time complexity of this search will be at most V * E. 


> 5-18. [5] Consider a set of movies M 1 , M 2 , . . . , M k . There is a set of customers, each one
of which indicates the two movies they would like to see this weekend. Movies are
shown on Saturday evening and Sunday evening. Multiple movies may be screened
at the same time.
>
> You must decide which movies should be televised on Saturday and which on Sun-
day, so that every customer gets to see the two movies they desire. Is there a
schedule where each movie is shown at most once? Design an efficient algorithm to
find such a schedule if one exists.

I at first tried to do this via hashmap of key being movie and value being the day, and going through a set of if conditions.
But then it was easily defeated with something like:
customer  movies
1        a, b
2        e ,f
3        a, e

where if I was greedily assigning a to sat and b to sun and e to sat and f to sun then customer 3 gets screwed. 

Instead it seems like I should use graphs, since this is a problem in the graph section. 

How about if we designate each movie as a node and then if a customer has a preference on movie, connect those two nodes with an edge.
Then we see if the graph is two-colorable. If it is, then a schedule exists. We can traverse the graph and alternate colors, sticking the movie name into the appropriate Sat or Sunday set/list that it belongs to.
Otherwise if it isn't two-colorable, then a schedule does not exist where the movie is shown as most once. 

>5-19. [5] The diameter of a tree T = (V, E) is given by
max δ(u, v)
u,v∈V
(where δ(u, v) is the number of edges on the path from u to v). Describe an efficient
algorithm to compute the diameter of a tree, and show the correctness and analyze
the running time of your algorithm.


> 5-20. [5] Given an undirected graph G with n vertices and m edges, and an integer k,
give an O(m + n) algorithm that finds the maximum induced subgraph H of G
such that each vertex in H has degree ≥ k, or prove that no such graph exists. An
induced subgraph F = (U, R) of a graph G = (V, E) is a subset of U of the vertices
V of G, and all edges R of G such that both vertices of each edge are in U .

Had some thoughts here about using DFS, but need to refine those thoughts.

> 5-21. [6] Let v and w be two vertices in a directed graph G = (V, E). Design a linear-
time algorithm to find the number of different shortest paths (not necessarily vertex
disjoint) between v and w. Note: the edges in G are unweighted.

Using breadth first search, we queue up each node connected to our current node and process it as usual. 
If we have found w from v, we would start the counter, process the rest of this "level" of BFS and count up all the ones that are in this level. These would all be different shortest paths (not necessarily vertex disjoint, meaning they may overlap). All of the shortest paths found will be on the same level because this is unweighted. 

> 5-22. [6] Design a linear-time algorithm to eliminate each vertex v of degree 2 from
a graph by replacing edges (u, v) and (v, w) by an edge (u, w). We also seek to
eliminate multiple copies of edges by replacing them with a single edge. Note that
removing multiple copies of an edge may create a new vertex of degree 2, which has
to be removed, and that removing a vertex of degree 2 may create multiple edges,
which also must be removed.

