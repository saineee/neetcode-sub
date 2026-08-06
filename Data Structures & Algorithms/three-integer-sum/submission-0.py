class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        found_nums = []
        nums_s = sorted(nums)
        n = len(nums)-1
        for i in range(len(nums)-2):
            if i > 0 and nums_s[i] == nums_s[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums_s[left]+nums_s[right]+nums_s[i] < target:
                    left += 1
                elif nums_s[left]+nums_s[right]+nums_s[i] > target:
                    right -= 1
                elif target == (nums_s[right]+nums_s[left]+nums_s[i]):
                    found_nums.append([nums_s[right],nums_s[left],nums_s[i]])
                    left += 1
                    right -= 1
                    while left < right and nums_s[left] == nums_s[left-1]:
                        left += 1
                    while left < right and nums_s[right] == nums_s[right+1]:
                        right -= 1
        return found_nums