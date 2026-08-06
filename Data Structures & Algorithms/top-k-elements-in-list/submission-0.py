import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        largest = defaultdict(int)
        heap = []
        for n in nums:
                largest[n] += 1
        for number, count in largest.items():
            heapq.heappush(heap, (count, number))
            if len(heap) > k:
                heapq.heappop(heap)
        return [number for count, number, in heap]
        