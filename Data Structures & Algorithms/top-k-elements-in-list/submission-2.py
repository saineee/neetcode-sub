class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mostFrequent = defaultdict(int)
        heap = []
        for n in nums:
            mostFrequent[n] += 1
        for num, count in mostFrequent.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for _, num in heap]