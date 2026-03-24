def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][1] <= right[j][1]:   
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


while True:
    n = int(input("Enter number of racers (minimum 10): "))
    if n >= 10:
        break
    print("Error: At least 10 racers are required!\n")

racers = []
print("Enter racer time:")
for i in range(n):
    time = int(input())
    racers.append((i + 1, time))  

sorted_racers = merge_sort(racers)

print("\nTop 10 Racers:")
for i in range(10):
    print(f"Racer ID {sorted_racers[i][0]} : Time {sorted_racers[i][1]}")
