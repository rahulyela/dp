class Solution:
    def shortestXYDist(self, grid, N, M):
        dist = [[float('inf')] * M for _ in range(N)]
        for y in range(N):
            for x in range(M):
                if grid[y][x] == 'X':
                    dist[y][x] = 0
                else:
                    if y > 0:
                        dist[y][x] = min(dist[y][x], dist[y - 1][x] + 1)
                    if x > 0:
                        dist[y][x] = min(dist[y][x], dist[y][x - 1] + 1)
        for y in range(N - 1, -1, -1):
            for x in range(M - 1, -1, -1):
                if grid[y][x] == 'X':
                    dist[y][x] = 0
                else:
                    if y < N - 1:
                        dist[y][x] = min(dist[y][x], dist[y + 1][x] + 1)
                    if x < M - 1:
                        dist[y][x] = min(dist[y][x], dist[y][x + 1] + 1)
        ans = 1e9
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 'Y':
                    ans = min(ans, dist[i][j])      
        return ans           

#matrix 0-1 replace 1 with nearest zero
class Solution:
    def updateMatrix(self, mat):
        n=len(mat)
        m=len(mat[0])
        dist=[[float('inf')]*m for _ in range(n)]
        # print(m,n)
        for i in range(n):
            for j in range(m):
                if(mat[i][j]!=0):
                    if(i-1>=0):
                        dist[i][j]=min(dist[i][j],dist[i-1][j]+1)
                    if(j>0):
                         dist[i][j]=min(dist[i][j],dist[i][j-1]+1)
                else:
                    dist[i][j]=0
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if(mat[i][j]!=0):
                    if(i+1<n):
                        dist[i][j]=min(dist[i][j],dist[i+1][j]+1)
                    if(j+1<m):
                         dist[i][j]=min(dist[i][j],dist[i][j+1]+1)
                else:
                    dist[i][j]=0
        return dist
#Given an n x n grid containing only values 0 and 1,
#  where 0 represents water and 1 represents land, 
# find a water cell such that its distance to the nearest land cell is maximized, and return the distance. 
# If no land or water exists in the grid, return -1.              

class Solution:
    def maxDistance(self, grid) -> int:
        n=len(grid)
        dp=[[float('inf')]*n for _ in range(n)]
        maxi=0
        for i in range(n):
            for j in range(n):
                if(grid[i][j]==1):
                    dp[i][j]=0
                else:
                    if(i-1>=0):
                        dp[i][j]=min(dp[i][j],1+dp[i-1][j])
                    if(j-1>=0):
                        dp[i][j]=min(dp[i][j],1+dp[i][j-1])
        maxi=0
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if(grid[i][j]==1):
                    dp[i][j]=0
                else:
                    if(i+1<n):
                        dp[i][j]=min(dp[i][j],1+dp[i+1][j])
                    if(j+1<n):
                        dp[i][j]=min(dp[i][j],1+dp[i][j+1])
                if(dp[i][j]!=float('inf')):
                    maxi=max(maxi,dp[i][j])
        if(maxi==0):
            return -1
        return maxi
        
            
            
        
        