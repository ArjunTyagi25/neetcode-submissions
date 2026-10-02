class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        n = len(nums)
        res = []
        print(freq)
        for num in freq:
            if freq[num] > int(n/3):
                res.append(num)

        return res