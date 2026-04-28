import threading

highestBid = 0

def place_bid(bid):
    global highestBid
    if bid > highestBid:
        highestBid = bid

n = int(input())
threads = []

for _ in range(n):
    bid = int(input())
    t = threading.Thread(target=place_bid, args=(bid,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Highest Bid =", highestBid)