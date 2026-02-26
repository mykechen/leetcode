"""
=============================================================
BFS (BREADTH FIRST SEARCH) TEMPLATES
=============================================================
"""

from collections import deque


# =============================================================
# 1. BINARY TREE BFS — LEVEL ORDER TRAVERSAL
# Use: process tree level by level
# Examples: Level Order Traversal, Zigzag, Right Side View
# =============================================================
def level_order(root):
    if not root:
        return []

    res = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        res.append(level)

    return res


# =============================================================
# 2. BINARY TREE BFS — MIN DEPTH / SHORTEST PATH IN TREE
# Use: find shortest path from root to a target
# Examples: Minimum Depth, Find Nearest Leaf
# =============================================================
def min_depth(root):
    if not root:
        return 0

    queue = deque([(root, 1)])  # (node, depth)

    while queue:
        node, depth = queue.popleft()

        # first leaf we hit = shortest path
        if not node.left and not node.right:
            return depth

        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))


# =============================================================
# 3. GRAPH BFS — SHORTEST PATH (UNWEIGHTED)
# Use: find shortest path in unweighted graph
# Examples: Word Ladder, Shortest Path in Binary Matrix
# =============================================================
def graph_bfs_shortest_path(graph, start, end):
    visited = {start}
    queue = deque([(start, 0)])  # (node, distance)

    while queue:
        node, dist = queue.popleft()

        if node == end:
            return dist

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return -1  # no path found


# =============================================================
# 4. GRAPH BFS — LEVEL BY LEVEL
# Use: process graph level by level (like tree level order)
# Examples: Word Ladder, All Nodes Distance K
# =============================================================
def graph_bfs_level(graph, start):
    visited = {start}
    queue = deque([start])
    level = 0

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            # process node at current level

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        level += 1


# =============================================================
# 5. GRID BFS — SHORTEST PATH
# Use: find shortest path in a grid
# Examples: Shortest Path in Binary Matrix, Rotting Oranges
# =============================================================
def grid_bfs_shortest_path(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    visited = {start}
    queue = deque([(start, 0)])  # ((row, col), distance)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        (r, c), dist = queue.popleft()

        if (r, c) == end:
            return dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (0 <= nr < rows and
                0 <= nc < cols and
                (nr, nc) not in visited and
                grid[nr][nc] == 0):  # change condition as needed

                visited.add((nr, nc))
                queue.append(((nr, nc), dist + 1))

    return -1  # no path found


# =============================================================
# 6. GRID BFS — MULTI-SOURCE (EXPAND FROM ALL SOURCES AT ONCE)
# Use: spread outward from multiple starting points simultaneously
# Examples: Rotting Oranges, Walls and Gates, 01 Matrix
# =============================================================
def multi_source_bfs(grid):
    rows = len(grid)
    cols = len(grid[0])
    queue = deque()
    visited = set()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # step 1: add ALL sources to queue
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == SOURCE:  # e.g., rotten orange, gate
                queue.append((r, c, 0))  # (row, col, distance)
                visited.add((r, c))

    # step 2: BFS from all sources simultaneously
    while queue:
        r, c, dist = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (0 <= nr < rows and
                0 <= nc < cols and
                (nr, nc) not in visited and
                grid[nr][nc] == TARGET):  # e.g., fresh orange, empty room

                visited.add((nr, nc))
                grid[nr][nc] = dist + 1  # update distance
                queue.append((nr, nc, dist + 1))


# =============================================================
# 7. BFS — TRACK FULL PATH
# Use: when you need the actual path, not just distance
# Examples: Word Ladder II, Shortest Path with Path Reconstruction
# =============================================================
def bfs_with_path(graph, start, end):
    visited = {start}
    queue = deque([(start, [start])])  # (node, path_so_far)

    while queue:
        node, path = queue.popleft()

        if node == end:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return []  # no path found


# =============================================================
# 8. BFS — BIDIRECTIONAL (MEET IN THE MIDDLE)
# Use: optimize shortest path when start and end are known
# Examples: Word Ladder (optimized), Shortest Path
# =============================================================
def bidirectional_bfs(graph, start, end):
    if start == end:
        return 0

    front = {start}
    back = {end}
    visited = {start, end}
    dist = 0

    while front and back:
        dist += 1

        # always expand the smaller set
        if len(front) > len(back):
            front, back = back, front

        next_front = set()
        for node in front:
            for neighbor in graph[node]:
                if neighbor in back:
                    return dist  # met in the middle

                if neighbor not in visited:
                    visited.add(neighbor)
                    next_front.add(neighbor)

        front = next_front

    return -1  # no path found


# =============================================================
# CHEAT SHEET
# =============================================================
# Process tree level by level      → 1. Level order traversal
# Shortest path in tree            → 2. Min depth pattern
# Shortest path in graph           → 3. Graph BFS shortest path
# Process graph level by level     → 4. Graph BFS level by level
# Shortest path in grid            → 5. Grid BFS shortest path
# Spread from multiple sources     → 6. Multi-source BFS
# Need the actual path             → 7. BFS with path tracking
# Optimize when start+end known    → 8. Bidirectional BFS