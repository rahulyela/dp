class Solution:
    def countSubstrings(self, s: str) -> int:
        dp=[[0]*(len(s)) for _ in range(len(s))]
        for i in range(len(dp)):
            dp[i][i]=1
        count=0
        for i in range(len(s)):
            for j in range(i+1):
                if(i==j):
                    dp[i][j]=1
                elif(s[i]==s[j]):
                    if(i-1==j):
                        dp[i][j]=1
                    else:
                        dp[i][j]= dp[i-1][j+1] 
                else:
                    dp[i][j]=0
                count+=dp[i][j]
        print(dp)
        return count
#dp solution n*n--------------------------------------------------------
def count_palindromic_substrings(s):
    n = len(s)
    count = 0
    for i in range(n):
        # count odd length palindromes with i at center
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        
        # count even length palindromes with i and i+1 at center
        l, r = i, i+1
        while l >= 0 and r < n and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
    
    return count
#--------------------------------space complexity(1)--------------------------