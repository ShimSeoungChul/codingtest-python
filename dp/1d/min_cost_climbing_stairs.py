# https://leetcode.com/problems/min-cost-climbing-stairs/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        if not cost:
            return 0

        dp = [0] * len(cost)
        dp[0] = cost[0]

        if len(cost) >= 2:
            dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[-1], dp[-2])


solution = Solution()
assert solution.minCostClimbingStairs([10, 15]) == 10
assert solution.minCostClimbingStairs([10, 15, 20]) == 15
assert solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
