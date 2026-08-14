class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = defaultdict(int)
        res = []

        for num in nums:
            count[num] += 1

        for i in range(len(nums)):
            # Temporarily decrement the count of nums[i]
            count[nums[i]] -= 1
            # If i > 0 and nums[i] is same as nums[i-1], we continue to next i
            if i and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, len(nums)):
                # Temporarily decrement the count of nums[j]
                count[nums[j]] -= 1

                # If j - 1 > i (i.e., j and i are not the same) and nums[j] is same as nums[j-1], increment j
                if j - 1 > i and nums[j] == nums[j-1]:
                    continue

                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i+1, len(nums)):
                count[nums[j]] += 1

        return res


        
                


#       L            R
# [-4, -1, -1, 0, 1, 2]

