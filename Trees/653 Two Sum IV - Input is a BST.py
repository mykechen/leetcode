# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        
        diff = set()

        def check(node):
            if not node:
                return False

            if k - node.val in diff:
                return True

            diff.add(node.val)

            return check(node.left) or check(node.right)

    
        return check(root)