class Solution(object):
    def removeElement(self, nums, val):
        count = 0
        for i in range(len(nums)):
            if val == nums[i]:
                nums[i] = 0
            else: 
                count += 1
        nums.sort(reverse = True)
        return count
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        