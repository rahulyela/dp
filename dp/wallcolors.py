def color(n,k,index,costs,took):
        if(index==n):
            return 0
        m=float('inf')
        for i in range(k):
            if(i!=took):
                c=costs[index][i]+color(n,k,index+1,costs,i)
                m=min(m,c)
        return m
costs=[[1,5,7],[5, 8, 4],[3,7, 9],[1,2,4]]
print(color(4,3,0,costs,-1))
dp=[[0]*(len(costs[0])) for x in range(len(costs)+1)]
n=len(costs)
k=len(costs[0])
for i in range(1,n+1):
    for j in range(k):
        m=float('inf')
        for l in range(k):
            if(l!=j):
                m=min(m,costs[i-1][j]+dp[i-1][l])
        dp[i][j]=m
print( min(dp[-1]))
                