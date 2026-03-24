n = int(input())
arr = list(map(int,input().split()))
s = arr[0]
s_max = arr[0]

for i in range(1,n):
    if s < 0: s = arr[i]
    else: s += arr[i]
    s_max = max(s_max, s)

print(s_max if s_max > 0 else 0)    