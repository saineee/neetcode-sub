class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers) - 1
        left = 0
        while left < right:
            if target < numbers[left] + numbers[right]:
                right -= 1
            elif target > numbers[left] + numbers[right]:
                left += 1
            else:
                return[left+1, right+1]