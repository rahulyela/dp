class Solution:
    def largestDivisibleSubset(self, nums):
        if(len(nums)==1):
            return nums
        nums.sort()
        dp=[1]*(len(nums))
        index=0
        t=[i for i in range(len(nums))]
        for i in range(1,len(nums)):
            for prev in range(i):
                if((nums[i]%nums[prev])==0):
                    if(dp[i]<dp[prev]+1):
                        dp[i]=dp[prev]+1
                        t[i]=prev
        i=dp.index(max(dp))
        # print(t,dp)
        ans=[]
        ans.append(nums[i])
        while(t[i]!=i):
            i=t[i]
            ans.append(nums[i])
            # print(i)
        return ans
#intution similar longest incresing sub but instaed we use arr[i]%arr[prev]==0 and printing simiar to lis
        