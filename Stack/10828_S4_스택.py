from collections import deque
import sys


if __name__ == "__main__":
    n = int(input())
    stack = deque([])

    for i in range(n):
        command = input().split()
        if command[0] == 'push':
            stack.append(command[1])
        elif command[0] == 'top':
            if stack:
                print(stack[-1])
            else:
                print(-1)
        elif command[0] == 'size':
            print(len(stack))

        elif command[0] == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        
        elif command[0] == 'pop':
            if stack:
                num = stack.pop()
                print(num)
            else:
                print(-1)

