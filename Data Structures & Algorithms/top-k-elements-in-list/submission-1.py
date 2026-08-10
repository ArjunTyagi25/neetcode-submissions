class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = {}  # num as key, count as value
        count_to_num = [[] for i in range(len(nums)+1)] # each index represents the frequency

        for i in range(len(nums)):
            if nums[i] in num_to_count:
                num_to_count[nums[i]] += 1
            else:
                num_to_count[nums[i]] = 1    
    
        for num in num_to_count:
            count_to_num[num_to_count[num]].append(num)

        res = []
        count = 0

        for i in range(len(count_to_num)-1, -1, -1):
            if count_to_num[i] is not []:
                for num in count_to_num[i]:
                    res.append(num)
                    count += 1

                    if (count == k):
                        return res
        