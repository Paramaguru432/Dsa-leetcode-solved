import heapq

class MedianFinder(object):

    def __init__(self):
        self.small = []   # max heap
        self.large = []   # min heap

    def addNum(self, num):

        heapq.heappush(self.small, -num)

        # Make sure every value in small <= every value in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            small_value = -heapq.heappop(self.small)
            large_value = heapq.heappop(self.large)

            heapq.heappush(self.small, -large_value)
            heapq.heappush(self.large, small_value)

        # Balance the sizes
        if len(self.small) > len(self.large) + 1:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        elif len(self.large) > len(self.small):
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    def findMedian(self):

        if len(self.small) > len(self.large):
            return float(-self.small[0])

        return (-self.small[0] + self.large[0]) / 2.0