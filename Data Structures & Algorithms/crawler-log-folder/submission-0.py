class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0

        for s in logs:
            if s == "../":
                res = max(0, res-1)
            elif s == "./":
                res = res
            else:
                res += 1

        return res
        