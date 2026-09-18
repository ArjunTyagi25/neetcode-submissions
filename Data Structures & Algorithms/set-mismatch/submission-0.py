class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = [0] * (len(nums)+1)

        for num in nums:
            count[num] += 1

        res = [-1, -1]
        for i in range(1, len(count)):
            if count[i] == 2:
                res[0] = i
            if count[i] == 0:
                res[1] = i

        return res
        