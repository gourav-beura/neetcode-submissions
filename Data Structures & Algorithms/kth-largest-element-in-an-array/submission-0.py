class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        for i,num in enumerate(nums):
            heapq.heappush(heap, (-num,i))
        
        res = 0
        for i in range(k):
            res = -1*heapq.heappop(heap)[0]
        
        return res

        