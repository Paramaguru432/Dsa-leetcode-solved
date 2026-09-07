class Solution(object):
    def findTargetSumWays(self, nums, target):

        memo = {}

        def dfs(index, total):

            if index == len(nums):
                if total == target:
                    return 1
                return 0

            if (index, total) in memo:
                return memo[(index, total)]

            positive = dfs(index + 1, total + nums[index])

            negative = dfs(index + 1, total - nums[index])

            memo[(index, total)] = positive + negative

            return memo[(index, total)]

        return dfs(0, 0)