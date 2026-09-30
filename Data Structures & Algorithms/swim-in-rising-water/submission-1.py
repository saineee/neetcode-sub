class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        grid_size = len(grid)
        visited = set()
        min_heap = [[grid[0][0], 0, 0]]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visited.add((0, 0))
        while min_heap:
            current_time, row, col = heapq.heappop(min_heap)
            
            if row == grid_size - 1 and col == grid_size - 1:
                return current_time
                
            for d_row, d_col in directions:
                neighbor_row, neighbor_col = row + d_row, col + d_col
                
                if (neighbor_row < 0 or neighbor_col < 0 or 
                    neighbor_row == grid_size or neighbor_col == grid_size or 
                    (neighbor_row, neighbor_col) in visited):
                    continue
                    
                visited.add((neighbor_row, neighbor_col))
                heapq.heappush(
                    min_heap, 
                    [max(current_time, grid[neighbor_row][neighbor_col]), neighbor_row, neighbor_col]
                )