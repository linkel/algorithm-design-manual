import collections
import copy
# The square of a directed graph G = (V, E) is the graph G 2 = (V, E 2 ) such that
# (u, w) ∈ E 2 iff there exists v ∈ V such that (u, v) ∈ E and (v, w) ∈ E; i.e., there is
# a path of exactly two edges from u to w.
# Give efficient algorithms for both adjacency lists and matrices.

# Basically if we have a graph G we're drawing extra arrows from each node
# to nodes that it can access exactly 2 steps away.

ex = {
    1: [3],
    2: [],
    3: [2,4,5],
    4: [],
    5: [6],
    6: []
}

# This mutates the input.

def square_adjacency_list(adj):
    for k in adj:
        to = adj[k][:]
        set_to = set(to)
        for node in to:
            twostep = adj[node]
            for v in twostep:
                # in case of cycles
                if v not in set_to:
                    adj[k].append(v)
    return adj

# print(square_adjacency_list(ex))

# this version doesn't mutate the input. Still have to be careful of cycles.
# At first I thought this was buggy because it was giving a different answer
# but then--duh, I'm mutating it in the last call and passing it back in. Whoops
def square_adjacency_list_nonmutate(adj):
    new_adj = {key: value[:] for key, value in adj.items()}
    for k in new_adj:
        to = new_adj[k][:]
        set_to = set(to)
        for node in to:
            twostep = new_adj[node]
            for v in twostep:
                # in case of cycles
                if v not in set_to:
                    new_adj[k].append(v)
    return new_adj

# print(square_adjacency_list_nonmutate(ex))

cycle_ex = {
    1: [3],
    2: [],
    3: [2,4,5],
    4: [],
    5: [6],
    6: [3]
}

print(square_adjacency_list_nonmutate(cycle_ex))
print(square_adjacency_list(cycle_ex))

# Square of a digraph for matrix representation

# Let's use this guy

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

def square_the_matrix(matrix):
    # make my copy
    new_matrix = [[matrix[i][j] for j in range(len(matrix[i]))] for i in range(len(matrix))]

    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            if matrix[i][j]:
                get_row = matrix[j]
                for n in range(len(new_matrix)):
                    new_matrix[i][n] |= get_row[n]

    return new_matrix

print(square_the_matrix(ex_adj_mat))

# and the mutating version is similar, won't repeat myself.
# I use the or equals since what's happening is really that you're adding the row contents to the current one
# and if it's already 1 you leave it as one. You're travelling into each 1 in the adjacency matrix to check that vertex's
# connections and adding them into the row you're currently in. 