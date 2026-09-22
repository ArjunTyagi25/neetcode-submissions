class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low
        if diff != 0:
            return (high - low)//2 + 1
        else:
            if low%2 != 0:
                return 1
            elif high%2 != 0:
                return 1
            else:
                return 0
        