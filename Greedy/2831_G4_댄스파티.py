if __name__ == "__main__":
    n = int(input())
    men = list(map(int,input().split()))
    women = list(map(int,input().split()))

    left_men = []
    right_men = []

    left_women = []
    right_women = []

    for man in men:
        if man < 0:
            left_men.append(man)
        else:
            right_men.append(man)
    
    for woman in women:
        if woman > 0:
            left_women.append(woman)
        else:
            right_women.append(woman)
    
    idx = 0
    jdx = 0
    
    mlen = len(left_men)
    wlen = len(left_women)

    left_men.sort(reverse=True)
    left_women.sort()

    cnt = 0

    while True:
        if idx == mlen or jdx == wlen:
            break
        
        if abs(left_men[idx]) > abs(left_women[jdx]):
            cnt+=1
            idx+=1
            jdx+=1
        else:
            idx+=1


    idx = 0
    jdx = 0
    
    mlen = len(right_men)
    wlen = len(right_women)

    right_men.sort()
    right_women.sort(reverse=True)

    while True:
        if idx == mlen or jdx == wlen:
            break
        
        if abs(right_men[idx]) < abs(right_women[jdx]):
            cnt+=1
            idx+=1
            jdx+=1
        else:
            jdx+=1
    
    print(cnt)