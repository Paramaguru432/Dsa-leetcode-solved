class Solution(object):
    def rob(self, nums):
        n = len(nums)

        if n == 1:
            return nums[0]

        # Case 1: Rob houses from 0 to n-2
        case1 = self.rob_linear(nums, 0, n - 2)

        # Case 2: Rob houses from 1 to n-1
        case2 = self.rob_linear(nums, 1, n - 1)

        return max(case1, case2)

    def rob_linear(self, nums, start, end):
        prev2 = 0
        prev1 = 0

        for i in range(start, end + 1):
            current = max(
                prev1,
                prev2 + nums[i]
            )

            prev2 = prev1
            prev1 = current

        return prev1