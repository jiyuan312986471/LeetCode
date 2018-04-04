class Solution:
    def palindrome(self, s, i):
        leng = len(s)

        # odd
        l, r = i, i
        while l >= 0 and r < leng and s[l] == s[r]:
            l -= 1
            r += 1
        palin = s[l + 1:r]

        # even
        l, r = i, i + 1
        while l >= 0 and r < leng and s[l] == s[r]:
            l -= 1
            r += 1
        palin = s[l + 1:r] if r - l - 1 > len(palin) else palin
        return palin

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ''
        for i, _ in enumerate(s):
            palin = self.palindrome(s, i)
            if len(palin) > len(longest):
                longest = palin
        return longest
