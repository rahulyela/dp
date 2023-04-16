class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        s=sum(nums)
        target=s//k
        if(s%k!=0):
            # print(1)
            return False
        visited=[False]*(len(nums))
        nums.sort(reverse=True)
        def sub(i,nums,cursum,k):
            # print(k,visited)
            if(k==1):
                return True
            if(target==cursum):
                return sub(0,nums,0,k-1)
            for i in range(i,len(nums)):
                if(visited[i]==False and nums[i]+cursum<=target):
                    visited[i]=True
                    if(sub(i+1,nums,cursum+nums[i],k)):
                        return True
                    else:
                        visited[i]=False
            return False
        return sub(0,nums,0,k)
#------------backtracking O(k*(2**n))
class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        nums_sum = sum(nums)
        n=len(nums)
        if nums_sum % k != 0:
            return False
        subset_sum = nums_sum // k
        nums.sort(reverse=True)
        mask=0
        Sum=0
        def part(mask,k,Sum,dp):
            if(k==1):
                return True
            if(Sum==subset_sum):
                return part(mask,k-1,0,dp)
            if(dp[mask]!=-1):
                return dp[mask]
            for i in range(len(nums)):
                if(mask &(1<<i)==0 and Sum+nums[i]<=subset_sum):
                    mask=mask|(1<<i)
                    if(part(mask,k,Sum+nums[i],dp)):
                        dp[mask]=True
                        return True
                    else:
                        mask^=(1<<i)
            dp[mask]=False
            return False
        dp=[-1]*((1<<n)+1)
        return part(mask,k,Sum,dp)
#dp with bitmasking                   
                    
            
       
                
        