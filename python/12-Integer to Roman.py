class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ['', 'M', 'MM', 'MMM']
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

        m, num = divmod(num, 1000)
        c, num = divmod(num, 100)
        x, num = divmod(num, 10)
        return M[m] + C[c] + X[x] + I[num]
