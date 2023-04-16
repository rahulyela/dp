class Solution:
    def maxProfit(self, arr) -> int:
        def sell(i,buy,arr,dp):
            if(i>=len(arr)):
                return 0
            if(dp[i][buy]!=-1):
                return dp[i][buy]
            if(buy):
                profit=max(-arr[i]+sell(i+1,0,arr,dp),sell(i+1,1,arr,dp))
            else:
                profit=max(arr[i]+sell(i+1,1,arr,dp),sell(i+1,0,arr,dp))
            dp[i][buy]=profit
            return profit
        dp=[[-1]*2 for x in range(len(arr))]
        return(sell(0,1,arr,dp))
#cooldown
#instead of i+1 while selling we inceasre 1=> i+2 in line 11