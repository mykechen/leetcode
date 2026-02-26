# DFS on adjacency matrix: count connected components (provinces) in the graph
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        n = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(city):
            visited.add(city)
            for cur, connected in enumerate(isConnected[city]):
                if connected and cur not in visited:  # visit all connected cities
                    dfs(cur)

        # each unvisited city starts a new province
        for i in range(n):
            if i not in visited:
                dfs(i)
                provinces += 1

        return provinces