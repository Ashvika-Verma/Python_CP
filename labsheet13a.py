n = int(input())
dist = list(map(int, input().split()))
left = 0
right = n - 1
while left <= right:
   if left == right:
     print(dist[left], end=" ")
   else:
     print(dist[left], dist[right], end=" ")
   left += 1
   right -= 1