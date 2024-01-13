

if __name__ == "__main__":
    m,n,c1,c2 = map(int,input().split())

    result = m*c1 + n*c1

    cnt = 0
    y,x = 0,0
    while True:
        if y==n or x == m:
            break
        y +=1
        x += 1
        cnt+=1
    print(cnt)


