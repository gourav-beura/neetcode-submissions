class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        heapq.heapify(heap)


        lookUp = Counter(nums)

        for num in lookUp:
            heapq.heappush(heap,(-lookUp[num],num))

        print(heap)
        res = []
        for i in range(k):
            val = heapq.heappop(heap)[1]
            res.append(val)
        return res
        