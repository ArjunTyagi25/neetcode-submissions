class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the nums array to set since we don't care about the location or repeated elements in the array
        nums_set = set(nums) 
        max_length = 0

        for num in nums_set:
            # If num-1 is not present, then it is a start of a sequence
            if num-1 not in nums_set: 
                cur_length = 0

                while (num+cur_length) in nums_set: 
                    # Calculate the length of the current sequence
                    cur_length += 1
                # Take the max of current sequence's length and max length
                max_length = max(cur_length, max_length)

        return max_length
        