arr=[5,16,11 ,9 ,15, 12, 6, 9, 6, 10]
dp=[[1]*(2) for x in range(len(arr))]
ans=1
for i in range(1,len(arr)):
    for j in range(i):
        if(arr[i]>arr[j]):
            dp[i][0]=max(dp[i][0],dp[j][1]+1)
            ans=max(dp[i][0],ans)
        elif(arr[j]>arr[i]):
            dp[i][1]=max(dp[i][1],dp[j][0]+1)
            ans=max(ans,dp[i][1])
print(ans)
#--------------------tc(n*n)---------------------------------------
ans1=1
ans2=1
for i in range(1,len(arr)):
    if(arr[i]>arr[i-1]):
        ans1=ans2+1
    elif(arr[i-1]>arr[i]):
        ans2=ans1+1
print(max(ans1,ans2))
#we are swapping the alternates like twisting each and finfing ans
#------------------------tc(n)------------------------------