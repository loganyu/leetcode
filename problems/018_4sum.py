'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        mapping = collections.defaultdict(list)
        ans = set()
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                remaining = target - (nums[i] + nums[j])
                if remaining in mapping:
                    for pair in mapping[remaining]:
                        x, y = pair
                        if (i not in [x,y] and j not in [x, y]):
                            temp = [nums[i], nums[j], nums[x], nums[y]]
                            temp.sort()
                            ans.add(tuple(temp))
                            
                mapping[nums[i] + nums[j]].append((i, j))
                
        return list(ans)
        
