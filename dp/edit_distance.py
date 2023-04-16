def edit(i,j,s1,s2,dp):
    if(i<0):
        return j+1
    if(j<0):
        return i+1
    if(dp[i][j]!=-1):
        return dp[i][j]
    if(s1[i]==s2[j]):
        return edit(i-1,j-1,s1,s2,dp)
    else:
        de=1+edit(i-1,j,s1,s2,dp)
        ins=1+edit(i,j-1,s1,s2,dp)
        rep=1+edit(i-1,j-1,s1,s2,dp)
        dp[i][j]=min(de,ins,rep)
        return min(de,ins,rep)
s1='intention'
s2='execution'
dp=[[-1]*(len(s2)+1) for x in range(len(s1)+1)]
print(edit(len(s1)-1,len(s2)-1,s1,s2,dp))