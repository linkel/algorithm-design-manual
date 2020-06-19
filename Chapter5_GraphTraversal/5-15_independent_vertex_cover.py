# [5] A vertex cover of a graph G = (V, E) is a subset of vertices V  ∈ V such that
# every edge in E contains at least one vertex from V  . An independent set of graph
# G = (V, E) is a subset of vertices V  ∈ V such that no edge in E contains both
# vertices from V  .
# An independent vertex cover is a subset of vertices that is both an independent set
# and a vertex cover of G. Give an efficient algorithm for testing whether G contains
# an independent vertex cover. What classical graph problem does this reduce to?

def has_independent_vertex_cover(adjlist):
    seen = {}
    if not adjlist:
        return True # Is an empty graph vertex covered?
    q = [0]
    pick = 1
    while q:
        length = len(q)
        # alternate our color every level down
        pick = pick ^ 1
        for _ in range(length):
            curr = q.pop(0)
            if curr in seen:
                # if it's been seen before we have a cycle, so check the coloring
                if seen[curr] != pick:
                    return False
            else:
                # if we haven't seen it before we will process it
                seen[curr] = pick
                for v in adjlist[curr]:
                    q.append(v)
    return True

# I feel like the way I've written this it does double-checks on previous nodes a lot, so it's like 2N.

adjlist_with_good_cycle = {
    0: [1],
    1: [0, 2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3, 5],
    5: [4]
}

adjlist_with_bad_cycle = {
    0: [1],
    1: [0, 2, 3],
    2: [1, 3, 4],
    3: [1, 2, 4],
    4: [2, 3, 5],
    5: [4]
}

print(has_independent_vertex_cover(adjlist_with_good_cycle))

print(has_independent_vertex_cover(adjlist_with_bad_cycle))
