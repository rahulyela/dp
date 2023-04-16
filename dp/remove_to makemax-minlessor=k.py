arr=[1, 3, 4, 9,10,11, 12, 17, 20]
k=4
arr.sort()
def remove(i,j,arr,k,dp):
    if(i>=j):
        return 0
    if(dp[i][j]!=-1):
        return dp[i][j]
    if(arr[j]-arr[i]<=k):
        return 0
    if(arr[j]-arr[i]>k):
        ans=1+min(remove(i+1,j,arr,k,dp),remove(i,j-1,arr,k,dp))
        dp[i][j]=ans
        return ans
dp=[[-1]*(len(arr)) for x in range(len(arr))]
print(remove(0,len(arr)-1,arr,k,dp))
#____________________________________time complexity (n*n)________________________-
def binary(i,key,arr):
    ans=-1
    low=i+1
    high=len(arr)-1
    while(low<high):
        mid=low+(high-low)//2
        if(arr[mid]-key<=k):
            ans=mid
            low=mid+1
        else:
            high=mid
    return ans
mini=float('inf')
for i in range(len(arr)):
    j=binary(i,arr[i],arr)
    if(j!=-1):
        mini=min(mini,len(arr)-(j-i+1))
print( mini)
#-------------------------------time complexity (nlogn)------------------------------------------------