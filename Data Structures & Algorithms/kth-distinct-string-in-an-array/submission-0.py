class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}
        nonDistinct = set()
        for s in arr:
            count[s] = 1 + count.get(s, 0)
            if count[s] > 1:
                nonDistinct.add(s)

        i = 0
        for s in arr:
            if s not in nonDistinct:
                i += 1

            if i == k:
                return s

        return ""
        

        