class Solution(object):
    def repeatedNTimes(self, nums):
        seen = set()

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                return nums[i]
        """
        :type nums: List[int]
        :rtype: int
        """
        