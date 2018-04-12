class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        i, j = 0, len(height) - 1
        while i < j:
            area = (j - i) * min(height[i], height[j])
            if area > max_area:
                max_area = area

            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1

        return max_area
