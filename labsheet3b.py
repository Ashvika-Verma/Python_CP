# Input
a, b, p, k = map(int, input().split())
# Modular multiplication
mod_prod = (a % p * b % p) % p
# Check divisibility
if mod_prod % k == 0:
    print("Divisible");
else:
    print("Not Divisible");