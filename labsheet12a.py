n = int(input())
arr = list(map(int, input().split()))
minimum = arr[0]
for x in arr:
    if x < minimum:
        minimum = x
print("Minimum =", minimum)