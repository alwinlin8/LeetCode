class Solution(object):
    def hIndex(self, citations):
        n = len(citations)
        citations.sort()
        for i,v in enumerate(citations): # i is index, v is value of citation
            if n - i <= v:
                return n - i
            else:
                return 0

        """
        :type citations: List[int]
        :rtype: int
        """
        