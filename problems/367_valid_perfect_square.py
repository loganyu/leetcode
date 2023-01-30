'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left, right = 2, num // 2
        while left <= right:
            x = left + (right - left) // 2
            guess = x**2
            if guess == num:
                return x
            elif guess > num:
                right = x - 1
            else:
                left = x + 1 
        
        return False

