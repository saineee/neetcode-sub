import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mostFreq = defaultdict(int)
        heap = []
        for n in nums:
            mostFreq[n] += 1
        for number, count in mostFreq.items():
            heapq.heappush(heap, (count, number))
            if len(heap) > k:
                heapq.heappop(heap)
        return [number for _, number in heap]