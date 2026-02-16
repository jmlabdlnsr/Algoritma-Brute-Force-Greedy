print("Nama : Jamal Abdul Nasir")
print("NPM  : 247006111015")
print("Kelas: A")
print()

class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            self.parent[rootB] = rootA


edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 1),
    ('B', 'D', 5),
    ('C', 'D', 8),
    ('C', 'E', 10),
    ('D', 'E', 2)
]

vertices = ['A', 'B', 'C', 'D', 'E']

edges.sort(key=lambda x: x[2])

uf = UnionFind(vertices)

mst = []
total_weight = 0

for u, v, w in edges:
    if uf.find(u) != uf.find(v):
        mst.append((u, v, w))
        uf.union(u, v)
        total_weight += w

    if len(mst) == len(vertices) - 1:
        break


print("Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"{u}-{v} ({w})")

print("Total bobot:", total_weight)