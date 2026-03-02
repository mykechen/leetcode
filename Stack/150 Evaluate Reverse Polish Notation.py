class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = []

        for token in tokens:
            if token not in "+-/*":
                stack.append(int(token))
            else:
                digit2, digit1 = stack.pop(), stack.pop()

                if token == "+":
                    stack.append(digit1 + digit2)
                elif token == "-":
                    stack.append(digit1 - digit2)
                elif token == "*":
                    stack.append(digit1 * digit2)
                else:
                    stack.append(int(float(digit1)/digit2))

        return stack.pop()