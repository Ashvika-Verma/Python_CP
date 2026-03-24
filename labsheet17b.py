from collections import deque

# Input
n, e = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

s, d = map(int, input().split())

# BFS to check path
visited = [False] * n
queue = deque([s])
visited[s] = True
found = False

while queue:
    node = queue.popleft()

    if node == d:
        found = True
        break

    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append(neighbor)

# Output
if found:
    print("Path Exists")
else:
    print("No Path Exists")