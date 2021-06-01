'''
Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104
'''

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - k
        while l < r:
            m = l + (r - l) // 2
            if arr[m] == arr[m+k]:
                if arr[m] == x:
                    return arr[m:m+k]
                if arr[m] > x:
                    r = m
                else:
                    l = m + 1
            elif abs(arr[m] - x) > abs(arr[m+k] - x):
                l = m + 1
            else:
                r = m

        return arr[l:l+k]
