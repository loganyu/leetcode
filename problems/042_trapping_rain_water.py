'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        left_max = [None]*n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
        right_max = [None]*n
        right_max[-1] = height[-1]
        for j in reversed(range(0, n-1)):
            right_max[j] = max(right_max[j+1], height[j])
        ans = 0
        for i in range(0,n):
            ans += min(left_max[i], right_max[i]) - height[i]
        
        return ans

# one pass solution
class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = right_max = 0
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1 
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        
        return ans
    
