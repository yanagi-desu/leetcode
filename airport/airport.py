class solution:
    def solve(self):
        i = input()
        aircount = int(i[0])
        flightCount = int(i[1])
        flights = []
        airport = []
        for i in range(flightCount):
            flights.append(input())
            print(flights)

        connected = [0]*flightCount
        for i in flights:
            connected[i[0]]+=1
            connected[i[1]]+=1
            if connected[i[0]]>aircount or connected[i[1]]>aircount:
                return False
        
        for each in connected:
            if connected!=aircount:
                return False
        
        def dfs(flights,at,visited):
            visited[at] == True
            for edge in flights:
                if at in edge:
                    i = 0 if edge[1] == at else 1
                    if visited[edge[i]]:
                        dfs(flights,edge[i],visited)





    
s = solution()
s.solve()
