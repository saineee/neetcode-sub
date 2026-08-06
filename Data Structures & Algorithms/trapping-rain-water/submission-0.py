class Solution:
    def trap(self, height: List[int]) -> int:    
        #get max_left
        max_left = [0] * len(height)
        current_max = 0
        for i in range(len(height)):
            max_left[i] = current_max
            current_max = max(current_max, height[i])
        
        # get max_right
        max_right = [0] * len(height)
        current_max = 0
        for i in range(len(height) - 1, -1, -1):
            max_right[i] = current_max
            current_max = max(current_max, height[i])
        
        # start iterating through list
        total = 0
        for i in range(len(height)):
            lowest = min(max_right[i], max_left[i])
            rainwater = lowest-height[i]
            if rainwater > 0:
                total += rainwater
        return total