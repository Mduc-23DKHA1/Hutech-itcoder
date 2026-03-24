cnt = 0
for i in range(int(input())):
    adv, real = map(float,input().split())
    cnt += 1 if adv > real * 1.5 else 0
print(cnt)