class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for source, destination, weight in times:
            graph[source].append((destination, weight))

        min_heap = [(0, k)]
        visited = set()
        total_time = 0

        while min_heap:
            current_time, node = heapq.heappop(min_heap)

            if node in visited:
                continue

            visited.add(node)
            total_time = max(total_time, current_time)

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (current_time + weight, neighbor))

        return total_time if len(visited) == n else -1