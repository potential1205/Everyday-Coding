import sys
input = sys.stdin.readline

def dfs(root,s,e):
    for i in range(s,e):
        if inorder[i] == preorder[root]:
            dfs(root+1,s,i)
            dfs(root+i+1-s, i+1, e)
            print(preorder[root],end=' ')

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    preorder = list(map(int,input().rstrip().split()))
    inorder = list(map(int,input().rstrip().split()))
    dfs(0,0,n)
    print("")