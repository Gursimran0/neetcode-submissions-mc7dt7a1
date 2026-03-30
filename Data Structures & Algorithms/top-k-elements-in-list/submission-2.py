class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1+count.get(nums[i],0)
        freq = [[] for i in range(len(nums)+1)]
        print(count)
        for num,cnt in count.items():
            freq[cnt].append(num)
        result = []
        for i in range(len(freq)-1,0,-1):
            for elem in freq[i]:
                result.append(elem)
                if len(result) == k:
                    return result
    
            


    