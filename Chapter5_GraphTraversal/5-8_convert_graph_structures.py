# Present correct and efficient algorithms to convert an undirected graph G be-
# tween the following graph data structures. You must give the time complexity of
# each algorithm, assuming n vertices and m edges.
# (a) Convert from an adjacency matrix to adjacency lists.
# (b) Convert from an adjacency list to an incidence matrix. An incidence matrix
# M has a row for each vertex and a column for each edge, such that M [i, j] = 1
# if vertex i is part of edge j, otherwise M [i, j] = 0.
# (c) Convert from an incidence matrix to adjacency lists.

# Ex:
#
#  0
#    \
#     1     4
#      \   /
#        2
#      /   \
#     3     5
#          /  \
#         6 -- 7
#

ex_adj_mat = [
    [0,1,0,0,0,0,0,0],
    [1,0,1,0,0,0,0,0],
    [0,1,0,1,1,1,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,1,0,0,0,1,1],
    [0,0,0,0,0,1,0,1],
    [0,0,0,0,0,1,1,0]
]

# Assumes graph number names are UNIQUE!

def convert_mat_to_list(mat):
    hashmap = {}
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]:
                if i not in hashmap:
                    hashmap[i] = [j]
                else:
                    hashmap[i].append(j)
    return hashmap

adj_list = convert_mat_to_list(ex_adj_mat)
print(adj_list)
# O(V^2) since we must go through every entry in the matrix.

# Assume that we get the number of edges as the input! Otherwise I'd have to iterate through and count them.

def convert_list_to_incidence_mat(list, num_edges):
    seen = set()
    mat = [[0 for j in range(num_edges)] for i in range(len(list))]
    edge_count = 0
    for i in range(len(list)):
        vertices = list[i]
        for v in vertices:
            tupl = tuple(sorted([i, v]))
            if tupl not in seen:
                mat[i][edge_count] = 1
                mat[v][edge_count] = 1
                edge_count += 1
                seen.add(tupl)
    return mat

matrix = convert_list_to_incidence_mat(adj_list, 8)
print(matrix)

def convert_incidence_mat_to_list(mat):
    hashmap = {}
    for j in range(len(mat[0])):
        u, v = -1, -1
        for i in range(len(mat)):
            if mat[i][j]:
                if u == -1:
                    u = i
                elif u != -1:
                    v = i
                elif v != -1:
                    raise Exception("Should only be 2 units of 1's in the column for the matrix")
        if u in hashmap:
            hashmap[u].append(v)
        else:
            hashmap[u] = [v]
        if v in hashmap:
            hashmap[v].append(u)
        else:
            hashmap[v] = [u]
    return hashmap

print(convert_incidence_mat_to_list(matrix))
