import numpy as np
class Solution(object):
    def numSpecial(self, mat):
        arr = np.array(mat)
        row_sums = arr.sum(axis=1)
        col_sums = arr.sum(axis=0)
        # A position is special if:
        # value == 1 AND row sum == 1 AND col sum == 1
        special = (arr == 1) & (row_sums[:, None] == 1) & (col_sums == 1)
    
        return special.sum()
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        