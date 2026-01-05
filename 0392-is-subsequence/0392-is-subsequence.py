class Solution(object):
    def isSubsequence(self, s, t):
        l = 0
        check = []
        for r in range(len(t)):
            if len(s) == 0:
                return True
            elif s[l] == t[r] and l <= len(s):
                check.append(t[r])
                if l < len(s) - 1:
                    l += 1
        return "".join(check) == s
            

        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        