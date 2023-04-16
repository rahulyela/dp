class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def bfs(m,n,i,j,dp):
            if(i==m and j==n):
                return 1
            if(i>m or j>n):
                return 0
            if(dp[i][j]!=-1):
                return dp[i][j]
            down=bfs(m,n,i+1,j,dp)
            right=bfs(m,n,i,j+1,dp)
            dp[i][j]=down+right
            return dp[i][j]
        dp = [[-1] * n for x in range(m)]
        x=bfs(m-1,n-1,0,0,dp)
        # print(dp)
        return x
