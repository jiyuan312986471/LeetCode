class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, n in enumerate(nums):
            for j in range(i+1, len(nums)):
                if n + nums[j] == target:
                    return [i, j]
