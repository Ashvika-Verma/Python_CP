import heapq

n = int(input())
bids = list(map(int, input().split()))

pq = []

for b in bids:
    heapq.heappush(pq, -b)

print(-pq[0])