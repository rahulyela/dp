class Solution:
    def maximalSquare(self, matrix) -> int:
        n=len(matrix)
        m=len(matrix[0])
        dp=[[0]*m for _ in range(n)]
        ans=0
        for i in range(m):
            dp[0][i]=int(matrix[0][i])
            ans=max(ans,dp[0][i]**2)
        for i in range(n):
            dp[i][0]=int(matrix[i][0])
            ans=max(ans,dp[i][0]**2)
        for i in range(1,n):
            for j in range(1,m):
                if(matrix[i][j]=="0"):
                    dp[i][j]=0
                else:
                    dp[i][j]=1+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
                ans=max(ans,dp[i][j]**2)
        return ans
#intutuion simiar to count all submartices squre with all ones for each time we maintain max
#such that if its x then max area that can be form by using this is x*x
                    
        
                    
                        
        