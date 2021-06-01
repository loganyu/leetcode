'''
Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

 

Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: 
The first missing number is 5.
Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation: 
The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation: 
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
 

Note:

1 <= A.length <= 50000
1 <= A[i] <= 1e7
1 <= K <= 1e8
'''

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        missing = lambda idx: nums[idx] - nums[0] - idx
        n = len(nums)
        if k > missing(n-1):
            return nums[n-1] + k - missing(n-1)
        idx = 1
        while missing(idx) < k:
            idx += 1
        
        return nums[idx-1] + k - missing(idx-1)
        
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        missing = lambda idx: nums[idx] - nums[0] - idx
        n = len(nums)
        if k > missing(n-1):
            return nums[n-1] + k - missing(n-1)
        idx = 1
        
        l = 0
        r = n - 1
        while l < r:
            pivot = l + (r - l) // 2
            if missing(pivot) < k:
                l = pivot + 1
            else:
                r = pivot
        
        return nums[l-1] + k - missing(l-1)
        
