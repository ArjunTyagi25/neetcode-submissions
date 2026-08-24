class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i, curr_combo):
            if len(curr_combo) == k:
                res.append(curr_combo.copy())
                return

            if i == n+1:
                return

            curr_combo.append(i)
            backtrack(i+1, curr_combo)
            curr_combo.pop()
            backtrack(i+1, curr_combo)

        backtrack(1, [])

        return res
        