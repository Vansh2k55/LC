from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph=defaultdict(list)
        path=set()
        finished=set()
        for course,pre in prerequisites:
            graph[course].append(pre)

        def dfs(course):
            if course in finished:
                return True
            if course in path:
                return False
            path.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False

            path.remove(course)
            finished.add(course)
            return True 

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True       