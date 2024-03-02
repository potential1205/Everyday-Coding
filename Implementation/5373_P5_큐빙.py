



if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        opes = list(input().split())
        
        cube = [
            [['r','r','r'],['r','r','r'],['r','r','r']], 
            [['g','g','g'],['g','g','g'],['g','g','g']],
            [['b','b','b'],['b','b','b'],['b','b','b']],
            [['y','y','y'],['y','y','y'],['y','y','y']],
            [['w','w','w'],['w','w','w'],['w','w','w']],
            [['o','o','o'],['o','o','o'],['o','o','o']]
        ]
        
        # cube[0] : 앞쪽
        # cube[1] : 왼쪽
        # cube[2] : 오른쪽
        # cube[3] : 아래쪽
        # cube[4] : 위쪽
        # cube[5] : 뒤쪽

        for ope in opes:
            a,b = ope[0],ope[1]

            if a == 'U':
                if b == '+':
                    temp1,temp2,temp3 = cube[0][0][0],cube[0][0][1],cube[0][0][2]
                    cube[0][0][0],cube[0][0][1],cube[0][0][2] = cube[2][0][0],cube[2][0][1],cube[2][0][2]
                    cube[2][0][0],cube[2][0][1],cube[2][0][2] = cube[5][0][0],cube[5][0][1],cube[5][0][2]
                    cube[5][0][0],cube[5][0][1],cube[5][0][2] = cube[1][0][0],cube[1][0][1],cube[1][0][2]
                    cube[1][0][0],cube[1][0][1],cube[1][0][2] = temp1,temp2,temp3
                    cube[4] = list(map(list,zip(*cube[4][::-1])))
                elif b == '-':
                    temp1,temp2,temp3 = cube[0][0][0],cube[0][0][1],cube[0][0][2]
                    cube[0][0][0],cube[0][0][1],cube[0][0][2] = cube[1][0][0],cube[1][0][1],cube[1][0][2]
                    cube[1][0][0],cube[1][0][1],cube[1][0][2] = cube[5][0][0],cube[5][0][1],cube[5][0][2]
                    cube[5][0][0],cube[5][0][1],cube[5][0][2] = cube[2][0][0],cube[2][0][1],cube[2][0][2]
                    cube[2][0][0],cube[2][0][1],cube[2][0][2] = temp1,temp2,temp3
                    cube[4] = list(map(list,zip(*cube[4])))[::-1]

            elif a == 'D':
                if b == '+':
                    temp1,temp2,temp3 = cube[0][2][0],cube[0][2][1],cube[0][2][2]
                    cube[0][2][0],cube[0][2][1],cube[0][2][2] = cube[2][2][0],cube[2][2][1],cube[2][2][2]
                    cube[2][2][0],cube[2][2][1],cube[2][2][2] = cube[5][2][0],cube[5][2][1],cube[5][2][2]
                    cube[5][2][0],cube[5][2][1],cube[5][2][2] = cube[1][2][0],cube[1][2][1],cube[1][2][2]
                    cube[1][2][0],cube[1][2][1],cube[1][2][2] = temp1,temp2,temp3
                    cube[3] = list(map(list,zip(*cube[3][::-1])))
                elif b == '-':
                    temp1,temp2,temp3 = cube[0][2][0],cube[0][2][1],cube[0][2][2]
                    cube[0][2][0],cube[0][2][1],cube[0][2][2] = cube[1][2][0],cube[1][2][1],cube[1][2][2]
                    cube[1][2][0],cube[1][2][1],cube[1][2][2] = cube[5][2][0],cube[5][2][1],cube[5][2][2]
                    cube[5][2][0],cube[5][2][1],cube[5][2][2] = cube[2][2][0],cube[2][2][1],cube[2][2][2]
                    cube[2][2][0],cube[2][2][1],cube[2][2][2] = temp1,temp2,temp3
                    cube[3] = list(map(list,zip(*cube[3])))[::-1]
            
            elif a == 'F':
                if b == '+':
                    temp1,temp2,temp3 = cube[2][0][0],cube[2][1][0],cube[2][2][0]
                    cube[2][0][0],cube[2][1][0],cube[2][2][0] = cube[4][2][0],cube[4][2][1],cube[4][2][2]
                    cube[4][2][0],cube[4][2][1],cube[4][2][2] = cube[1][2][2],cube[1][1][2],cube[1][0][2]
                    cube[1][2][2],cube[1][1][2],cube[1][0][2] = cube[3][0][2],cube[1][0][1],cube[3][0][0]
                    cube[3][0][2],cube[1][0][1],cube[3][0][0] = temp1,temp2,temp3
                    cube[0] = list(map(list,zip(*cube[0][::-1])))

                elif b == '-':
                    temp1,temp2,temp3 = cube[2][0][0],cube[2][1][0],cube[2][2][0]
                    cube[2][0][0],cube[2][1][0],cube[2][2][0] = cube[3][0][2],cube[3][0][1],cube[3][0][0]
                    cube[3][0][0],cube[3][0][1],cube[3][0][2] = cube[1][0][2],cube[1][1][2],cube[1][2][2]
                    cube[1][0][2],cube[1][1][2],cube[1][2][2] = cube[4][2][2],cube[4][2][1],cube[4][2][0]
                    cube[4][2][0],cube[4][2][1],cube[4][2][2] = temp1,temp2,temp3 
                    cube[0] = list(map(list,zip(*cube[0])))[::-1]
            
            elif a == 'B':
                if b == '+':
                    temp1,temp2,temp3 = cube[2][0][2],cube[2][1][2],cube[2][2][2]
                    cube[2][0][2],cube[2][1][2],cube[2][2][2] = cube[3][0][2],cube[3][1][2],cube[3][2][2]

                    cube[2][0][0],cube[2][1][0],cube[2][2][0] = cube[4][2][0],cube[4][2][1],cube[4][2][2]
                    cube[4][2][0],cube[4][2][1],cube[4][2][2] = cube[1][2][2],cube[1][1][2],cube[1][0][2]
                    cube[1][2][2],cube[1][1][2],cube[1][0][2] = cube[3][0][2],cube[1][0][1],cube[3][0][0]
                    cube[3][0][2],cube[1][0][1],cube[3][0][0] = temp1,temp2,temp3
                    cube[0] = list(map(list,zip(*cube[5][::-1])))

                elif b == '-':
                    temp1,temp2,temp3 = cube[2][0][0],cube[2][1][0],cube[2][2][0]
                    cube[2][0][0],cube[2][1][0],cube[2][2][0] = cube[3][0][2],cube[3][0][1],cube[3][0][0]
                    cube[3][0][0],cube[3][0][1],cube[3][0][2] = cube[1][0][2],cube[1][1][2],cube[1][2][2]
                    cube[1][0][2],cube[1][1][2],cube[1][2][2] = cube[4][2][2],cube[4][2][1],cube[4][2][0]
                    cube[4][2][0],cube[4][2][1],cube[4][2][2] = temp1,temp2,temp3 
                    cube[0] = list(map(list,zip(*cube[5])))[::-1]
            
            # elif a == 'L':
            
            # elif a == 'R':

        print(cube)