class Solution(object):
    def removeDuplicates(self, nums):
        length = len(nums)
        new_length = len(set(nums))
        nums[:] = sorted(set(nums))
        return new_length
        """
        :type nums: List[int]
        :rtype: int
        """
        