l=list(map(int,input().split()))
dp=[0]*(len(l)+1)
dp[1]=l[0]
m=0
for i in range(1,len(l)):
    dp[i+1]=max(l[i]+m,dp[i])
    if(dp[i]>=m):
        m=dp[i]
    print(dp,m)
print(dp[-1])