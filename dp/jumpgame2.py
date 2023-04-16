nums=[2,1]
n=len(nums)
dp=[-1]*n
dp[-1]=0
for j in range(n-2,-1,-1):
    m=float('inf')
    if(j+nums[j]<len(nums)):
        for i in range(j+1,j+nums[j]+1):
            m=min(m,dp[i])
        dp[j]=m+1
    else:
        dp[j]=float('inf')
print(dp[0])

