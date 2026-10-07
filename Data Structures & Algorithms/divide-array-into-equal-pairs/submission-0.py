class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for num, freq in count.items():
            if freq % 2 != 0:
                return False

        return True