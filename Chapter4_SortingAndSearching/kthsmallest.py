class PriorityQueue: # let's make it size 20
    def __init__(self):
        self.n = 0
        self.q = [None for i in range(21)]

    def peek(self):
        return self.q[1]

    def pq_parent(self, n):
        if n == 1: return -1
        else: return n // 2

    def pq_young_child(self, n):
        return (2 * n)

    def pq_swap(self, x, y):
        self.q[x], self.q[y] = self.q[y], self.q[x]

    def insert(self, x):
        if self.n >= 20:
            print("Overflowing priority queue size")
            raise Exception
        else:
            self.n = self.n + 1
            self.q[self.n] = x
            self.bubble_up(self.n)
    def bubble_up(self, n):
        if self.pq_parent(n) == -1: return

        if self.q[self.pq_parent(n)] > self.q[n]:
            self.pq_swap(n, self.pq_parent(n))
            self.bubble_up(self.pq_parent(n))
            


def pq_young_child(n):
    return (2 * n)

def heap_compare(q, i, count, x):
    if count <= 0 or i > q.n: return count
    if q.q[i] < x:
        count = heap_compare(q, pq_young_child(i), count - 1, x)
        count = heap_compare(q, pq_young_child(i) + 1, count, x)
    
    return count
# result of this is the number of elements up to k count that are bigger or equal to x
pq = PriorityQueue()
pq.insert(4)
pq.insert(2)
pq.insert(45)
pq.insert(32)
pq.insert(22)
pq.insert(17)
pq.insert(11)

print(pq.peek())

print(heap_compare(pq, 1, 4, 11))
# print(heap_compare(pq, 1, 4, 11))
# so the above answers 2, it is saying "the 4th smallest element is bigger than or equal to
# x and the 3rd smallest element is bigger than or equal to x, but the 
# 2nd and the smallest elements are not bigger or equal to x
#  "