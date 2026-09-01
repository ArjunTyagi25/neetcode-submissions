class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k > n:
            K = k%n
        else:
            K = k

        nums[0:n] = nums[n-K:n] + nums[0:n-K]        