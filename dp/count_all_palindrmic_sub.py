def count(i,j,arr,dp):
    if(i>j):
        return 0
    if(i==j):
        dp[i][j]=1
        return 1
    if(dp[i][j]!=-1):
        return dp[i][j]
    if(arr[i]==arr[j]):
        dp[i][j]=1+count(i+1,j,arr,dp)+count(i,j-1,arr,dp)
        return dp[i][j]
    dp[i][j]=count(i+1,j,arr,dp)+count(i,j-1,arr,dp)-count(i+1,j-1,arr,dp)
    return dp[i][j]
arr='abcb'
dp=[[-1]*(len(arr)) for x in range(len(arr))]
print(count(0,len(arr)-1,arr,dp))