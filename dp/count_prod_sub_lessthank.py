def sub(i,k,arr):
    if(i==len(arr)):
        return 0
    ntake=sub(i+1,k,arr)
    take=0
    if(arr[i]<=k):
        take=1+sub(i+1,k//arr[i],arr)
    return take+ntake
arr=[1,2,3,4]
k=10
# print(sub(0,k,arr))
dp=[[0]*(k+1) for  x in range(len(arr)+1)]
for i in range(1,len(arr)+1):
    for k in range(1,k+1):
        ntake=dp[i-1][k]
        take=0
        if(arr[i-1]<=k):
            take=1+dp[i-1][k//arr[i-1]]
        dp[i][k]= take+ntake
print(dp[-1][k])
        
        
    