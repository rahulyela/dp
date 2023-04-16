n=1
arr=[[-10]]
dp=[[-1]*n for i in range(n)]
dp[0][0]=arr[0][0]
for i in range(1,n):
    for j in range(i+1):
        d1=float('inf')
        d2=float('inf')
        if(i-1>=0 and j<=i-1):
            d1=arr[i][j]+dp[i-1][j]
        if(i-1>=0 and j-1>=0):
            d2=arr[i][j]+dp[i-1][j-1]
        dp[i][j]=min(d1,d2)
print(min(dp[n-1]))
print(dp)