class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prereq = defaultdict(list)
        for crs,pre in prerequisites:
            prereq[crs].append(pre)
        print(prereq)
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if prereq[crs] == []:
                return True

            visitSet.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
                visitSet.add(crs)
            prereq[crs] = []
            visitSet.remove(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
        
        

        