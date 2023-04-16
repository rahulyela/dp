#thought process total length-longest pandliromic subsequnce
#min insrtion to make a string palindrome
text1="leetcode"
text2=text1[::-1]
dp=[[0]*(len(text2)+1) for x in range(len(text1)+1)]
l1=len(text1)
l2=len(text2)
for i in range(1,l1+1):
    for j in range(1,l2+1):
        if(text1[i-1]==text2[j-1]):
            dp[i][j]=1+dp[i-1][j-1]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(len(text1)-dp[-1][-1])