class Solution:
    def trap(self, height: List[int]) -> int:
        totalArea = 0

        for i in range(1, len(height)-1):
            left, right = i - 1, i + 1
            maxLeft, maxRight = 0, 0

            while left >= 0:
                maxLeft = max(maxLeft, height[left])
                left -= 1

            while right < len(height):
                maxRight = max(maxRight, height[right])
                right +=1

            area = min(maxLeft, maxRight) - height[i]

            if area > 0:
                totalArea += area
        
        return totalArea


