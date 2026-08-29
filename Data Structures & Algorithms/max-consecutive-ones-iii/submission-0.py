class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        flipped_count = 0
        flipped_indices = []
        L = 0
        res = 0

        for R in range(len(nums)):
            if nums[R] == 0:
                if flipped_count < k:
                    nums[R] = 1
                    flipped_indices.append(R)
                    flipped_count += 1
                else:
                    while L <= R and flipped_count >= k:
                        if L in flipped_indices:
                            nums[L] = 0
                            flipped_indices.remove(L)
                            flipped_count -= 1
                        L += 1

                    nums[R] = 1
                    flipped_indices.append(R)
                    flipped_count += 1

            res = max(res, R - L + 1)

        return res
        