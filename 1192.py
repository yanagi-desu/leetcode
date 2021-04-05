
from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        visited = [False for _ in range(n)]
        ranks = [i for i in range(n)]
        graph = [[] for i in range(n)]
        for each in connections:
            graph[each[0]].append(each[1])
            graph[each[1]].append(each[0])
        res = []
        def dfs(n, connections, visited, ranks, rank, preVertex, curVertex):
            visited[curVertex] = True
            ranks[curVertex] = rank

            for each in graph[curVertex]:
                if each == preVertex:
                    continue
                if not visited[each]:
                    dfs(res, connections, visited, ranks, rank+1,curVertex,each)
                ranks[curVertex] = min(ranks[curVertex], ranks[each])
                if ranks[each]>=rank+1:
                    res.append([curVertex,each])
        dfs(n, connections,visited,ranks,0,-1,0)
        return res
        
          
solve = Solution()
print(solve.criticalConnections(4,[[0,1],[1,2],[2,0],[1,3]]))
