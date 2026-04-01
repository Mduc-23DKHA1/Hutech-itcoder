n = int(input())
arr = list(map(int,input().split()))

l = 0
len_max = 1
for r in range(1, n):
    if arr[r] != arr[l]:
        l = r
        len_max += 1
print(len_max)