class Solution(object):
    def xorAfterQueries(self, nums, queries):
        for start, end, step, mult in queries:
            idx = start
            while idx <= end and idx < len(nums):
                nums[idx] = (nums[idx] * mult) % (10**9 + 7)
                idx += step
        res = 0
        for x in nums:
            res ^= x
        
        return res
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        