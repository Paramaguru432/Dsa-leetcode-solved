class Solution(object):
    def pancakeSort(self, arr):
        ans = []

        for size in range(len(arr), 1, -1):
            max_index = arr.index(size)
            if max_index != 0:
                arr[:max_index + 1] = arr[:max_index + 1][::-1]
                ans.append(max_index + 1)
            arr[:size] = arr[:size][::-1]
            ans.append(size)

        return ans
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        