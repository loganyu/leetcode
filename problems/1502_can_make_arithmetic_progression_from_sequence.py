'''
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.



Example 1:

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
Example 2:

Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.


Constraints:

2 <= arr.length <= 1000
-106 <= arr[i] <= 106
'''

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        min_value, max_value = min(arr), max(arr)
        n = len(arr)
        if max_value - min_value == 0:
            return True
        if (max_value - min_value) % (n - 1) != 0:
            return False
        diff = (max_value - min_value) // (n - 1)
        number_set = set()
        for num in arr:
            if (num - min_value) % diff != 0:
                return False
            number_set.add(num)

        return len(number_set) == n

