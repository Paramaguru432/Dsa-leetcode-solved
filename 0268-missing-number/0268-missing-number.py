class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        expec_sum=n*(n+1)//2
        actual_sum=sum(nums)
        return expec_sum-actual_sum
        """
        :type nums: List[int]
        :rtype: int
        """
        