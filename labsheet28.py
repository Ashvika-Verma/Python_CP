import heapq

def dijkstra(n, graph, start, target):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    
    pq = [(0, start)]  # (cost, node)
    
    while pq:
        cost, node = heapq.heappop(pq)
        
        if node == target:
            return cost
        
        if cost > dist[node]:
            continue
        
        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))
    
    return -1  # if unreachable

# Input
n = int(input())  # nodes
m = int(input())  # edges

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # remove if directed

start = int(input())
target = int(input())

result = dijkstra(n, graph, start, target)

print("Minimum Cost =", result)