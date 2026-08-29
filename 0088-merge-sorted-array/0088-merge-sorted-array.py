class Solution(object):
    def merge(self, nums1, m, nums2, n):
        k=0
        for i in range(m):
            if nums1[i] in nums1:
                nums1[k]=nums1[i]
                k+=1
        for j in range(n):
            if nums2[j] in nums2:
                nums1[k]=nums2[j]
                k+=1
        return nums1.sort()            

        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        