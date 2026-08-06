class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        have = 0
        need = Counter(t)
        min_sub = ""
        required = len(need)
        window_count = defaultdict(int)
        for right in range(len(s)):
            window_count[s[right]] += 1
            if s[right] in need and window_count[s[right]] == need[s[right]]:
                have += 1
            while required == have:
                if min_sub == "" or (right - left + 1) < len(min_sub):
                    min_sub = s[left:right+1]
                if s[left] in need and window_count[s[left]] == need[s[left]]:
                    have -= 1
                window_count[s[left]] -= 1
                left += 1
        return min_sub