class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        ans = []
        for i in range(len(nums)):
            counter = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    counter += 1
            ans.append(counter)
        return ans
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        