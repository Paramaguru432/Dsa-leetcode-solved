class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""
        
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        longest = ""
        for i in range(len(s)):
            # Odd-length palindrome (center at i)
            odd = expandAroundCenter(i, i)
            # Even-length palindrome (center between i and i + 1)
            even = expandAroundCenter(i, i + 1)
            
            # Pick the longer palindrome from odd/even
            current_longest = odd if len(odd) > len(even) else even
            
            # Update longest if we found a bigger one
            if len(current_longest) > len(longest):
                longest = current_longest
                
        return longest
        """
        :type s: str
        :rtype: str
        """
        