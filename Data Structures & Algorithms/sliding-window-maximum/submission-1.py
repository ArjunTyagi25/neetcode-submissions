class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        for i in range(k):
            # Pop from the back if the number is smaller than the current number
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

        for i in range(k, len(nums)):
            res.append(nums[q[0]])

            # Pop from the front if the index is out of the window’s range
            while q and q[0] <= i - k:
                q.popleft()

            # Pop from the back if the number is smaller than the current number
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

        res.append(nums[q[0]])

        return res


        