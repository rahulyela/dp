class Solution:
    def splitArraySameAverage(self, nums) -> bool:
        s=sum(nums)
        n=len(nums)
        def f(i,target,k,dict):
            if(k==0):
                return target==0
            if(i+k>n):
                return False
            if (i,target,k) in dict:
                return dict[(i,target,k)]
            take=False
            if(nums[i]<=target):
                take=f(i+1,target-nums[i],k-1,dict)
            ntake=f(i+1,target,k,dict)
            dict[(i,target,k)]=take or ntake
            return take or ntake
        ans=False
        dict={}
        for k in range(1,len(nums)//2+1):
            if(ans):
                return ans
            if(k*s%n==0):
                x=f(0,k*s//n,k,dict)
                ans= ans or x
        return ans
#split array into 2 subsets such that average is same
#intution is similart to target but with k numbers and target will sum=k*avg so target=k*s//n and k*s%n==0

        