class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        words.reverse()
        return " ".join(words)
        """
        :type s: str
        :rtype: str
        """
        