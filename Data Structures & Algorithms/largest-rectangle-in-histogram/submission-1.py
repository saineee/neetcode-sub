class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        best = 0
        n = len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                popped = stack.pop()
                height = heights[popped]
                if not stack:
                    left = -1
                else:
                    left = stack[-1]
                width = i - left - 1
                area = height * width
                best = max(best, area)
            stack.append(i)

        while stack:
            popped = stack.pop()
            height = heights[popped]
            if not stack: 
                left = -1
            else:
                left = stack[-1]
            width = n - left - 1
            area = width * height
            best = max(best, area)
        return best