def distinct(i,j,s1,s2,dp):
    if(j>=len(s2)):
        return 1
    if(i>=len(s1)):
        return 0
    if(dp[i][j]!=-1):
        return dp[i][j]
    if(s1[i]==s2[j]):
        dp[i][j]=distinct(i+1,j+1,s1,s2,dp)+distinct(i+1,j,s1,s2,dp)
        return dp[i][j]
    dp[i][j]=distinct(i+1,j,s1,s2,dp)
    return dp[i][j]
s1='babgbag'
s2='bag'
dp=[[-1]*(len(s2)) for x in range(len(s1))]
print(distinct(0,0,s1,s2,dp))