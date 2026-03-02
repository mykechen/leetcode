"""
=============================================================
TREE TEMPLATES
=============================================================
"""

from collections import deque


# =============================================================
# BASIC NODE DEFINITION
# =============================================================
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# =============================================================
# 1. DFS — RETURN VALUE (BOTTOM-UP)
# Use: calculate something about the tree from leaves up
# Examples: Max Depth, Diameter, Balanced Tree, Subtree Sum
# =============================================================
def max_depth(root):
    if not root:
        return 0

    left = max_depth(root.left)
    right = max_depth(root.right)

    return max(left, right) + 1


# =============================================================
# 2. DFS — PASS VALUE DOWN (TOP-DOWN)
# Use: track path/state from root to current node
# Examples: Path Sum, Root to Leaf Paths, Valid BST
# =============================================================
def path_sum(root, target):
    if not root:
        return False

    if not root.left and not root.right:
        return target == root.val

    return (path_sum(root.left, target - root.val) or
            path_sum(root.right, target - root.val))


# =============================================================
# 3. DFS — VALID BST (RANGE PASSING)
# Use: validate BST or find violations
# Examples: Validate BST, Recover BST
# =============================================================
def is_valid_bst(root):
    def dfs(node, low, high):
        if not node:
            return True

        if node.val <= low or node.val >= high:
            return False

        return (dfs(node.left, low, node.val) and
                dfs(node.right, node.val, high))

    return dfs(root, float('-inf'), float('inf'))


# =============================================================
# 4. DFS — DIAMETER / GLOBAL VARIABLE PATTERN
# Use: track a global answer while returning something else
# Examples: Diameter, Max Path Sum, Longest Univalue Path
# =============================================================
def diameter(root):
    result = [0]  # use list to modify in nested function

    def dfs(node):
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        # update global answer (path through this node)
        result[0] = max(result[0], left + right)

        # return height to parent
        return max(left, right) + 1

    dfs(root)
    return result[0]


# =============================================================
# 5. DFS — SAME TREE / SYMMETRIC (TWO NODE COMPARISON)
# Use: compare two trees or mirror halves
# Examples: Same Tree, Symmetric Tree, Subtree of Another Tree
# =============================================================
def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False

    return (is_same_tree(p.left, q.left) and
            is_same_tree(p.right, q.right))


def is_symmetric(root):
    def dfs(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False

        return (dfs(left.left, right.right) and
                dfs(left.right, right.left))

    return dfs(root.left, root.right)


# =============================================================
# 6. DFS — INORDER TRAVERSAL (BST → SORTED ORDER)
# Use: process BST nodes in sorted order
# Examples: Kth Smallest, Validate BST, Convert BST to List
# =============================================================
def kth_smallest(root, k):
    count = [0]
    result = [0]

    def inorder(node):
        if not node:
            return

        inorder(node.left)

        count[0] += 1
        if count[0] == k:
            result[0] = node.val
            return

        inorder(node.right)

    inorder(root)
    return result[0]


# =============================================================
# 7. BFS — LEVEL ORDER TRAVERSAL
# Use: process tree level by level
# Examples: Level Order, Zigzag, Right Side View, Average Levels
# =============================================================
def level_order(root):
    if not root:
        return []

    res = []
    queue = deque([root])

    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        res.append(level)

    return res


# =============================================================
# 8. BFS — RIGHT SIDE VIEW
# Use: see tree from one side
# Examples: Right Side View, Left Side View
# =============================================================
def right_side_view(root):
    if not root:
        return []

    res = []
    queue = deque([root])

    while queue:
        for i in range(len(queue)):
            node = queue.popleft()

            if i == len(queue):  # last node in level before we added children
                res.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return res


# Better approach: just take last element of each level
def right_side_view_simple(root):
    if not root:
        return []

    res = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            if i == level_size - 1:  # last node in this level
                res.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return res


# =============================================================
# 9. CONSTRUCT TREE FROM TRAVERSALS
# Use: build tree from preorder/inorder or inorder/postorder
# Examples: Construct from Preorder+Inorder, Postorder+Inorder
# =============================================================
def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    # first element of preorder is always root
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])

    root.left = build_tree(preorder[1:mid + 1], inorder[:mid])
    root.right = build_tree(preorder[mid + 1:], inorder[mid + 1:])

    return root


# Optimized with hashmap
def build_tree_optimized(preorder, inorder):
    inorder_map = {val: idx for idx, val in enumerate(inorder)}

    def helper(pre_start, in_start, in_end):
        if pre_start > len(preorder) - 1 or in_start > in_end:
            return None

        root = TreeNode(preorder[pre_start])
        mid = inorder_map[root.val]

        root.left = helper(pre_start + 1, in_start, mid - 1)
        root.right = helper(pre_start + 1 + mid - in_start, mid + 1, in_end)

        return root

    return helper(0, 0, len(inorder) - 1)


# =============================================================
# 10. LOWEST COMMON ANCESTOR (LCA)
# Use: find shared ancestor of two nodes
# Examples: LCA of Binary Tree, LCA of BST
# =============================================================

# Binary Tree LCA
def lca(root, p, q):
    if not root or root == p or root == q:
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root   # p and q are on different sides
    return left or right


# BST LCA (use BST property to go left or right)
def lca_bst(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left    # both on left
        elif p.val > root.val and q.val > root.val:
            root = root.right   # both on right
        else:
            return root  # split point = LCA


# =============================================================
# 11. SERIALIZE / DESERIALIZE TREE
# Use: convert tree to string and back
# Examples: Serialize and Deserialize Binary Tree
# =============================================================
def serialize(root):
    if not root:
        return "null"

    return (str(root.val) + "," +
            serialize(root.left) + "," +
            serialize(root.right))


def deserialize(data):
    nodes = iter(data.split(","))

    def helper():
        val = next(nodes)
        if val == "null":
            return None

        node = TreeNode(int(val))
        node.left = helper()
        node.right = helper()
        return node

    return helper()


# =============================================================
# 12. INVERT BINARY TREE
# Use: mirror/flip a tree
# Examples: Invert Binary Tree
# =============================================================
def invert_tree(root):
    if not root:
        return None

    root.left, root.right = root.right, root.left

    invert_tree(root.left)
    invert_tree(root.right)

    return root


# =============================================================
# 13. FLATTEN TREE TO LINKED LIST
# Use: convert tree to right-only linked list
# Examples: Flatten Binary Tree to Linked List
# =============================================================
def flatten(root):
    if not root:
        return

    flatten(root.left)
    flatten(root.right)

    # save right subtree
    right = root.right

    # move left subtree to right
    root.right = root.left
    root.left = None

    # find end of new right subtree and attach old right
    curr = root
    while curr.right:
        curr = curr.right
    curr.right = right


# =============================================================
# CHEAT SHEET
# =============================================================
# Calculate property bottom-up      → 1. Return value (depth, height)
# Track state from root down        → 2. Pass value down (path sum)
# Validate BST                      → 3. Range passing
# Global answer + return different   → 4. Diameter pattern
# Compare two trees/halves          → 5. Same tree / symmetric
# BST in sorted order               → 6. Inorder traversal
# Process level by level            → 7. BFS level order
# See tree from one side            → 8. Right side view
# Build tree from traversals        → 9. Construct from preorder+inorder
# Find shared ancestor              → 10. LCA
# Convert tree to/from string       → 11. Serialize/deserialize
# Mirror/flip tree                  → 12. Invert
# Tree to linked list               → 13. Flatten