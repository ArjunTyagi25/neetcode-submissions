class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1
        pivot = float('inf')
        pivot_index = -1

        while L<=R:
            if nums[L] < nums[R]:
                if nums[L] < pivot:
                    pivot_index = L
                    pivot = nums[L]
                break

            M = (L+R)//2
            if nums[M] < pivot:
                pivot_index = M
                pivot = nums[M]

            if nums[L] <= nums[M]:
                L = M + 1
            else:
                R = M - 1
            
        L, R = 0, pivot_index - 1
        while L<=R:
            M = (L+R)//2

            if nums[M] < target:
                L = M + 1
            elif nums[M] > target:
                R = M - 1
            else:
                return M

        L, R = pivot_index, len(nums)-1
        while L<=R:
            M = (L+R)//2

            if nums[M] < target:
                L = M + 1
            elif nums[M] > target:
                R = M - 1
            else:
                return M

        return -1
        