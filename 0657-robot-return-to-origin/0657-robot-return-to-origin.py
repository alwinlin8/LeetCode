class Solution(object):
    def judgeCircle(self, moves):
        vert, hor = 0,0
        for i in range(len(moves)):
            if moves[i] == "U":
                vert += 1
            elif moves[i] == "D":
                vert -= 1
            elif moves[i] == "L":
                hor -= 1
            elif moves[i == "R"]:
                hor += 1
        return vert == 0 and hor == 0
        """
        :type moves: str
        :rtype: bool
        """
        