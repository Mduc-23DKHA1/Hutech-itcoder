def mat(n : str, r : int):
    s = 1
    for i in range(1,r):
        if int(n[i]) < 4:
            return 0
        elif int(n[i]) == 4:
            continue
        elif int(n[i]) >= 7:
            s *= 2
    return s
    
def solve(n : str):
    r = len(n)
    if int(n[0]) < 4:
        return 2**r - 2
    elif int(n[0]) == 4 :
        return mat(n, r) + 2**r - 2
    elif 4 <= int(n[0]) < 7:
        return 3 * 2**(r-1) - 2
    elif int(n[0]) == 7:
        return mat(n, r) + 3 * 2**(r-1) - 2
    else:
        return 2**(r+1) - 2
    
if __name__ == "__main__":
    n = str(input())
    print(solve(n))
