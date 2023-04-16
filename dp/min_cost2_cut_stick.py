class Solution:
    def minCost(self, n: int, cuts) -> int:
        cuts.sort()
        cuts.append(n)
        cuts.insert(0,0)
        def cut(i,j,dp):
            if(i>j):
                return 0
            if(dp[i][j]!=-1):
                return dp[i][j]
            mini=float('inf')
            for ind in range(i,j+1):
                cost=cuts[j+1]-cuts[i-1]+cut(i,ind-1,dp)+cut(ind+1,j,dp)
                mini=min(mini,cost)
            dp[i][j]=mini
            return mini
        dp=[[-1]*(len(cuts)) for _ in range(len(cuts))]
        return cut(1,len(cuts)-2,dp)
#--------------partiton dp-----------------------------
#------------------we cut from i to j and add len before cutting to cost and return min of all the cuts------------
#------------------time complexity m*m*m m is len(cuts)-2 as we added to extra elements
