# n = int(input("Enter N: "))
# arr = list(map(int, input().split()))
# arr.sort()
# print(arr[2])
# n = int(input("Enter N: "))
# arr = list(map(int, input().split()))
# arr.sort()
# for i in range(n):
#     print(arr[i])
# print("3rd element is:")
# print(arr[2])
n= int(input())
times=list(map(int,input().split()))
for i in range(1,n):
    key=times[i]
    j=i-1
    while j>=0 and times[j]>key:
        times[j+1]=times[j]
        j-=1
    times[j+1]=key
print(times[2])
