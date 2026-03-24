def mod_exp(a, m, p):
    result = 1
    a = a % p
    while m > 0:
        if m % 2 == 1:
            result = (result * a) % p
        a = (a * a) % p
        m //= 2
    return result
# INPUT
n, p = map(int, input().split())
total = 0
for _ in range(n):
    a, m = map(int, input().split())
    total = (total + mod_exp(a, m, p)) % p
# OUTPUT
print(total)
