class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[True] + [False] * len(s)]
        for i, pc in enumerate(p):
            r = [pc == '*' and dp[-2][0]]
            for j, sc in enumerate(s):
                j += 1  # counting col for empty s
                if pc == '*':
                    match_0 = dp[-2][j]
                    match_1_or_plus = (p[i - 1] == sc or p[i - 1] == '.') and r[
                        j - 1]
                    r.append(match_0 or match_1_or_plus)
                elif pc == '.':
                    r.append(dp[-1][j - 1])
                else:
                    r.append(dp[-1][j - 1] and pc == sc)
            dp.append(r)
        return dp[-1][-1]
