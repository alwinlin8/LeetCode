class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        tot = 0
        happiness.sort(reverse=True)
        for i in range(k):
            tot += max(happiness[i]-i,0)
        return tot
            
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        