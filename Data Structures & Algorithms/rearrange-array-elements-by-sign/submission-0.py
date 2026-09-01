class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_nums, neg_nums = [], []

        for num in nums:
            if num < 0:
                neg_nums.append(num)
            else:
                pos_nums.append(num)

        res = []
        for i in range(len(pos_nums)):
            res.append(pos_nums[i])
            res.append(neg_nums[i])

        return res
        