n, m = map(int, input("Enter n and m: ").split())
arr = list(map(int,input("Enter array elements (numbers only): ").split()))
total = 0
for num in arr:
    total = (total + num) % m
print("Result:", total)
