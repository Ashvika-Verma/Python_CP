import heapq

n = int(input())
bids = list(map(int, input().split()))

pq = []

for b in bids:
    heapq.heappush(pq, -b)

if pq:
    highest = -heapq.heappop(pq)
    print("Highest Bid:", highest)

    if pq:
        print("Next Highest Bid:", -heapq.heappop(pq))