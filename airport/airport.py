class solution:
    def solve(self):
        aircount = 3
        flightCount = 3
        airport = [i for i in range(1,aircount+1)]
        flights = ["12","23","13"]
        visited = [False]*aircount
        connected = [0]*aircount
        for i in flights:
            connected[int(i[0])-1]+=1
            connected[int(i[1])-1]+=1
            if connected[int(i[0])-1]>aircount or connected[int(i[1])-1]>aircount:
                return False
        
        for each in connected:
            if each!=aircount-1:
                return False
        
        def dfs(flights,at,visited):
            for edge in flights:
                if str(at) == edge[0] and not visited[int(edge[1])-1]:
                    visited[int(edge[1])-1] = True
                    dfs(flights,edge[1],visited)

        rev = []
        for each in flights:
            temp = [each[1]+each[0]]
            rev.append(temp)

        for each in airport:
            dfs(flights,each,visited)
        for each in airport:
            if not visited[each-1]:
                return False
        # visited = [False]*aircount
        # for each in airport:
        #     dfs(rev,each,visited)
        # for each in airport:
        #     if not visited[each-1]:
        #         return False
        return True

s = solution()
print("Yes" if s.solve() else "No")
