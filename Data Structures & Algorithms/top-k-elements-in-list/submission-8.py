class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for elem in nums:
            count[elem] = 1+count.get(elem,0)
        res = []
        resCount = [[] for i in range(len(nums)+1)]
        for ind,val in count.items():
            resCount[val].append(ind)
        print(resCount)
        for i in range(len(resCount)-1,-1,-1):
            for j in range(len(resCount[i])):
                res.append(resCount[i][j])
                if len(res) == k:
                    return res
