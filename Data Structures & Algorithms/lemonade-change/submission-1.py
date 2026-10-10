class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        billCount = {5: 0,
                     10: 0,
                     20: 0}

        for bill in bills:
            billCount[bill] += 1

            if bill > 5:
                # balance can either be 5 (if the customer gave $10) or 15 (if the customer gave $20)
                balance = bill - 5

                if balance == 5:
                    if billCount[5] > 0:
                        billCount[5] -= 1
                    else:
                        return False
                elif balance == 15:
                    if billCount[10] > 0 and billCount[5] > 0:
                        billCount[10] -= 1
                        billCount[5] -= 1
                    elif billCount[5] >= 3:
                        billCount[5] -= 3
                    else:
                        return False


        return True