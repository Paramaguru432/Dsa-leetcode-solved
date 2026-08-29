class Solution(object):
    def maximumGap(self, nums):
        maxi=0
        n = len(nums)
        if (n<2):
            return 0
        nums.sort()
        for k in range(1,n):
            maxi=max(maxi,nums[k]-nums[k-1]) 
        return maxi    

        """
        :type nums: List[int]
        :rtype: int
        """
        