import heapq

# Input number of nodes and edges
n, e = map(int, input().split())

# Create adjacency list
graph = [[] for _ in range(n)]

# Read edges
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # Remove this line if graph is directed

# Source and destination
s, d = map(int, input().split())

# Initialize distances
dist = [float('inf')] * n
dist[s] = 0

# Priority queue
pq = [(0, s)]

# Dijkstra's Algorithm
while pq:
    current_dist, node = heapq.heappop(pq)

    # Skip outdated entries
    if current_dist > dist[node]:
        continue

    for neighbor, weight in graph[node]:
        new_dist = current_dist + weight

        if new_dist < dist[neighbor]:
            dist[neighbor] = new_dist
            heapq.heappush(pq, (new_dist, neighbor))

# Output result
if dist[d] == float('inf'):
    print("No Connection Found")
else:
    print("Shortest connection cost:", dist[d])