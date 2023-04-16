class Solution:
    def cherryPickup(self, grid) -> int:
        def cherry(i,j1,j2,c,grid,dp):
            if(j1<0 or j2<0 or j1>c or j2>c):
                return float('-inf')
            if(i==len(grid)-1):
                if(j1==j2):
                    return grid[i][j1]
                else:
                    return grid[i][j1]+grid[i][j2]
            m=float('-inf')
            if(dp[i][j1][j2]!=-1):
                return dp[i][j1][j2]
            for k in range(-1,2,1):
                for l in range(-1,2,1):
                    value=0
                    if(j1==j2):
                        value=grid[i][j1]
                    else:
                        value=grid[i][j1]+grid[i][j2]
                    value+=cherry(i+1,j1+k,j2+l,c,grid,dp)
                    m=max(m,value)
                    # print(m)
            dp[i][j1][j2]=m
            return m
        d=len(grid[0])-1
        dp=[[[-1]*(d+1) for x in range(d+1)] for x in range(len(grid))]
        return cherry(0,0,d,d,grid,dp)
                    
                
                        
                    
        