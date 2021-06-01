'''
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

 

Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.
 

Constraints:

1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
'''

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        sol = []
        i = j = k = 0
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            min_val = min(arr1[i], arr2[j], arr3[k])
            if arr1[i] == arr2[j] == arr3[k]:
                sol.append(arr1[i])
            if arr1[i] == min_val:
                i += 1
            if arr2[j] == min_val:
                j += 1
            if arr3[k] == min_val:
                k += 1
        
        return sol

