arr=list(map(int,input().split()))
target=int(input())
n=len(arr)
dp=[[0]*(target+1) for x in range(len(arr))]
for i in range(len(dp)):
    dp[i][0]=1
dp[0][arr[0]]=1
for i in range(1,len(arr)):
    for t in range(1,target+1):
        s,l=0,0
        l=dp[i-1][t]
        if(t-arr[i]>=0):
            s=dp[i-1][t-arr[i]]
        dp[i][t]=s+l
print(dp[n-1][target])
        