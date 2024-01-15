

if __name__ == "__main__":
    m,n,c1,c2 = map(int,input().split())
    answer = 0

    rest_val = m + n
    max_val = max(m,n)
    min_val = min(m,n)

    if (rest_val)%2!=0:
        max_val -= 1
        answer += c1

    if 2*c1 >= c2:
        answer += (min_val*c2)
        max_val = max_val - min_val
        min_val = 0
    else:
        answer += (min_val*c1*2)
        max_val = max_val - min_val
        min_val = 0

    answer += (max_val * min(c1, c2))
    
    print(answer)
