# https://leetcode.com/problems/house-robber/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            dp[i] = max((nums[i] + dp[i-2]), dp[i-1])

        return max(dp[-1], dp[-2])


solution = Solution()
assert solution.rob([2,1,1,2]) == 4
assert solution.rob([1,2,3,1]) == 4
assert solution.rob([2,7,9,3,1]) == 12
