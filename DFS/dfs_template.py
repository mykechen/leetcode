"""
=============================================================
DFS (DEPTH FIRST SEARCH) TEMPLATES
=============================================================
"""


# =============================================================
# 1. BINARY TREE DFS — RECURSIVE
# Use: traverse/search binary trees
# Examples: Max Depth, Path Sum, Invert Tree, Validate BST
# =============================================================

# --- Preorder (root → left → right) ---
def dfs_preorder(root):
    if not root:
        return

    # process root
    dfs_preorder(root.left)
    dfs_preorder(root.right)


# --- Inorder (left → root → right) ---
def dfs_inorder(root):
    if not root:
        return

    dfs_inorder(root.left)
    # process root (for BST this gives sorted order)
    dfs_inorder(root.right)


# --- Postorder (left → right → root) ---
def dfs_postorder(root):
    if not root:
        return

    dfs_postorder(root.left)
    dfs_postorder(root.right)
    # process root (useful when you need children's results first)


# =============================================================
# 2. BINARY TREE DFS — RETURN VALUE PATTERN
# Use: calculate something about the tree bottom-up
# Examples: Max Depth, Diameter, Balanced Tree, Subtree Sum
# =============================================================
def max_depth(root):
    if not root:
        return 0  # base case

    left = max_depth(root.left)
    right = max_depth(root.right)

    return max(left, right) + 1  # combine results


# =============================================================
# 3. BINARY TREE DFS — PASS VALUE DOWN PATTERN
# Use: track path/state from root to current node
# Examples: Path Sum, Root to Leaf Paths, Max Path Sum
# =============================================================
def path_sum(root, target):
    if not root:
        return False

    # leaf node check
    if not root.left and not root.right:
        return target == root.val

    # pass remaining target down
    return (path_sum(root.left, target - root.val) or
            path_sum(root.right, target - root.val))
    
def dfs_tree(root, target):
    if not root:
        return

    if root.val == target:
        return root

    left = dfs_tree(root.left, target)
    if not left:
        return left
    return dfs_tree(root.right, target)


# =============================================================
# 4. BINARY TREE DFS — ITERATIVE (USING STACK)
# Use: when recursion depth might be too deep
# Examples: same problems as recursive, just iterative
# =============================================================
def dfs_iterative(root):
    if not root:
        return

    stack = [root]

    while stack:
        node = stack.pop()

        # process node

        # push right first so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


# =============================================================
# 5. GRAPH DFS — RECURSIVE (ADJACENCY LIST)
# Use: traverse connected components, detect cycles, find paths
# Examples: Number of Islands, Clone Graph, Course Schedule
# =============================================================
def graph_dfs_recursive(graph, start):
    visited = set()

    def dfs(node):
        if node in visited:
            return
        visited.add(node)

        # process node

        for neighbor in graph[node]:
            dfs(neighbor)

    dfs(start)


# =============================================================
# 6. GRAPH DFS — ITERATIVE (ADJACENCY LIST)
# Use: same as recursive, avoids stack overflow
# Examples: same problems as recursive
# =============================================================
def graph_dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node in visited:
            continue
        visited.add(node)

        # process node

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)


# =============================================================
# 7. GRAPH DFS — CYCLE DETECTION (DIRECTED GRAPH)
# Use: detect cycles in directed graphs
# Examples: Course Schedule, Course Schedule II
# =============================================================
def has_cycle(graph, num_nodes):
    # 0 = unvisited, 1 = in current path, 2 = fully processed
    state = [0] * num_nodes

    def dfs(node):
        if state[node] == 1:
            return True   # cycle found
        if state[node] == 2:
            return False  # already processed

        state[node] = 1  # mark as in current path

        for neighbor in graph[node]:
            if dfs(neighbor):
                return True

        state[node] = 2  # mark as fully processed
        return False

    # check all nodes (graph might be disconnected)
    for i in range(num_nodes):
        if dfs(i):
            return True

    return False


# =============================================================
# 8. GRAPH DFS — TOPOLOGICAL SORT
# Use: find valid ordering of dependencies
# Examples: Course Schedule II, Alien Dictionary
# =============================================================
def topological_sort(graph, num_nodes):
    visited = set()
    result = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)

        for neighbor in graph[node]:
            dfs(neighbor)

        result.append(node)  # add AFTER processing all neighbors

    for i in range(num_nodes):
        dfs(i)

    return result[::-1]  # reverse for correct order


# =============================================================
# 9. GRID DFS — RECURSIVE
# Use: traverse 2D grids, find connected components
# Examples: Number of Islands, Max Area of Island, Flood Fill
# =============================================================
def grid_dfs(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()

    def dfs(r, c):
        # boundary check + visited check + condition check
        if (r < 0 or r >= rows or
            c < 0 or c >= cols or
            (r, c) in visited or
            grid[r][c] == 0):  # change condition as needed
            return

        visited.add((r, c))

        # process cell

        # explore 4 directions
        dfs(r + 1, c)  # down
        dfs(r - 1, c)  # up
        dfs(r, c + 1)  # right
        dfs(r, c - 1)  # left

    # iterate over all cells
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                dfs(r, c)


# =============================================================
# 10. GRID DFS — NUMBER OF ISLANDS PATTERN
# Use: count connected components in a grid
# Examples: Number of Islands, Count Enclosed Regions
# =============================================================
def num_islands(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def dfs(r, c):
        if (r < 0 or r >= rows or
            c < 0 or c >= cols or
            grid[r][c] == "0"):
            return

        grid[r][c] = "0"  # mark visited by modifying grid

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1  # found new island
                dfs(r, c)   # sink the entire island

    return count


# =============================================================
# 11. BACKTRACKING (DFS + UNDO)
# Use: generate all combinations, permutations, subsets
# Examples: Permutations, Subsets, Combination Sum, N-Queens
# =============================================================
def backtrack(nums):
    res = []

    def dfs(path, choices):
        # base case: found valid result
        if len(path) == len(nums):
            res.append(path[:])  # append a COPY
            return

        for i, choice in enumerate(choices):
            # make choice
            path.append(choice)

            # recurse (modify choices to avoid reuse)
            dfs(path, choices[:i] + choices[i+1:])

            # undo choice
            path.pop()

    dfs([], nums)
    return res


# =============================================================
# CHEAT SHEET
# =============================================================
# Traverse binary tree            → 1. Recursive preorder/inorder/postorder
# Calculate tree property bottom-up → 2. Return value pattern
# Track path from root            → 3. Pass value down pattern
# Avoid deep recursion            → 4. Iterative with stack
# Traverse graph                  → 5/6. Graph DFS recursive/iterative
# Detect cycle in directed graph  → 7. Three-state cycle detection
# Dependency ordering             → 8. Topological sort
# Traverse 2D grid                → 9. Grid DFS
# Count connected components      → 10. Number of islands pattern
# Generate all combos/perms       → 11. Backtracking