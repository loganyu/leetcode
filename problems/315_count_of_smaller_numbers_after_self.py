'''

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
'''

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge_sort(indexes):
            if len(indexes) <= 1:
                return indexes
            n = len(indexes)
            mid = n // 2
            left = merge_sort(indexes[:mid])
            right = merge_sort(indexes[mid:])
            for i in reversed(range(n)):
                if not right or left and nums[left[-1]] > nums[right[-1]]:
                    smaller[left[-1]] += len(right)
                    indexes[i] = left.pop()
                else:
                    indexes[i] = right.pop()
            
            return indexes
        
        smaller = [0] * len(nums)
        merge_sort(list(range(len(nums))))
        
        return smaller
            
