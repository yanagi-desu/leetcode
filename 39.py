from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def recursion(candidates, target, j,trace):
            if target == 0:
                ans.append(trace)
            for i in range(j,len(candidates)):
                if target-candidates[i]>=0:
                    recursion(candidates,target-candidates[i], i, trace+[candidates[i]])
                else:
                    continue
        recursion(candidates,target,0,[])
        return ans

solve = Solution()
ans = solve.combinationSum([2,3,6,7],7)
print(ans)