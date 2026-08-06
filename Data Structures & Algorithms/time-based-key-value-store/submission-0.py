class TimeMap:

    def __init__(self):
        self.entries = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.entries[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.entries:
            return ""
        
        lst = self.entries[key]
        left = 0
        right = len(lst) - 1
        result = ""
        while left <= right:
            mid = left + (right - left) // 2
            
            if lst[mid][0] <= timestamp:
                result = lst[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return result