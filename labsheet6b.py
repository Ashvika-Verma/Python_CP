n= int(input())
arr = list(map(int, input().split()))
checksum=int(input("Enter checkSum"))
result = 0
for i in range(n):
    result = result ^ arr[i]

print(result)
if result==checksum:
    print("Okyy")
else:
    print("Anamoly")