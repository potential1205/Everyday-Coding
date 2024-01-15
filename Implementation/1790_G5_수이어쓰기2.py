



if __name__ == "__main__":
    n,k = map(int,input().split())
    cnt = 0

    temp = n
    while temp > 0:
        cnt+=1
        temp = temp//10

    val = 9
    length = 0
    info = []

    for i in range(1,cnt+1):
        if val < n:
            gap = val*i
            length += gap
            n = n - (val)
            info.append([val,i])
            val = val*10
            
        else:
            break
    
    length += (cnt*n)
    info.append([n,cnt])



    if k > length:
        print(-1)
    else:

        std_val,std_idx = 0,0
        for i in range(len(info)):
            std_val += info[i][0]*(i+1)

            if std_val >= k:
                std_idx = i+1
                break
        
        std_val = 0
        for i in range(std_idx):
            std_val = 10**(i)
        
        std_order = 0
        for i in range(std_idx-1):
            std_order += (info[i][0]*info[i][1])


        gap_order = k-std_order-1


        result1 = std_val + (gap_order//std_idx)

        result1 = list(str(result1))

        print(int(result1[gap_order%std_idx]))
