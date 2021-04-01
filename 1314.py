class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        dir = [0,-1,0,1,0,0]
        def flip(x,y,s):
            for i in range(5):
                tx = x+dir[i]
                ty = y+dir[i+1]
                if tx>=m or ty>=n or tx<0 or ty<0:
                    continue
                else:
                    s ^= 1<<ty*n+tx 
                return s

        #fill in the first round of queue
        queue = []
        steps = 0
        seen = []*(1<<n*m)
        start = 0
        for i in range(m):
            for j in range(n):
                start.append(mat[i][j]<<(j*n+i))
        if start == 0: return 0
        queue.append(start)
        seen[start] = 1
        print(seen)
        

        while queue:
            size = len(queue)
            while size:
                s = queue.peek()
                if s==0: return steps
                s.pop()
                for i in range(m):
                    for j in range(n):
                        t = flip(s,i,j)
                        if seen[t]: continue
                        seen[t] = 1
                        queue.append(t)
                
                steps+=1
            return -1