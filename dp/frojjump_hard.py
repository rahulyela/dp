class Solution:
    def canCross(self, stones) -> bool:
        dict={}
        for i in range(len(stones)):
            dict[stones[i]]=i
        def jump(i,stones,k,dict,dp):
            if(i==len(stones)-1):
                ans=True
                return 1
            if(dp[i][k]!=-1):
                return dp[i][k]
            l,m,r=0,0,0
            if(k-1>=0):
                if(stones[i]+k-1 in dict):
                    l=jump(dict[stones[i]+k-1],stones,k-1,dict,dp)
            if(stones[i]+k in dict and k!=0):
                m=jump(dict[stones[i]+k],stones,k,dict,dp)
            if(stones[i]+k+1 in dict):
                l=jump(dict[stones[i]+k+1],stones,k+1,dict,dp)
            dp[i][k]=l+m+r
            return dp[i][k]
        dp=[[-1]*(len(stones)) for x in range(len(stones))]
        ans=False
        x= jump(0,stones,0,dict,dp)
        print(dp)
        return ans
                    
        