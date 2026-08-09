class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_index_hash_map = {}

        for i in range(len(nums)):
            req_num = target - nums[i]

            if req_num in value_to_index_hash_map:
                return [value_to_index_hash_map[req_num], i]
            else:
                value_to_index_hash_map[nums[i]] = i 
        