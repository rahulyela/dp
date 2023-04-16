class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        if(obstacleGrid[0][0]==1 or obstacleGrid[n-1][m-1]==1):
            return 0
        dp=[-1]*m
        for i in range(n):
            curr=[-1]*m
            for j in range(m):
                if(obstacleGrid[i][j]==1):
                    curr[j]=0
                elif(i==0 and j==0):
                    curr[j]=1
                else:
                    left,up=0,0
                    if(j>0):
                        left=curr[j-1]
                    if(i>0):
                        up=dp[j]
                    curr[j]=left+up
            dp=curr
        # print(dp)
        return curr[m-1]
                    
        