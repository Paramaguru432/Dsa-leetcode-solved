class Solution(object):
    def findRepeatedDnaSequences(self, s):
        seen = set()
        repeated = set()

        for i in range(len(s) - 9):

            sequence = s[i:i + 10]

            if sequence in seen:
                repeated.add(sequence)
            else:
                seen.add(sequence)

        return list(repeated)
        """
        :type s: str
        :rtype: List[str]
        """
        