class Solution(object):
    def lengthOfLastWord(self, s):
        reverse = s[::-1]
        reverse = reverse.strip()
        count = 0
        for i in range(len(reverse)):
            if reverse[i] == " ":
                break
            else:
                 count += 1
        return count
        """
        :type s: str
        :rtype: int
        """
        