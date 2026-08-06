class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        best = 0
        while left < right:
            if heights[left] < heights[right]:
                max_area = (right-left) * heights[left]
                left += 1
            elif heights[left] > heights[right]:
                max_area = (right-left) * heights[right]
                right -= 1
            else: #if even vals
                max_area = (right-left) * heights[left]
                left += 1
            best = max(max_area, best)
        return best
            