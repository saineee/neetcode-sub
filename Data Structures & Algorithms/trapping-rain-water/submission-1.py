class Solution:
    def trap(self, height: List[int]) -> int:    
        left_max = 0
        right_max = 0
        left = 0
        right = len(height) - 1
        total = 0
        while left <= right:
            if left_max < right_max:
                left_max = max(height[left], left_max)
                total += left_max - height[left]
                left += 1
            else:
                right_max = max(height[right], right_max)
                total += right_max - height[right]
                right -= 1
        return total