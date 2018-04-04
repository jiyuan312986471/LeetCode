class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
            return s

        # num_char in one period
        half_T = numRows - 1
        T = 2 * half_T

        rows = [''] * numRows
        for i, c in enumerate(s):
            n = i % T
            if n <= half_T:
                rows[n] += c
            else:
                rows[T - n] += c
        return ''.join(rows)
