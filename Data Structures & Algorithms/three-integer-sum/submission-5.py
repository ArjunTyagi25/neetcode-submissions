class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        # Iterate through all numbers
        for i in range(len(nums)):
            # Skip duplicate value 
            if i and nums[i] == nums[i-1]:
                continue

            # Iterate through [i+1 : len(nums)] numbers
            L, R = i+1, len(nums)-1
            while L<R:
                threeSum = nums[i] + nums[L] + nums[R]

                if threeSum < 0:
                    L = L + 1
                elif threeSum == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    L = L + 1
                    R = R - 1
                    while L < R and nums[L] == nums[L-1]:
                        L += 1
                else:
                    R = R - 1

        return res



