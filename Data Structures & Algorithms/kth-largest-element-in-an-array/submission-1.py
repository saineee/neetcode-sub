class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = nums[:k]
        heapq.heapify(minHeap)

        for num in nums[k:]:
            if num > minHeap[0]:
                heapq.heapreplace(minHeap, num)
        
        return minHeap[0]