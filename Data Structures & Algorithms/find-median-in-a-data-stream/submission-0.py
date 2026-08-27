class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

        heapq.heapify(self.max_heap)
        heapq.heapify(self.min_heap)
        

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == 0:
            heapq.heappush(self.min_heap, num)

        else:
            if num > self.min_heap[0]:
                heapq.heappush(self.min_heap, num)

                while len(self.min_heap) - len(self.max_heap) > 1:
                    val = self.min_heap[0]
                    heapq.heappop(self.min_heap)

                    heapq.heappush(self.max_heap, -val)
            else:
                heapq.heappush(self.max_heap, -num)

                while len(self.max_heap) - len(self.min_heap) > 1:
                    val = self.max_heap[0]
                    heapq.heappop(self.max_heap)

                    heapq.heappush(self.min_heap, -val)

        

        

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        elif len(self.max_heap) < len(self.min_heap):
            return self.min_heap[0]
        else:
            m = (self.min_heap[0] + (-self.max_heap[0]))/2
            return m