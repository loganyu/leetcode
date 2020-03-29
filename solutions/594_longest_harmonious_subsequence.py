'''
We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:

Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
 

Note: The length of the input array will not exceed 20,000.
'''

from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        res = 0
        count_by_num = Counter(nums)
        for num, count in count_by_num.items():
            if num + 1 in count_by_num:
                res = max(res, count_by_num[num] + count_by_num[num+1])
        
        return res
        
