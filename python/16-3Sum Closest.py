class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        leng = len(nums)
        if leng == 3:
            return sum(nums)

        min_d = nums[0] + nums[1] + nums[leng - 1] - target
        if min_d > 0:
            sign = 1
        elif min_d < 0:
            min_d = -min_d
            sign = -1
        else:
            return target

        for i0 in range(leng - 2):
            i1, i2 = i0 + 1, leng - 1
            d = nums[i0] + nums[i1] + nums[i2] - target
            while d != 0 and i1 < i2:
                d = nums[i0] + nums[i1] + nums[i2] - target
                if d > min_d:
                    i2 -= 1
                elif d < -min_d:
                    i1 += 1
                elif d > 0:
                    min_d = d
                    sign = 1
                    i2 -= 1
                else:
                    min_d = -d
                    sign = -1
                    i1 += 1
            if d == 0:
                return target
        return sign * min_d + target
