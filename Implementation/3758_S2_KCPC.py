
import heapq

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n,k,t,m = map(int,input().split())
        info = []
        for i in range(m):
            info.append(list(map(int,input().split())))

        team = []
        team.append(dict())

        for team_num in range(1,n+1):
            team.append(dict())
            team[team_num]["cnt"] = 0
            team[team_num]["last"] = 0
            for problem_num in range(k):
                team[team_num][problem_num] = 0


        for i in range(m):
            team_id, probelm_id, score = info[i]
            team[team_id]["cnt"]+=1
            team[team_id]["last"] = i

            if team[team_id][probelm_id-1] < score:
                team[team_id][probelm_id-1] = score
        
        result = []
        for i in range(n):
            cum = 0
            for j in range(k):
                cum += team[i+1][j]
            
            heapq.heappush(result,[-cum,team[i+1]["cnt"],team[i+1]["last"],i+1])


        #result.sort(key = lambda x : (-x[0],x[1],x[2]))

        for i in range(n):
            a = heapq.heappop(result)
            if a[3] == t:
                print(i+1)
                break

