class Solution(object):
    def isPowerOfTwo(self, n):
        return n>0 and (n&(n-1))==0
        """
        :type n: int
        :rtype: bool
        """
        