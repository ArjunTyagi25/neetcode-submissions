class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        nums_idx = [(nums[i], i) for i in range(len(nums))]
        heapq.heapify(nums_idx)

        for _ in range(k):
            num, idx = heapq.heappop(nums_idx)
            heapq.heappush(nums_idx, (num * multiplier, idx))

        res = [0] * len(nums)
        for i in range(len(nums_idx)):
            res[nums_idx[i][1]] = nums_idx[i][0]
        return res
        