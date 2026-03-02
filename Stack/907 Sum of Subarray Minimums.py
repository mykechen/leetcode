class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        # use a monotonic stack (non-decreasing)
        # loop through the entire arr
        # check if stack and stack[-1] > arr[i]
            # stack.pop()
            # and then calculate res

        # stack.append(i)

        # return res % (10**9 + 7)

        res = 0
        stack = []

        for i in range(len(arr) + 1):
            cur = arr[i] if i < len(arr) else 0

            while stack and arr[stack[-1]] >= cur:
                mid = stack.pop()
                left = mid - stack[-1] if stack else mid + 1
                right = i - mid

                res += arr[mid] * left * right

            stack.append(i)
        
        return res % (10**9 + 7)

    