from collections import defaultdict

n = int(input())
arr = list(map(int,input().split()))

d = defaultdict(int)

d[arr[0]] += 1
key = arr[0]
cnt = 1

for i in range(1,n):
    d[arr[i]] += 1
    if d[arr[i]] > cnt:
        key = arr[i]
        cnt = d[key]
    elif d[arr[i]] == cnt:
        if arr[i] < key:
            key = arr[i]
            cnt = d[key]

print(f"{len(d.keys())} {key}")