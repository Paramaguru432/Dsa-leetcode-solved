class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == 1:
            return 1
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] +=1
            else :
                dict[i] = 0
        for key,value in dict.items():
            if value==0:
                return key