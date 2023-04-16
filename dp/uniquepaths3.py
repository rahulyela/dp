class Solution:
    def uniquePathsIII(self, grid) -> int:
        count=0
        start=[]
        end=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==0):
                    count+=1
                elif(grid[i][j]==1):
                    count+=1
                    start=[i,j]
                elif(grid[i][j]==2):
                    end=[i,j]
        def path(i,j,grid,count,dp,end):
            if(i<0 or i>=len(grid) or j<0 or j>=len(grid[0])):
                return 0
            if(grid[i][j]==-1):
                return 0
            if(count==0 and i==end[0] and j==end[1]):
                return 1
            if(count==0 or (i==end[0] and j==end[1])):
                return 0
            if(dp[i][j]!=-1):
                return 0
            dp[i][j]=0
            count-=1
            left=path(i,j-1,grid,count,dp,end)
            right=path(i,j+1,grid,count,dp,end)
            down=path(i+1,j,grid,count,dp,end)
            up=path(i-1,j,grid,count,dp,end)
            dp[i][j]=-1
            return left+right+down+up
        dp=[[-1]*len(grid[0]) for x in range(len(grid))]
        return path(start[0],start[1],grid,count,dp,end)
            