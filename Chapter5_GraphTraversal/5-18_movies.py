ex = [('A','B'), ('E', 'F'), ('A', 'E')]

# Make undirected graph where edges represent customer preference of the two movies that are connected by that edge and nodes are the movies
# It returns a hashmap where the movie is the key and the value is 0 or 1, where 0 is Sat and 1 is Sun for the scheduling.
def find_movie_schedule(customers):
    # we can create the graph in the form of an adjacency list
    g = {}
    for cust in customers:
        first = cust[0]
        second = cust[1]
        if first in g:
            g[first].append(second)
        else:
            g[first] = [second]
        if second in g:
            g[second].append(first)
        else:
            g[second] = [first]

    start_node = cust[0][0]
    movieToDay = {}
    queue = [start_node]
    curr_color = 1
    while queue:
        curr_color = curr_color ^ 1
        length = len(queue)
        for _ in range(length):
            node = queue.pop(0) # pretend python pop(0) is O(1) here, otherwise use a double ended deque to be legit
            if node in movieToDay:
                if curr_color != movieToDay[node]:
                    return 'Cannot create a valid movie schedule'
            else:
                for v in g[node]:
                    queue.append(v)
                movieToDay[node] = curr_color

    return movieToDay

print(find_movie_schedule((ex)))

notwork_ex = [('A','B'),('C','A'),('B','C')]

print(find_movie_schedule((notwork_ex)))

longer_works = [('A','C'), ('A', 'B'), ('B','D'), ('D','E'), ('B','F'), ('F','E')]

print(find_movie_schedule((longer_works)))