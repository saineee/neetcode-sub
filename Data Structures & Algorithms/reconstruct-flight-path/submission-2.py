class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}

        for src, dst in tickets:
            if src not in adj:
                adj[src] = []
            adj[src].append(dst)
        for src in adj:
            adj[src].sort(reverse=True)

        itinerary = []

        def dfs(src):
            while src in adj and adj[src]:
                dst = adj[src].pop()
                dfs(dst)

            itinerary.append(src)

        dfs("JFK")

        return itinerary[::-1]