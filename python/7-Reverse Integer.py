class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = '-' if x < 0 else ''
        x = str(abs(x))
        s += x[::-1]
        s = int(s)
        if s > 2 ** 31 - 1 or s < -2 ** 31:
            return 0
        return s
