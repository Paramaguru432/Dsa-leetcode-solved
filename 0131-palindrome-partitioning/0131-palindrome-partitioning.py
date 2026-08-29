class Solution(object):
    def partition(self, s):
        result = []

        def isPalindrome(left, right):

            while left < right:

                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        def backtrack(start, path):

            # Entire string is partitioned
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start, len(s)):

                # Check whether s[start:end+1] is palindrome
                if isPalindrome(start, end):

                    # Choose
                    path.append(s[start:end + 1])

                    # Explore
                    backtrack(end + 1, path)

                    # Undo
                    path.pop()

        backtrack(0, [])

        return result
        """
        :type s: str
        :rtype: List[List[str]]
        """
        