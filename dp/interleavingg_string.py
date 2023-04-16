class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        i=0
        j=0
        k=0
        def s(i,j,k,dp):
            if(k==len(s3)):
                if(i>=len(s1) and j>=len(s2)):
                    return True
                else:
                    return False
            if(dp[i][j]!=-1):
                return dp[i][j]
            x,y=False,False
            if(i<len(s1) and s1[i]==s3[k]):
                 x=s(i+1,j,k+1,dp)
            if(j<len(s2) and s2[j]==s3[k]):
                y=s(i,j+1,k+1,dp)
            dp[i][j]=x or y
            return x or y
        dp=[[-1]*(len(s2)+1) for x in range(len(s1)+1)]
        return s(0,0,0,dp)