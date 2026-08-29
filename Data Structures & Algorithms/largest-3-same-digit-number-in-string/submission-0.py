class Solution:
    def largestGoodInteger(self, num: str) -> str:
        nums = []
        l = 0

        for r in range(3, len(num) + 1):
            nums.append(num[l:r])
            l += 1
        
        res_num = float('-inf')
        res = ""
        for n in nums:
            if n[0] == n[1] == n[2] and int(n) > res_num:
                res_num = int(n)
                res = n

        return res
        