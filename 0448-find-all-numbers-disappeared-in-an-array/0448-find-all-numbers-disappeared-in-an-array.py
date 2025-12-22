class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        nums_set = set(nums)
        missing = []

        for i in range(1, n + 1):
            if i not in nums_set:
                missing.append(i)

        return missing
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        