class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq_nums = [num*num for num in nums]
        res = []

        l, r = 0, len(nums)-1
        while l<=r:
            if sq_nums[l] > sq_nums[r]:
                res.append(sq_nums[l])
                l += 1
            else:
                res.append(sq_nums[r])
                r -= 1
        
        return res[::-1]
        