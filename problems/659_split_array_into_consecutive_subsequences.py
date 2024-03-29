'''
Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

 

Example 1:

Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5

Example 2:

Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5

Example 3:

Input: [1,2,3,4,4,5]
Output: False
 

Constraints:

1 <= nums.length <= 10000
'''

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = Counter(nums)
        tails = Counter()
        for num in nums:
            if count[num] == 0:
                continue
            count[num] -= 1
            if tails[num-1] > 0:
                tails[num-1] -= 1
                tails[num] += 1
            elif count[num+1] > 0 and count[num+2] > 0:
                count[num+1] -= 1
                count[num+2] -= 1
                tails[num+2] += 1
            else:
                return False
        
        return True
        
