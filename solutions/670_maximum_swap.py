'''
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
'''

class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(map(int, str(num)))
        max_ = digits[-1]
        l = -1
        r = max_i = len(digits) - 1
        for i in reversed(range(len(digits) - 1)):
            if digits[i] > max_:
                max_ = digits[i]
                max_i = i
            elif digits[i] < max_:
                l = i
                r = max_i
        if l != -1:
            digits[l], digits[r] = digits[r], digits[l]
        
        return int("".join(map(str, digits)))
       
