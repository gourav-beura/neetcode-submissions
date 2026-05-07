class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = [-stone for stone in stones]
        heapq.heapify(self.heap)

        while len(self.heap) > 1:
            print(self.heap)
            x = -1*heapq.heappop(self.heap)
            y = -1*heapq.heappop(self.heap)

            if x<y:
                diff = y-x
            elif x>y:
                diff = x-y
            else:
                diff = 0
            heapq.heappush(self.heap, -1*diff)
        
        return -heapq.heappop(self.heap)
        
        