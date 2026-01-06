class Solution(object):
    def rotate(self, nums, k):
        k_pos = len(nums) - k
        if k > len(nums):
            k_pos = len(nums) - (abs(len(nums) - k) % len(nums))
        nums[:] = nums[k_pos:] + nums[:k_pos]
        return nums
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        