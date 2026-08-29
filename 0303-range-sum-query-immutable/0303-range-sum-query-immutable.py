class NumArray(object):

    def __init__(self, nums):
        self.nums=nums
        """
        :type nums: List[int]
        """
    def sumRange(self, left, right):
        sum=0
        for i in range(left,right+1):
            sum+=self.nums[i]
        return sum    
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)