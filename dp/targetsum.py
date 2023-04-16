class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        sumOfNums = sum(nums)
        n = len(nums)
        if target > sumOfNums:
            return 0
        if (target + sumOfNums) % 2 != 0:
            return 0
        s1 = (sumOfNums + target) // 2
        t = [[0] * (abs(s1) + 1) for i in range(n+1)]
        t[0][0] = 1
        for i in range(1, n+1):
            for j in range(s1 + 1):
                if nums[i - 1] <= j:
                    t[i][j] = t[i - 1][j] + t[i - 1][j - nums[i - 1]]
                else:
                    t[i][j] = t[i-1][j]
        return t[n][s1]