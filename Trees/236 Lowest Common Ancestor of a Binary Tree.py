# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        # BC: if curr node is p or q, return
        if root == p or root == q:
            return root

        left = right = None

        # look through left and right child
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        # if both children returned a node
        # both p and q found so parent is LCA
        if left and right:
            return root
        else:
            # if only one of the children found a node
            # that means the one found the node is the LCA as 
            # the other child is somewhere down the tree on the node that didnt find one
            # Example: assuming 'p' found in left child, right child returned 'None'. This means 'q' is
            # somewhere below node where 'p' was found we dont need to search all the way, 
            # because in such scenarios, node where 'p' found is LCA
            return left or right