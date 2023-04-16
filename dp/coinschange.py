def coins(i,p,target,arr,dp):
    if(target==0):
        return 1
    if(i>=len(arr)):
        return 0
    if(dp[i][target]!=-1):
        return dp[i][target]
    t=0
    if(arr[i]<=target):
        t=coins(i,p,target-arr[i],arr,dp)
    nt=coins(i+1,p,target,arr,dp)
    dp[i][target]=t+nt
    return t+nt
arr=list(map(int,input().split()))
target=int(input())
dp=[[-1]*(target+1) for x in range(len(arr))]
print(coins(0,[],target,arr,dp))
#---------------------------------------#tabulation-------------------------------------------
class Solution:
    def change(self, amount: int, coins) -> int:
        if(len(coins)==1):
            return int(amount%coins[-1]==0)
        n=len(coins)
        prev=[0]*(amount+1)
        prev[0]=1
        for i in range(1,n+1):
            curr=[0]*(amount+1)
            curr[0]=1
            for j in range(amount+1):
                t,nt=0,0
                if(coins[i-1]<=j):
                    t=curr[j-coins[i-1]]
                nt=prev[j]
                curr[j]=t+nt
            prev=curr
        return prev[-1]
                    