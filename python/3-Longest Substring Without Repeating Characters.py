class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lengs = [0]
        for i, c in enumerate(s):
            ss = c
            for ch in s[i + 1:]:
                if ch not in ss:
                    ss += ch
                else:
                    break
            lengs.append(len(ss))
        return max(lengs)
