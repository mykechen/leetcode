# DFS cycle detection: if prerequisite graph has a cycle, courses can't all be finished
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # build adjacency list: course -> list of prerequisites
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()  # tracks nodes in current DFS path (cycle detection)
        def dfs(crs):
            if crs in visited:
                return False  # cycle detected
            if preMap[crs] == []:
                return True  # no more prereqs, base case

            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)  # backtrack — remove from current path
            preMap[crs] = []  # cache result — already verified this course
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True