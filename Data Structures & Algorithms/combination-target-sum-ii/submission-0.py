class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        curr_comb, res = [], []
        self.helper(0, candidates, target, curr_comb, res)

        return res

    def helper(self, i, candidates, target, curr_comb, res):
        if sum(curr_comb) == target:
            res.append(curr_comb.copy())
            return
        
        if i == len(candidates) or sum(curr_comb) > target:
            return

        for j in range(i, len(candidates)):
            if j > i and candidates[j] == candidates[j-1]:
                continue 
            curr_comb.append(candidates[j])
            self.helper(j+1, candidates, target, curr_comb, res)
            curr_comb.pop()