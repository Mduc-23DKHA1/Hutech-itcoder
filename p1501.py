from collections import defaultdict, deque
n,k = map(int,input().split())
exits = list(map(int,input().split()))
m = int(input())
doors = defaultdict(list)
for i in range(m):
    a,b = map(int,input().split())
    doors[a].append(b)
    doors[b].append(a)
step = [-1 for _ in range(n)]

d = deque()
for x in exits:
    d.append(x)
    step[x-1] = 0

while d:
    u = d.popleft()
    for v in doors[u]:
        if step[v-1] == -1:
            step[v-1] = step[u-1] + 1
            d.append(v)
print(*step)
