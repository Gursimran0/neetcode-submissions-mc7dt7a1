class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        freq = [[] for i in range(len(nums)+1)]
        for i in range(len(nums)):
            count[nums[i]] = 1+count.get(nums[i],0)
        print(count)
        for key,val in count.items():
            freq[val].append(key)
        for i in range(len(freq)-1,0,-1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res)==k:
                    return res
            
        