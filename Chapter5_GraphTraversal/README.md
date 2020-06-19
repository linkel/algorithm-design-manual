# Graphs Intro

Some basic DS and traversal for graphs to help me COBBLE TOGETHER solutions for basic graph problems, supposedly. 

A graph is defined on a set of vertices and has a set of edges of ordered or unordered pairs. 

G = (V,E) 

So the ordered pairs are directed graphs and unordered pairs are undirected, right? People also call 'em digraphs and graphs. 

Vertices could be cities or junctions connected by roads that are edges, if modelling a road network.

Vertices could be lines of code with edges connecting lines where the next is the next statement. 

Vertices could be people, connected by edges meaning certain relations. 

If the edge (x,y) exists in E implies that y,x is also in E, it's UNDIRECTED. Road networks between cities are usually undirected. Street networks with one way roads are directed. 

Program flow graphs are usually directed since execution is in one order. 

If each edge has a numerical value or weight, it's a weighted graph. Length, drive-time, speed limit, could all be weights. 

## Check out some WILD FLAVORS of graphs!!

undirected vs directed
weighted vs unweighted
simple vs nonsimple (seems to have reflexive loops and extra lanes between nodes. 
sparse vs dense (hey, what counts as dense?)
cyclic vs acyclic (cycles exist for a cyclic one, does it have to have all cycles? don't think so, probably just one counts, but acyclic needs zero cycles)
embedded vs topological (no fuckin' clue what the heck the swirly curls mean)
explicit vs implicit (UH just a but lump eating up the nodes?)
unlabelled vs labelled (this one is funny to me for some reason)


For unweighted graphs, shortest path must have the fewest # of edges and can be found using BFS. Shortest paths in weighted graphs need fancier algos. 

### Simple vs nonsimple:

Self loop is an edge involving one vertex. Multiedge if it occurs more than once in the graph. Any graph that doesn't have these features is called simple. 

### Sparse vs Dense:

Graphs are sparse when only a small fraction of the possible vertex pairs (n over 2? how do I read this notation?) for a simple, undirected graph on n vertices actually have edges defined between them. Graphs where a large fraction of the vertex pairs define edges are called dense. 

Typically dense graphs have a quadratic number of edges, while sparse graphs are linear in size. 

### Cyclic vs Acyclic:

An acyclic graph contains no cycles. Trees are connected, acyclic undirected graphs. 

Trees are the simplest interesting graphs, and are inherently recursive since if you chop any edge it leaves two smaller trees. Hahaha it LEAVES two smaller trees. 

Directed acyclic graphs are commonly shorted to DAGs. They are there in scheduling problems where ad irected edge of x,y indicates that x must occur before y. Like the math in that MIT course you were taking with the TA world domination plans problem. 

Topological sorting orders the vertices of a DAG to respect these precedence constraints. Toplogical sorting is usually the first step of any algo on a DAG. 

Man, it sounds so complex but maybe it's pretty understandable if I work on it. 

### embedded vs topological:

Graph is embedded if vertices and edges are assigned geometric positions. Any drawing of a graph is then an embedding. Sometimes the structure of a graph is completely defined by the geometry of its embedding! So if I get a collection of points in the plane and look for a tour visiting all of them like the TSP, then the underlying topology is the complete graph connecting each pair of vertices. Weights would then be defined by the Euclidean distance b/t each pair of points. Euclidean distance is ordinary straight line distance. Draw a line b/t the two points. 

### Implicit vs Explicit. 

Some graphs get constructed as we use them. Backtrack search has vertices that are the states of the vector while edges link pairs of states that can be directly generated from each other. It's usually easier to work with an implicit graph than to construct it explicitly prior to analysis. 

### labelled vs unlabelled:

Each vertex has a unique name for labelled. Isomorphism testing determines whether topological structure of two graphs are identical if we ignore any labels. Usually backtracking will solve these. 

## The Friendship Graph

Is such a graph directed? A "heard of you" graph is definitely directed. "had sex with" graph is undirected. 

How close a friend are you? Is there a weight for each friendship or enemy? If all edges are equal weight you can call it unweighted. 

Who has the most friends? Degree of a vertex is the number of edges adjacent to it. In a regular graph, each vertex has exactly the same degree. 

Do my friends live near me? An embedded graph would show where people live. Or where people worked. Proximity does seem to inform friendships. 

Do you also know her? Friendship graph can be explicit in things like LinkedIn or FB, but it's more implicit in the world since you can't find out who other people know unless you ask. 

Are you an individual? Is the friendship graph labelled or unlabelled? Do we care? 

So the terminology is helpful for thinking about how to model a graph. 

# Data Structures for Graphs 

Two basic choices we have are ADJACENCY MATRIXES and ADJACENCY LISTS. 

In an adjacency matrix, we represent the Graph G = (V,E) by using an n x n matrix M where element M[i,j] = 1 if (i, j) is an edge of G, and 0 if it isn't. So we can quickly answer "is (i,j) in G?" and also rapidly update anything for edge insertion and deletion. 

But it does use more space for graphs with many vertices and few edges. 

What if we had a street map of Manhattan? Manhattan's got 15 avenues crossing 200 streets--that's 3000 vertices. Since each vertex neighbors four other vertices and each edge is shared between two, it's probably 6000 edges. An adjacency matrix would have 3000 x 3000 cells, meaning 9 million cells, and most of them would be empty. 

Inherently quadratic. 

Adjacency lists let us more efficiently represent sparse graphs by using linked lists to store the neighbors adj to each vertex. 

It's harder to figure out if a given edge (i,j) is in G since we gotta do a search in the linked list for the edge. 

But Skiena says it's easy to design graph algos that avoid the need for those queries. He says we sweep thru all the edges of a graph in one pass through BFS or DFS and then update the implications of the current edge as we visit it. 

He asserts that adjacency lists are the right choice for most applications of graphs. 

# Traversing a Graph

Printing, copying graphs, converting them, are all applications of graph traversal. 

Any graph traversal algo needs to be powerful enough to get out of a maze. Because mazes are naturally represented by graphs, where vertex is the maze junction and edges are hallways. 

We have to not repeatedly look in the same place for efficiency, and we have to traverse systematically to correctly get out of the maze. We must be searching every edge and vertex. 

Mark vertices! 

- undiscovered -
- discovered - found but not visited all edges
- processed - all edges visited

Undirected edges get considered twice, directed edges get considered once, to explore the source vertex. 

Why does every piece need to get visited? suppose there exists a vertex u unvisited, whose neighbor v was visited. This neighbor v will eventually be explored, after which we will visit u. 

# Breadth First Search

Every edge gets a direction in a breadth first search of an undirected graph... There's the discoverer u and the discovered v. u will be the parent of v. 

Each node has exactly one parent except for the root. This defines a tree on the vertices of the graph. 

Shortest path problems can get solved by BFS. 

Let's see if I can translate his thing into Python.

def BFS(G, s):
    seen = {s}
    parents = {}
    Q = [s]
    while Q:
        u = Q.pop(0)
        print(u.data) # process the vertex as desired 
        for v in u.adj:
            print("travelling from ", u, " to ", v) # process edge
            if v not in seen:
                seen.add(v)
                parents[v] = u
                Q.append(v)
        seen.add(u)

Graph edges that do not appear in the breadth first search tree have special properties. For undirected graphs, nontree edges can point only to vertices on the same level as the parent vertex, or to vertices on the level directly below the parent. 

Okay, at first I thought nontree edge meant like an edge not in that tree diagram at all, but what it means is that it's the edges that point sideways since that doesn't follow the tree rules? Like you wouldn't go from 1 to 2 to 5 in the example graph, you'd go from 1 to 5 for the shortest path. 

By definition of a shorter path, that's how that works. So if I added a vertex where 6 is connected to 3, that's still fine since it is pointing to a level below it. But if I connect 7 to 3, and then connect 6 to 7, the 7 wouldn't be under 3--it'd be under 6, since that's a shortest path, so it'd stick to the tree dynamic and 3 and 7 would be on the same level which is valid. 

In a directed graph, a back pointing edge (u, v) can exist whenever v lies closer to the root than u does. 

## Implementation

Skiena uses two boolean arrays to maintain knowledge about each vertex. It starts off as discovered when visited then processed when all its outgoing edges are traversed. 

```
processed = []
discovered = []
parent = []

def initialize_search(graph):
    for i in range(1, g.num_vertices()):
        processed[i] = discovered[i] = False
        parent[i] = -1
```

Once a vertex is discovered, it gets put in a queue, and we process them FIFO. 

```
v - current vertex
y - successor vertex
*p - temp pointer

def bfs(graph, start):
    q = [start]
    discovered[start] = True
    while q:
        v = q.pop(0)
        process_vertex_early(v)
        processed[v] = True
        p = graph.edges[v]
        while p:
            y = p.y (???)
            if (processed[y] == False or g is directed)
                process_edge(v,y)
            if discovered[y] == False
                q.append(y)
                discovered[y] = True
                parent[y] = v
            p = p.next
        process_vertex_late(v)
```

I'm a bit confuzzled on the y = p -> y thing he has. 

I should try to implement this stuff myself in Python to better understand. 

Anyhow, you can process a vertex early on, or process the edge, or process the vertex at the end. So you could for instance count edges. 

