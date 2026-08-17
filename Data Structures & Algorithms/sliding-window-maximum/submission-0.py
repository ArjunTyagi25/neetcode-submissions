class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = [[-nums[i], i] for i in range(k)]
        heapq.heapify(window)

        res = [-window[0][0]]
        L, R = 0, k

        while R != len(nums):
            L += 1
            heapq.heappush(window, [-nums[R], R])
            
            while window[0][1] < L:
                heapq.heappop(window)

            res.append(-window[0][0])
            R += 1

        return res


        