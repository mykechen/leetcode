class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        
        # use stack to store postiive numbers
        # if negative, compare to top of stack
        # if stack[-1] < abs(asteroids[i]), keep going until it reaches when it is bigger
            # remove top of stack
        # return stack

        stack = []

        for ast in asteroids:
            while stack and ast < 0 < stack[-1]:
                if stack[-1] < -ast:
                    stack.pop()
                    continue
                elif stack[-1] == -ast:
                    stack.pop()
                break

            else:
                stack.append(ast)

        return stack
        