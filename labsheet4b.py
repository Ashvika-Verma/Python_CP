def factorial(n):
   fact = 1
   for i in range(1, n + 1):
     fact *= i
   return fact
# Input
N, K = map(int, input().split())
# Combination using factorials
result = factorial(N) // (factorial(K) * factorial(N - K))
print(result)
