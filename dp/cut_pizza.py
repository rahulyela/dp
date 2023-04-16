class Solution:
    def ways(self, pizza, k: int) -> int:
        n=len(pizza)
        m=len(pizza[0])
        presum=[[0]*(m+1) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                presum[i][j]=presum[i+1][j]+presum[i][j+1]-presum[i+1][j+1]+(pizza[i][j]=='A')
        def f(i,j,k,dp):
            if(k==0):
                if(presum[i][j]>0):
                    return 1
                else:
                    return 0
            if(dp[i][j][k]!=-1):
                return dp[i][j][k]
            ans=0
            for t in range(i+1,n):
                if(presum[i][j]-presum[t][j]>0):
                    ans+=f(t,j,k-1,dp)
            for t in range(j+1,m):
                if(presum[i][j]-presum[i][t]>0):
                    ans+=f(i,t,k-1,dp)
            dp[i][j][k]=ans
            return ans
        dp=[[[-1]*(k) for _ in range(m)]for _ in range(n)]
        return f(0,0,k-1,dp)%(10**9+7)
                    
#--------------   new pattern of prefixsum and dp -----------------------
# --------------------we find whther we can cut or not using additional 2dp-----------------
# time complexity n*m*k*(m+n)-----------------------------------------------   