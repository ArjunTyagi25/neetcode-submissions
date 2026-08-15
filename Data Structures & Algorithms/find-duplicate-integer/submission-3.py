class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                second_slow = 0

                while second_slow != slow:
                    slow = nums[slow]
                    second_slow = nums[second_slow]

                return slow



        