from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [set() for i in range(numCourses)]
        outdegree = [[] for i in range(numCourses)]
        for rel in prerequisites:
            indegree[rel[0]].add(rel[1])
            outdegree[rel[1]].append(rel[0])
        ret, start = [], [i for i in range(numCourses) if not indegree[i]]
        while start:
            newStart = []
            for each in start:
                ret.append(each)
                for j in outdegree[each]:
                    indegree[j].remove(each)
                    if not indegree[j]:
                        newStart.append(j)
            start = newStart 
                
        return ret if len(ret) == numCourses else []

solve = Solution()
print(solve.findOrder(4,[[0,1],[2,0],[3,1],[3,2]]))