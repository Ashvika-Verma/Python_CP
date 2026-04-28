def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # path compression
    return parent[x]

def union(parent, rank, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    
    if rootA != rootB:
        if rank[rootA] < rank[rootB]:
            parent[rootA] = rootB
        elif rank[rootA] > rank[rootB]:
            parent[rootB] = rootA
        else:
            parent[rootB] = rootA
            rank[rootA] += 1

# Input
n = int(input())  # number of users
m = int(input())  # number of friendships

parent = list(range(n + 1))
rank = [0] * (n + 1)

# Existing friendships
for _ in range(m):
    a, b = map(int, input().split())
    union(parent, rank, a, b)

# Count components
components = set()
for i in range(1, n + 1):
    components.add(find(parent, i))

# Minimum new friendships needed
print("Minimum new friendships =", len(components) - 1)