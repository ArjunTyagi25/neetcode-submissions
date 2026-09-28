class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False

        per_subset_target_sum = total_sum // k
        per_subset_sum = [0] * k
        nums.sort(reverse=True)
        memo = {}

        def rec(i, per_subset_sum):
            if i == len(nums):
                return True

            if (i, tuple(sorted(per_subset_sum))) in memo:
                return memo[(i, tuple(sorted(per_subset_sum)))]

            for j in range(k):
                if per_subset_sum[j] + nums[i] <= per_subset_target_sum:
                    per_subset_sum[j] += nums[i]
                    if rec(i+1, per_subset_sum):
                        memo[(i, tuple(sorted(per_subset_sum)))] = True
                        return True
                    per_subset_sum[j] -= nums[i]
            
            memo[(i, tuple(sorted(per_subset_sum)))] = False
            return False

        return rec(0, per_subset_sum)
            