class Solution:
    def findNumberOfLIS(self, nums) -> int:
        cnt=[1]*(len(nums))
        dp=[1]*(len(nums))
        for i in range(len(nums)):
            for prev in range(i):
                if(nums[i]>nums[prev]):
                    if(dp[prev]+1>dp[i]):
                        dp[i]=dp[prev]+1
                        cnt[i]=cnt[prev]
                    elif(dp[prev]+1==dp[i]):
                        cnt[i]+=cnt[prev]
        maxi=max(dp)
        ans=0
        for i in range(len(nums)):
            if(dp[i]==maxi):
                ans+=cnt[i]
        return ans
        