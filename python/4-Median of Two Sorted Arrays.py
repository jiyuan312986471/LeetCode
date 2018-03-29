class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # keep A as the short list
        A, B, m, n = nums1, nums2, len(nums1), len(nums2)
        if m > n:
            A, B, m, n = B, A, n, m

        i_min, i_max, half_len = 0, m, (m + n + 1) // 2
        while i_min <= i_max:
            i = (i_min + i_max) // 2
            j = half_len - i
            if i > 0 and A[i - 1] > B[j]:
                i_max = i - 1
            elif i < m and B[j - 1] > A[i]:
                i_min = i + 1
            else:
                if i == 0:
                    l_max = B[j - 1]
                elif j == 0:
                    l_max = A[i - 1]
                else:
                    l_max = max(A[i - 1], B[j - 1])

                if (m + n) % 2:
                    return l_max

                if i == m:
                    r_min = B[j]
                elif j == n:
                    r_min = A[i]
                else:
                    r_min = min(A[i], B[j])
                return (l_max + r_min) / 2
