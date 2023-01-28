# Frist Try
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, length = 0, len(height) - 1, 0
        volume = 0

        while left < right:
            length = right - left
            if height[left] <= height[right]:
                volume = max(volume, height[left]*length)
                left += 1
            else:
                volume = max(volume, height[right]*length)
                right -= 1

        return volume
    
    
# Second Try
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area, left, right = 0, 0, len(height) - 1

        while left < right:
            cur_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, cur_area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area