# https://leetcode.com/problems/n-th-tribonacci-number/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [0, 1, 1]

        for i in range(n+1):
            if i > 2:
                result.append(result[i - 3] + result[i - 2] + result[i - 1])

        return result[n]


solution = Solution()
assert solution.tribonacci(0) == 0
assert solution.tribonacci(1) == 1
assert solution.tribonacci(2) == 1
assert solution.tribonacci(3) == 2
assert solution.tribonacci(4) == 4
