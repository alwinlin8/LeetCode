class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while numbers[l] + numbers[r] != target:
            total = numbers[l] + numbers[r]
            if total > target:
                r -= 1
            else:
                l += 1
        return l+1, r+1
        
            
    

        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        