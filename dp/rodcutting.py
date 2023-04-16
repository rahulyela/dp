def cut(i,target,costs,dp):
    if(i>target):
        return 0
    if(target==0):
        return 0
    if(dp[i][target]!=-1):
        return dp[i][target]
    take=float('-inf')
    if(i<=target):
        take=costs[i-1]+cut(i,target-(i),costs,dp)
    ntake=cut(i+1,target,costs,dp)
    dp[i][target]=max(ntake,take)
    return max(ntake,take)
costs=[5,6,1,8,9]
target=5
dp=[[0]*(target+1) for x in range(target+2)]
print(cut(1,target,costs,dp))
#---------------tabulation with space optimization----------------------
prev=[0]*(target+1)
for i in range(1,target+2):
    for j in range(target+1):
        t,nt=float('-inf'),float('-inf')
        if(j-i>=0):
            t=costs[i-1]+prev[j-i]
        nt=prev[j]
        prev[j]=max(nt,t)
print(prev[target])