class Solution:
    def beautifulSubsets(self, nums, k: int) -> int:
        res = 0
        n = len(nums)
        seen = set()
        nums.sort()
        
        def dfs(subset, ind, s):
            nonlocal res
            if ind >= n:
                res+=1 if len(subset)>0 else 0
                return
            if nums[ind]-k not in seen:
                subset.append(nums[ind])
                seen.add(nums[ind])
                dfs(subset, ind+1, s+nums[ind])
                subset.pop()
                seen.discard(nums[ind])
            dfs(subset, ind+1, s)
        dfs([], 0, 0)
        return res