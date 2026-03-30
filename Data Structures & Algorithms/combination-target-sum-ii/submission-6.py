class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()
        def dfs(i,curr,total):
            if total == target:
                res.add(tuple(curr[:]))
                return
            if i>=len(candidates) or total>target:
                return
            curr.append(candidates[i])
            dfs(i+1,curr,total+candidates[i])
            curr.pop()
            dfs(i+1,curr,total)
        dfs(0,[],0)
        return [list(elem) for elem in res]