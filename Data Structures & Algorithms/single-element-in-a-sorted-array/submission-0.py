class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1

        while L<R:
            M = (L+R)//2

            if M%2 != 0:
                M = M - 1

            if nums[M] == nums[M+1]:
                L = M + 2
            else:
                R = M

        return nums[L]

        