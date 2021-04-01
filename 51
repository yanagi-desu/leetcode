from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #try place one queen at each block 
        #check for availability for rest of the blocks, if available place another queen 
        #if not available skip the current run routine,
        #if all four queens places, add the current map layout to the ans list
        def recursion(queens,diff,sum_):
            p = len(queens) 
            if p == n:
                ans.append(queens)
                return None
            for i in range(n):
                if i not in queens and p-i not in diff and p+i not in sum_:
                    recursion(queens+[i],diff+[p-i],sum_+[p+i])
        ans = []           
        recursion([],[],[])
        return [["."*i+"Q"+"."*(n-1-i) for i in queen]for queen in ans ]
            
solve = Solution()
p = solve.solveNQueens(4)
print(p)