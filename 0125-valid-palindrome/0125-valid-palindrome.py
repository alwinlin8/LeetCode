class Solution(object):
    def isPalindrome(self, s):
        l, r = 0, 0
        palindrome = list()
        for i in range(len(s)):
            if s[i].isalpha() is True:
                palindrome.append(s[i])
            elif s[i].isnumeric() is True:
                palindrome.append(s[i])
        palindrome = "".join(palindrome)
        palindrome = palindrome.lower()
        r = len(palindrome)-1
        while l < r:
            if palindrome[l] == palindrome[r]:
                l += 1
                r -= 1
            else: return False
        return True

        """
        :type s: str
        :rtype: bool
        """
        