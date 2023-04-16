class Solution:
    def closedIsland(self, grid) -> int:
        m=len(grid[0])
        n=len(grid)
        ans=[]
        dp=[[False]*m for _ in range(n)]
        def bfs(i,j,grid):
            if(i<0 or i>=n or j<0 or j>=m):
                return False
            if(grid[i][j]==1 or dp[i][j]):
                return True
            dp[i][j]=True
            left=bfs(i-1,j,grid)
            right=bfs(i+1,j,grid)
            down=bfs(i,j+1,grid)
            up=bfs(i,j-1,grid)
            if(left and right and up and down):
                return True
            else:
                return False
        ans=0
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==0 and dp[i][j]==False and  bfs(i,j,grid)):
                    ans+=1
        return ans
#----------similar question but to find no 1s cannot be walk through(no fo enclaves)
class Solution:
    def numEnclaves(self, grid) -> int:
        m=len(grid[0])
        n=len(grid)
        ans=[0]
        sol=0
        def dfs(i,j,grid):
            if(i<0 or j<0 or j>=m or i>=n):
                return True
            if(grid[i][j]==0):
                return False
            grid[i][j]=0
            ans[0]+=1
            left=dfs(i,j-1,grid)
            right=dfs(i,j+1,grid)
            down=dfs(i+1,j,grid)
            up=dfs(i-1,j,grid)
            return left or right or down or up
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==1):
                    if(dfs(i,j,grid)==False):
                        sol+=ans[0]
                    ans[0]=0
                        
        return sol
#---optimized
class Solution:
    def numEnclaves(self, grid) -> int:
        m=len(grid[0])
        n=len(grid)
        sol=0
        def dfs(i,j,grid):
            if(i<0 or j<0 or j>=m or i>=n):
                return 
            if(grid[i][j]==0):
                return 
            grid[i][j]=0
            left=dfs(i,j-1,grid)
            right=dfs(i,j+1,grid)
            down=dfs(i+1,j,grid)
            up=dfs(i-1,j,grid)
            return 
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==1 and (i==0 or j==0 or j==m-1 or i==n-1)):
                    dfs(i,j,grid)
        for i in grid:
            sol+=sum(i)
        return sol
            
            
            
        