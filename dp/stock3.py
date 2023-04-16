class Solution:
    def maxProfit(self, arr) -> int:
        def sell(i,buy,arr,cap,dp):
            if(i>=len(arr) or cap==0):
                return 0
            if(dp[i][buy][cap]!=-1):
                return dp[i][buy][cap]
            if(buy):
                profit=max(-arr[i]+sell(i+1,0,arr,cap,dp),sell(i+1,1,arr,cap,dp))
            else:
                profit=max(arr[i]+sell(i+1,1,arr,cap-1,dp),sell(i+1,0,arr,cap,dp))
            dp[i][buy][cap]=profit
            return profit
        dp=[[[-1]*3 for x in range(2)] for x in range(len(arr))]
        return(sell(0,1,arr,2,dp))
#atmost 2 transcations extension of stocks 2