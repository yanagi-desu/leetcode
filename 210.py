from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [set() for _ in range(numCourses)]
        outdegree = [[] for _ in range(numCourses)]
        for point in prerequisites:
            indegree[p[0]].add(p[1])
            outdegree[p[1]].append(p[0])
        ret, start = [], [i for i in range(numCourses) if not indegree[i]]




solve = Solution()
print(solve.findOrder(4,[[0,1],[2,0],[3,1],[3,2]]))