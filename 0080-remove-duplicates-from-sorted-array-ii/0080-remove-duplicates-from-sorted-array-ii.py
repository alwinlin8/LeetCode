class Solution(object):
    def removeDuplicates(self, nums):
        count = list(set(nums))
        new_count = sorted(count + count)
        i = 0
        while i < len(nums):
            if nums[i] in new_count:
                new_count.remove(nums[i])
                i += 1
            else:
                nums.pop(i)
        return len(nums)
        """
        :type nums: List[int]
        :rtype: int
        """
        