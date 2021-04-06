from typing import List
import collections
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        f = collections.defaultdict(dict)
        for a,b,p in flights:
            f[a][b] = p
        heap = [(0,src,K)]
        while heap:
            p,i,k = heapq.heappop(heap)
            if i == dst:
                return p
            if k >= 0:
                for each in f[i]:
                    heapq.heappush(heap,(p+f[i][each],each,k-1))
solve = Solution()
print(solve.findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))

#3,[[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1
#5,[[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]],0,4,1
#3,[[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0
               