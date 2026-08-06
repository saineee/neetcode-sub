class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        count = 0
        longest = 0
        for n in nums:
            if n-1 not in nums:
                count = 0
                while n in nums:
                    count += 1
                    n += 1
            if count > longest:
                longest = count
        return longest
