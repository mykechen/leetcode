class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []

        res = []
        digits_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(path, idx):
            if len(digits) == len(path):
                res.append("".join(path))
                return

            for c in digits_to_letters[digits[idx]]:
                path.append(c)
                backtrack(path, idx+1)
                path.pop()

        backtrack([], 0)
        return res