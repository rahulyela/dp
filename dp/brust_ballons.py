class Solution():
    def maxCoins(self, N, cuts):
        #your code goes here
        cuts.append(1)
        cuts.insert(0,1)
        print(cuts)
        def cut(i,j,dp):
            if(i>j):
                return 0
            if(dp[i][j]!=-1):
                return dp[i][j]
            maxi=float('-inf')
            for ind in range(i,j+1):
                cost=cuts[j+1]*cuts[ind]*cuts[i-1]+cut(i,ind-1,dp)+cut(ind+1,j,dp)
                maxi=max(maxi,cost)
            dp[i][j]=maxi
            return maxi
        dp=[[0]*(N+2) for x in range(N+2)]
        # return(cut(1,len(cuts)-2,dp))
#--------------------recursive instaed of brust from staring we add ballons from last to first inorder 
# to overcome dependency of subprobvelms -------------------------------
        for i in range(N,0,-1):
            for j in range(1,N+1):
                maxi=0
                for ind in range(i,j+1):
                    # print(i,j,ind)
                    cost=cuts[j+1]*cuts[ind]*cuts[i-1]+dp[i][ind-1]+dp[ind+1][j]
                    maxi=max(maxi,cost)
                dp[i][j]=maxi
        return dp[1][N]
#------------------tabulation----------------------