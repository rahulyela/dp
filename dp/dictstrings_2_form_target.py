from collections import defaultdict
# target should be formed from left to right.
# To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in 
# words if target[i] = words[j][k].
# Once you use the kth character of the jth string of words, you can no longer use the xth character of
#  any string in words where x <= k. In other words, all characters to the left of or at index k become 
# unusuable for every string.
# Repeat the process until you form the string target.
class Solution:
    def numWays(self, words, target: str) -> int:
        n=len(words)
        m=len(words[0])
        hashi = [defaultdict(int) for _ in range(len(words[0]))]
        for word in words:
            for i, letter in enumerate(word):
                hashi[i][letter] += 1
        def ways(i,j,dp):
            if(j==len(target)):
                return 1
            if(i==m):
                return 0
            if(dp[i][j]!=-1):
                return dp[i][j]
            ntake=ways(i+1,j,dp)
            take=hashi[i][target[j]]*ways(i+1,j+1,dp)
            dp[i][j]=take+ntake
            return take+ntake
        dp=[[-1]*(len(target)) for _ in range(m)]
        return ways(0,0,dp)%(10**9+7)
#intution is that each string i values are calucted and take that rqiured chr and nottake