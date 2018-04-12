class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        ch_v = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = ch_v[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            if ch_v[s[i]] < ch_v[s[i + 1]]:
                res -= ch_v[s[i]]
            else:
                res += ch_v[s[i]]
        return res
