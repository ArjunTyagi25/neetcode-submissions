class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        digits[n-1] += 1
        carry = 0 if digits[n-1] != 10 else 1
        digits[n-1] = 0 if digits[n-1] == 10 else digits[n-1]

        for i in range(n-2, -1, -1):
            digits[i] += carry
            if digits[i] == 10:
                digits[i] = 0
                carry = 1
            else:
                carry = 0

        if carry == 1:
            digits.insert(0, carry)

        return digits
        