class Solution(object):
    def finalPrices(self, prices):
        stack = []
        sol = [p for p in prices]
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                sol[j] -= prices[i]
            stack.append(i)
        return sol

        """
        :type prices: List[int]
        :rtype: List[int]
        """
        