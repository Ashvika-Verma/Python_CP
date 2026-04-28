import heapq

def fastest_path(n, graph, start, target):
    # (time, cost)
    dist = [(float('inf'), float('inf')) for _ in range(n + 1)]
    dist[start] = (0, 0)
    
    pq = [(0, 0, start)]  # (time, cost, node)
    
    while pq:
        time, cost, node = heapq.heappop(pq)
        
        if node == target:
            return time, cost
        
        if (time, cost) > dist[node]:
            continue
        
        for neighbor, t, c in graph[node]:
            new_time = time + t
            new_cost = cost + c
            
            # Check better condition
            if (new_time < dist[neighbor][0]) or \
               (new_time == dist[neighbor][0] and new_cost < dist[neighbor][1]):
                
                dist[neighbor] = (new_time, new_cost)
                heapq.heappush(pq, (new_time, new_cost, neighbor))
    
    return -1, -1

# Input
n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, t, c = map(int, input().split())  # time, cost
    graph[u].append((v, t, c))
    graph[v].append((u, t, c))  # remove if directed

start = int(input())
target = int(input())

time, cost = fastest_path(n, graph, start, target)

print("Fastest Time =", time)
print("Cost =", cost)