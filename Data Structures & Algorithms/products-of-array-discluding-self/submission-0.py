class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        n = len(nums)
        
        left = 1
        for i in range(n):
            output[i] *= left
            left *= nums[i]

        right = 1
        for i in range(n-1, -1, -1):
            output[i] *= right
            right *= nums[i]
        
        return output