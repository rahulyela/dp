class Solution:
    def minimumTotal(self, triangle) -> int:
        n=len(triangle)
        dp=[triangle[0][0]]
        for i in range(1,n):
            curr=[0]*(i+1)
            for j in range(i+1):
                d1=float('inf')
                d2=float('inf')
                if(i-1>=0 and j<=i-1):
                    d1=triangle[i][j]+dp[j]
                if(i-1>=0 and j-1>=0):
                    d2=triangle[i][j]+dp[j-1]
                curr[j]=min(d1,d2)
            dp=curr
        # print(dp)
        return(min(dp))
        