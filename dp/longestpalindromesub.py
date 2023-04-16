def lps(i,j,s):
    if(i>j):
        return 0
    if(i==j):
        return 1
    if(dp[i][j]!=-1):
        return dp[i][j]
    if(s[i]==s[j]):
        dp[i][j]=2+lps(i+1,j-1,s)
        return dp[i][j]
    dp[i][j]=max(lps(i+1,j-1,s),lps(i,j-1,s))
    return max(lps(i+1,j-1,s),lps(i,j-1,s))
s="BBABCBCAB"
dp=[[-1]*(len(s)) for x in range(len(s))]
print(lps(0,len(s)-1,s))
#intution if arr[i]anda[j] are equal we include else we return max(i+1,j),(i,j-1)