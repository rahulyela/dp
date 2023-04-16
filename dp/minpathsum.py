class Solution:
    def minFallingPathSum(self, matrix) -> int:
        dp=matrix[0]
        for i in range(1,len(matrix)):
            curr=[-1]*len(matrix[0])
            for j in range(len(matrix[0])):
                d_right,d_left=float('inf'),float('inf')
                if(j+1<len(matrix[0])):
                    d_left=matrix[i][j]+dp[j+1]
                if(j-1>=0):
                    d_right=matrix[i][j]+dp[j-1]
                down=matrix[i][j]+dp[j]
                curr[j]=min(d_left,d_right,down)
            dp=curr
        return min(dp)