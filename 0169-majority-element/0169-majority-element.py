class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        unique = set(nums)
        for i in unique:
            if nums.count(i) > (n/2):
                return i
        """
        :type nums: List[int]
        :rtype: int
        """
        