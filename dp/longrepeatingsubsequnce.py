class Solution:
	def LongestRepeatingSubsequence(self, str):
		# Code here
		n=len(str)
		dp=[[0]*(n+1) for x in range(n+1)]
# 		print(dp)
		for i in range(1,len(str)+1):
		    for j in range(1,len(str)+1):
		        if(str[i-1]==str[j-1] and i!=j):
		            dp[i][j]=1+dp[i-1][j-1]
	# 	        else:
	# 	            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    # return dp[-1][-1]
