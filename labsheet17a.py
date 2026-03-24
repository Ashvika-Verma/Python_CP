from collections import deque

# Input
n, e = map(int, input().split())

graph = [[] for i in range(n)]

for i in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

start = int(input())

# ---------------- BFS Traversal ----------------
visited = [False] * n
queue = deque([start])
visited[start] = True

print("BFS Traversal:", end=" ")

while queue:
    node = queue.popleft()
    print(node, end=" ")

    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append(neighbor)

# ---------------- DFS Traversal ----------------
visited = [False] * n

def dfs(node):
    visited[node] = True
    print(node, end=" ")

    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)

print("\nDFS Traversal:", end=" ")
dfs(start)