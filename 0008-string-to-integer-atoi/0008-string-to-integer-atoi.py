class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # 1. Remove leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1

        elif i < n and s[i] == '+':
            i += 1

        # 3. Convert digits
        number = 0

        while i < n and s[i].isdigit():

            digit = ord(s[i]) - ord('0')

            number = number * 10 + digit

            i += 1

        number *= sign

        # 4. Handle 32-bit integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if number < INT_MIN:
            return INT_MIN

        if number > INT_MAX:
            return INT_MAX

        return number
        """
        :type s: str
        :rtype: int
        """
        