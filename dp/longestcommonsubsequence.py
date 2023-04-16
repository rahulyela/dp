# def sub(i,j,s1,s2,dp):
        #     if(i>=len(s1) or j>=len(s2)):
        #         return 0
        #     if(dp[i][j]!=-1):
        #         return dp[i][j]
        #     if(s1[i]==s2[j]):
        #         dp[i][j]=1+sub(i+1,j+1,s1,s2,dp)
        #         return dp[i][j]
        #     else:
        #         dp[i][j]=max(sub(i+1,j,s1,s2,dp),sub(i,j+1,s1,s2,dp))
        #     return dp[i][j]
#---------------------------tabulation----------------------------#
text1="eabcb"
text2='bcbae'
dp=[[0]*(len(text2)+1) for x in range(len(text1)+1)]
l1=len(text1)
l2=len(text2)
for i in range(1,l1+1):
    for j in range(1,l2+1):
        if(text1[i-1]==text2[j-1]):
            dp[i][j]=1+dp[i-1][j-1]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
# print(dp[-1][-1])
#-----------longest common substring----------------------
sol=''
temp=''
res=float('-inf')
for i in range(1,l1+1):
    for j in range(1,l2+1):
        if(text1[i-1]==text2[j-1]):
            dp[i][j]=1+dp[i-1][j-1]
            res=max(res,dp[i][j])
            print(temp)
        else:
            dp[i][j]=0 #minor change
# print(res)
#-----------------------print common subsequnce------------
i,j=l1-1,l2-1
print(dp)
sol=''
temp=''
while(i>=0 and j>=0):
    print(i,j)
    if(text1[i]==text2[j]):
        temp+=text1[i]
        print('1')
        i-=1
        j-=1
    else:
        if(dp[i][j-1]>dp[i-1][j]):
            j-=1
        else:
            i-=1
        temp=''
    if(len(sol)<len(temp)):
            sol=temp
            print(temp)
print(sol,12)
