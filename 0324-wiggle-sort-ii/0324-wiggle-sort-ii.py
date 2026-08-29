class Solution(object):
    def wiggleSort(self, nums):
        # 1. Sort the list properly
        nums.sort()
        n = len(nums)
        
        # 2. Initialize placeholders
        res = [0] * n
        left = (n - 1) // 2  # Integer division
        right = n - 1
        
        # 3. Interleave elements
        for i in range(n):
            if i % 2 == 0:
                res[i] = nums[left]
                left -= 1
            else:
                res[i] = nums[right]
                right -= 1
                
        # 4. Modify nums in place
        nums[:] = res
