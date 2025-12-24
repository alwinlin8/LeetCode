class Solution(object):
    def minimumBoxes(self, apple, capacity):
        numapples = sum(apple)
        count = 0
        i = 0
        while numapples > 0:
            sortedcap = sorted(capacity, reverse=True)
            numapples = numapples - int(sortedcap[i])
            count += 1
            i += 1
        return count
            
        
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        