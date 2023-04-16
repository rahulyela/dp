class Solution:
    def lengthOfLIS(self, nums) -> int:
        def lis(i,prev,arr,dict):
            if(i==len(arr)):
                return 0
            if((i,prev) in dict):
                return dict[(i,prev)]
            ntake,take=0,0
            ntake=lis(i+1,prev,arr,dict)
            if(prev==-1 or arr[i]>arr[prev]):
                take=1+lis(i+1,i,arr,dict)
            dict[(i,prev)]=max(ntake,take)
            return max(ntake,take)
        dict={}
        return(lis(0,-1,nums,dict))
#________________________time complexity n*n____________________________________________________________________
arr=list(map(int,input().split()))
dp=[[0]*(len(arr)+1) for x in range(len(arr)+1)]
#here prev will be form index-1 to -1 second paramter always goes to +1 state
for i in range(len(arr)):
    for prev in range(i-1,-2,-1):
        ntake=dp[i+1][prev+1]
        if(prev==-1 or arr[i]>arr[prev]):
            take=1+dp[i+1][i+1]
        dp[i][prev+1]=max(ntake,take)
print(dp[0][-1+1],'yyy')
#another method is for any index i how much the lis is  and printing lis
dp=[1]*(len(arr))
hash=[i for i in range(len(arr))]
ans=[]
for i in range(len(arr)):
    for prev in range(i):
        if(arr[i]>arr[prev]):
            if(1+dp[prev]>dp[i]):
                hash[i]=prev
                dp[i]=1+dp[prev]
i=dp.index(max(dp))
ans.append(arr[i])
while(hash[i]!=i):
    i=hash[i]
    ans.append(arr[i])
ans.reverse()
print(ans)
#________________________________time complexity n*n________________________________________________________
#binary search
#method if top < current append else bisectleft and replace with arr[i]
temp=[]
import bisect
temp.append(arr[0])
for i in range(1,len(arr)):
    if(temp[-1]<arr[i]):
        temp.append(arr[i])
    else:
        j=bisect.bisect_left(temp,arr[i])
        temp[j]=arr[i]
print(len(temp))

     





    
    
    
    
    
    
    
        