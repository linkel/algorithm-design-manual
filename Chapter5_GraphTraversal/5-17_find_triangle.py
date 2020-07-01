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

def find_triangle_VE_time(mat):
    adj_list = convert_mat_to_list(mat)
    seen = set()
    for i in range(len(mat)):
        for u in adj_list[i]:
            if u not in seen:
                for v in adj_list[i]:
                    if v not in seen:
                        if mat[u][v]:
                            return True
        seen.add(i)
    return False

print(find_triangle_VE_time(ex_adj_mat))