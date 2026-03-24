n = int(input())
speeds = list(map(int, input().split()))
d = int(input())
min_speed = speeds[0]
for s in speeds:
    if s < min_speed:
        min_speed = s
time_required = d / min_speed
print("Minimum Speed =", min_speed)
print(f"Maximum Time = {time_required:.2f} hours")