class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort the candidates to handle duplicate numbers
        candidates.sort()
        res = []

        def backtrack(i, curr_comb, curr_total):
            if curr_total == target:
                res.append(curr_comb.copy())
                return
            
            if i == len(candidates) or curr_total > target:
                return

            # include the candidate at index i
            curr_comb.append(candidates[i])
            backtrack(i+1, curr_comb, curr_total + candidates[i])
            curr_comb.pop()

            # skip the candidate at index i. if candidate at i is equal to i+1, skip them
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, curr_comb, curr_total)

        backtrack(0, [], 0)

        return res
            