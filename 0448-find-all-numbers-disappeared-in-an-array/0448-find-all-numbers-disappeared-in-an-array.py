class Solution(object):
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
                
        return result
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        