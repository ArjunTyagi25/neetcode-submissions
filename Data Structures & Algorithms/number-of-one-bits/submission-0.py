class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]
        res = 0

        for i in range(len(binary)):
            if binary[i] == "1":
                res += 1

        return res
        