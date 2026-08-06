class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if not num in seen:
                seen.add(num)
            else:
                return True
        return False