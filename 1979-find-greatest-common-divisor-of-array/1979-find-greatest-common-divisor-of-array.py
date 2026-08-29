class Solution(object):
    def findGCD(self, nums):
        mn=min(nums)
        mx=max(nums)
        while mn!=0:
            mx,mn=mn,mx%mn
        return mx    
        """
        :type nums: List[int]
        :rtype: int
        """
        