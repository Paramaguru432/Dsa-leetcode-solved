class Solution(object):
    def findKthLargest(self, nums, k):
        import heapq
        heap=[]
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]        
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        