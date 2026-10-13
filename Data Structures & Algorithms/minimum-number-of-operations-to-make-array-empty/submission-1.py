class Solution:
    def minOperations(self, nums: List[int]) -> int:
        frequency = {}
        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)

        res = 0
        for num, count in frequency.items():
            if count == 1:
                return -1
            
            if count == 2:
                res += 1
            elif count == 3:
                res += 1
            else:
                res += count//3
                remainder = count%3

                if remainder == 1:
                    res += 1
                elif remainder == 2:
                    res += 1

        return res