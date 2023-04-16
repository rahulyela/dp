text1="brute"
text2='grte'
dp=[[0]*(len(text2)+1) for x in range(len(text1)+1)]
l1=len(text1)
l2=len(text2)
for i in range(1,l1+1):
    for j in range(1,l2+1):
        if(text1[i-1]==text2[j-1]):
            dp[i][j]=1+dp[i-1][j-1]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(l1+l2-dp[-1][-1])#length of supersequnece
#print supersequnce
print(dp)
i=l1
j=l2
ans=''
while(i>0 and j>0):
    if(text1[i-1]==text2[j-1]):
        ans+=text1[i-1]
        i-=1
        j-=1
    elif(dp[i-1][j]>dp[i][j-1]):
        ans+=text1[i-1]
        i-=1
    else:
        ans+=text2[j-1]
        j-=1
    print(i,j)
print(ans[::-1])
while(i>0):
    ans+=text1[i-1]
    i-=1
while(j>0):
    ans+=text2[j-1]
    j-=1
print(ans[::-1])