arr=[3,3,5,0,0,3,1,4]
k=3
dp=[[[0]*(k+1) for x in range(2)] for x in range(len(arr)+1)]
# return(sell(0,1,arr,2,dp))
for i in range(len(arr)-1,-1,-1):
    for buy in range(2):
        for cap in range(1,k+1):
            if(buy):
                profit=max(-arr[i]+dp[i+1][0][cap],dp[i+1][1][cap])
                dp[i][buy][cap]=profit
            else:
                profit=max(arr[i]+dp[i+1][1][cap-1],dp[i+1][0][cap])
                dp[i][buy][cap]=profit
print(dp[0][1][k])
#tabulation