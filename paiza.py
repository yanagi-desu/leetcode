input_line = input()
H,W = input_line.split(" ")
choco = []
sum_ = 0
for i in range(int(H)):
    line = []
    input_line = input()
    input_line = input_line.split(" ")
    for e in input_line:
        line.append(int(e))
        sum_ += int(e)
    choco.append(line)

past = {}
accum_choco = [[0 for i in range(int(W))]  for j in range(int(H))]
for row in range(int(H)):
    for element in range(int(W)):
        accum_choco[row][element] = choco[row][element] if element-1<0 else choco[row][element]+accum_choco[row][element-1] 
    
ans = []
cur_ac = 0

def dfs(accumed,level,maxL,width,goal,cur_ac,track,ans):
    
    if level>=maxL:
        return
    for each in range(width):
        if cur_ac+accumed[level][each]>goal:
            continue
        # print((track,cur_ac,goal,cur_ac+accumed[level][each]),ans)
        if cur_ac+accumed[level][each] == goal and level!=maxL-1:
            continue
        
        if cur_ac+accumed[level][each] == goal:
            # print("got")
            track.append([level,each])
            return ans.append(track)
        
        dfs(accumed,level+1,maxL,width,goal,cur_ac+accumed[level][each],track+[[level,each]],ans)
        
    
dfs(accum_choco,0,int(H),int(W),int(sum_/2),0,[],ans)
print(ans)
if not ans:
    print("No")
else:
    schema = ans[0]
    ret = [["B" for i in range(int(W))]for j in range(int(H))]
    for i in range(len(schema)):
        for j in range(schema[i][1]+1):
            ret[i][j] = "A"
    print(ret)