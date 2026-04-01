m, n, k = map(int,input().split())
def gcd(a,b):
    while b:
        a, b = b, a % b
    return a
g = gcd(m,n)
for i in range(g,0,-1):
    if g % i == 0:
        k -= 1
        if k == 0:
            print(i)
            break