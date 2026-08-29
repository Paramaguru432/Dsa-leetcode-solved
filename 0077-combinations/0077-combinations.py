class Solution(object):
    def combine(self, n, k):
        result = []

        def backtrack(start, path):

            # We selected k numbers
            if len(path) == k:
                result.append(path[:])
                return

            for i in range(start, n + 1):

                # Choose
                path.append(i)

                # Explore
                backtrack(i + 1, path)

                # Undo
                path.pop()

        backtrack(1, [])

        return result
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        