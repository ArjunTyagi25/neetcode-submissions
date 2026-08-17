class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1

        while L<R:
            M = (L+R)//2

            if nums[M] > nums[R]:
                L = M + 1
            else:
                R = M

        pivot = R
        # if target > nums[0]:
        L, R = 0, pivot-1
        # else:
            # L, R = pivot, len(nums)-1

        while L<=R:
            M = (L+R)//2

            if nums[M] < target:
                L = M + 1
            elif nums[M] > target:
                R = M - 1
            else:
                return M

        L, R = pivot, len(nums)-1

        while L<=R:
            M = (L+R)//2

            if nums[M] < target:
                L = M + 1
            elif nums[M] > target:
                R = M - 1
            else:
                return M

        return -1
            
        
        
        