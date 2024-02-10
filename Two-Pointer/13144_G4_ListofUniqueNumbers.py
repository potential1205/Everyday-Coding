
if __name__ == "__main__":
    n = int(input())
    arr = [*map(int,input().split())]

    mem = [0] * 100001
    e = 0
    s = 0
    ret = 0
    while e < n:
        if not mem[arr[e]]:
            mem[arr[e]] +=1
            e +=1
        else:
            ret += (e-s)
            mem[arr[s]] -= 1
            s+=1

    ret += ((e-s) * (e-s+1)) // 2
    print(ret)
        



