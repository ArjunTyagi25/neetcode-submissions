class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            tar_sum = -nums[i]
            L, R = i+1, len(nums)-1

            while L < R:
                cur_sum = nums[L] + nums[R]

                if cur_sum < tar_sum:
                    L += 1
                elif cur_sum > tar_sum:
                    R -= 1
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    while L < R and nums[L] == nums[L-1]:
                        L += 1

        return res
