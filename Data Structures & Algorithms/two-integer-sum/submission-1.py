class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_index = {}

        for i in range(len(nums)):
            req_num = target - nums[i]

            if req_num in val_to_index:
                return [val_to_index[req_num], i]
            else:
                val_to_index[nums[i]] = i

                
        