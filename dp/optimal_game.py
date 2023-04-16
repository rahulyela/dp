class Solution:
    def optimalStrategyOfGame(self,arr, n):
        # code here
        def game(i,j,arr,dp):
            if(i>j or i>=n or j<0):
                return 0
            if(dp[i][j]!=-1):
                return dp[i][j]
            take1=arr[i]+min(game(i+1,j-1,arr,dp),game(i+2,j,arr,dp))
            take2=arr[j]+min(game(i,j-2,arr,dp),game(i+1,j-1,arr,dp))
            dp[i][j]=max(take1,take2)
            return max(take1,take2)
        dp=[[-1]*(n) for x in range(n)]
        return game(0,n-1,arr,dp)