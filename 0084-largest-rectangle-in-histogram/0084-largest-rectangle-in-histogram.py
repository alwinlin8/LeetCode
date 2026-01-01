class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        areas = [h for h in heights]
        counter = 1

        for i in range(len(heights)):
            while stack and heights[stack[-1]] <= heights[i]:
                j = stack.pop()
                print(counter)
                areas[j] = (min(heights[j], heights[i])) * counter #not always 2
                counter += 1
            stack.append(i)
            counter = 1
        print(areas)
        return max(areas)
        """
        :type heights: List[int]
        :rtype: int
        """
        