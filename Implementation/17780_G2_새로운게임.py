
def check():
    return



if __name__ == "__main__":

    n,k = map(int,input().split())
    board = []
    for _ in range(n):
        line = list(map(int,input().split()))
        board.append(line)

    players = []
    for i in range(k):
        players.append([])
        line = list(map(int,input().split()))
        players[i].append(line)

    print(players)

    dx = [1,-1,0,0]
    dy = [0,0,-1,1]


    # for turn in range(1000):
    #     for i in range(len(players)):
    #         y,x,d = players[i][0]-1,players[i][1]-1,players[i][2]-1
    #         ky,kx = y+dy[d], x+dx[d]

    #         if board[ky][kx] == 0: # 흰색이면 원래 있던 말위에 올라타고 해당 칸으로 이동
    #             for j in range(len(players)):
    #                 if players[j][]
                

            
    #         elif board[ky][kx] == 1:

    #         elif board[ky][kx] == 2:




        