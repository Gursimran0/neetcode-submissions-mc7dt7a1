class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        check ={}
        if len(trust) == 0:
            return -1
        for i in range(1,n+1):
            check[i] = []

        for i in range(len(trust)):
            check[trust[i][0]].append(trust[i][1])
        print(check)
        testInd = -1
        for ind,val in check.items():
            if len(val) == 0:
                testInd = ind
        for ind,val in check.items():
            if ind!=testInd:
                if testInd not in val:
                    return -1

        print(testInd)
        return testInd




        