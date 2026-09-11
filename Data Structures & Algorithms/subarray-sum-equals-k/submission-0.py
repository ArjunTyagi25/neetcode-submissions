class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_freq = {0 : 1}
        cur_prefix = 0
        res = 0
        
        for i in range(len(nums)):
            cur_prefix += nums[i]
            req_prefix = cur_prefix - k

            if req_prefix in prefix_freq:
                res += prefix_freq[req_prefix]

            prefix_freq[cur_prefix] = 1 + prefix_freq.get(cur_prefix, 0)

        return res




        '''
        prefix[j] - prefix[i] = k --> subarray from i+1 to j
        at any index j, if we can find
        '''
        