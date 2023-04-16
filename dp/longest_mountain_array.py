class Solution:
    def longestMountain(self, arr) -> int:
        if(len(arr)<3):
            return 0
        dp1=[1]*(len(arr))
        dp2=[1]*(len(arr))
        for i in range(len(arr)):
            for prev in range(i):
                if(arr[i]>arr[prev]):
                    dp1[i]=max(dp1[i],dp1[prev]+1)
        for i in range(len(arr)-1,-1,-1):
            for prev in range(len(arr)-1,i,-1):
                if(arr[i]>arr[prev]):
                    dp2[i]=max(dp2[i],dp2[prev]+1)
        ans=0
        for i in range(len(dp1)):
            if(dp1[i]>1 and dp2[i]>1):
                ans=max(ans,dp1[i]+dp2[i]-1)
        return ans
        
        
#-------------------dp n*n tle---------similart to lis buts we we find lis from front in dp and back in another dp------------------
class Solution:
    def longestMountain(self,arr) -> int:
        if(len(arr)<3):
            return 0
        n=len(arr)
        dp1=[0]*(len(arr))
        dp2=[0]*(len(arr))
        for i in range(n-2,-1,-1):
            if(arr[i]>arr[i+1]):
                dp1[i]=dp1[i+1]+1
        for i in range(0,n):
            if(i>0 and arr[i-1]<arr[i]):
                dp2[i]=dp2[i-1]+1
        maxi=0
        for i in range(n):
            if(dp1[i] and dp2[i]):
                maxi=max(maxi,dp1[i]+dp2[i]+1)
        return maxi
#---------------------------two pointer methods we find back and from front-------------time(n)------------------ 
        
        
        