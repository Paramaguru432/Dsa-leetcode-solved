class Solution(object):
    def isAnagram(self, s, t):
        freq1 = {}
        freq2 = {}

        for ch in s:
            if ch in freq1:
                freq1[ch] = freq1[ch] + 1
            else:
                freq1[ch] = 1

        for ch in t:
            if ch in freq2:
                freq2[ch] = freq2[ch] + 1
            else:
                freq2[ch] = 1

        if freq1 == freq2:
            return True
        else:
            return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        