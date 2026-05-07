class Solution:
    def distance(self, p1, p2):
        return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.heap = []
        heapq.heapify(self.heap)

        for i,point in enumerate(points):
            x,y = point
            dist = self.distance([0,0],[x,y])
            heapq.heappush(self.heap,(dist,i))
        
        result = []
        for i in range(k):
            dist, idx = heapq.heappop(self.heap)
            result.append(points[idx])
        return result


        