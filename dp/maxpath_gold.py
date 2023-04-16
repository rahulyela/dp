class Solution:
    def getMaximumGold(self, grid) -> int:
        def gold(i,j,grid,dp,dp2):
            if(i<0 or j<0 or i>=len(grid) or j>=len(grid[0])):
                return 0
            if(grid[i][j]==0):
                return 0
            if(dp[i][j]!=-1):
                return 0
            dp[i][j]=1
            up=grid[i][j]+gold(i-1,j,grid,dp,dp2)
            down=grid[i][j]+gold(i+1,j,grid,dp,dp2)
            left=grid[i][j]+gold(i,j+1,grid,dp,dp2)
            right=grid[i][j]+gold(i,j-1,grid,dp,dp2)
            dp[i][j]=-1
            return max(left,right,up,down)
        m=float('-inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]!=0):
                    dp=[[-1]*len(grid[0]) for x in range(len(grid))]
                    x=gold(i,j,grid,dp)
                    # print(x)
                    m=max(m,x)
        return m if m!=float('-inf') else 0