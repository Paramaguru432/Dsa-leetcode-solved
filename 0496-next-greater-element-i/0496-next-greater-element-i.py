class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}

        for num in nums2:

            while stack and num > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = num

            stack.append(num)

        result = []

        for num in nums1:
            if num in next_greater:
                result.append(next_greater[num])
            else:
                result.append(-1)

        return result
        