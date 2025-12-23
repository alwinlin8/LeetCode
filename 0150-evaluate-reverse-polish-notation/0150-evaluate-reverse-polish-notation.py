class Solution(object):
    def evalRPN(self, tokens):
        nums = []
        op = []
        output = 0
        for i in range(len(tokens)):
            if tokens[i].isnumeric() or tokens[i][1:].isnumeric():
                nums.append(int(tokens[i]))
            else:
                output = 0
                op1 = nums.pop()
                op2 = nums.pop()
                if tokens[i] == "+":
                    output = op1 + op2
                elif tokens[i] == "-":
                    output = op2 - op1
                elif tokens[i] == "*":
                    output = op1 * op2
                elif tokens[i] == "/":
                    if op2 * op1 < 0:
                        output = abs(op2) // abs(op1)
                        output *= -1
                    else:
                        output = op2 // op1
                nums.append(output)

        return nums[0]

        """
        :type tokens: List[str]
        :rtype: int
        """
        