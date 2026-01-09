class Solution(object):
    def canJump(self, nums):
        m = 0 #Maximum index reached
        for i, n in enumerate(nums):
            if i > m: #if i ever gets past m that means you can never reach m(goal)
                return False
            m = max(m, i+n)
        return True
        """
        :type nums: List[int]
        :rtype: bool
        """
        