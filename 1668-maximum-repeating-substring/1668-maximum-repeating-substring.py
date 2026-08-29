class Solution(object):
    def maxRepeating(self, sequence, word):
        count=0
        char=""
        while(char+word) in sequence:
            char+=word
            count+=1
        return count   
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        