class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       left = 0
       seen = set()
       max_len = 0
       for right in range(len(s)):
           if s[right] not in seen:
              seen.add(s[right])
           else:
              while s[right] in seen:
                 seen.remove(s[left])
                 left += 1
              seen.add(s[right])
           max_len = max(max_len, right - left + 1)
       return max_len