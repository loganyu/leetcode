'''
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
'''

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ranges = []
        prev = lower - 1
        nums.append(upper + 1)
        for num in nums:
            if num == prev + 2:
                ranges.append(f"{num-1}")
            elif num > prev + 2:
                ranges.append(f"{prev+1}->{num-1}")
            
            prev = num
        
        return ranges
    
