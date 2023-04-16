class Solution:
    def goodStones(self, n, arr) -> int:
        #code here
        dp=[-1]*len(arr)
        i=0
        def good(i,dp,arr):
            if(i<0 or i>n-1):
                return 1
            if(dp[i]!=-1):
                return dp[i]
            dp[i]=0
            dp[i]=good(i+arr[i],dp,arr)
            return dp[i]
        for i in range(len(dp)):
            if(dp[i]==-1):
                dp[i]=good(i,dp,arr)
        return dp.count(1)