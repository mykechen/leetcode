class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []

        def backtrack(path, openP, closeP):
            if openP == closeP and openP + closeP == 2 * n:
                res.append("".join(path))
                return
            
            # add open parantheses
            if openP < n:
                path.append("(")
                backtrack(path, openP+1, closeP)
                path.pop()

            # add close parantheses
            if closeP < openP:
                path.append(")")
                backtrack(path, openP, closeP+1)
                path.pop()

        backtrack([], 0, 0)
        return res