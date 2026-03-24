d, sT = map(int,input().split())
left = 0
right = 0
for i in range(d):
    mi, ma = map(int,input().split())
    left += mi
    right += ma
print("YES" if left <= sT <= right else "NO")