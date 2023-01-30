'''
Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome.

Given two positive integers left and right represented as strings, return the number of super-palindromes integers in the inclusive range [left, right].

 

Example 1:

Input: left = "4", right = "1000"
Output: 4
Explanation: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
Example 2:

Input: left = "1", right = "2"
Output: 1
 

Constraints:

1 <= left.length, right.length <= 18
left and right consist of only digits.
left and right cannot have leading zeros.
left and right represent integers in the range [1, 1018].
left is less than or equal to right.
'''

ass Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left, right = int(left), int(right)
        
        def reverse(x):
            ans = 0
            while x:
                ans = 10 * ans + x % 10
                x //= 10
                
            return ans
        
        def is_palindrome(x):
            return x == reverse(x)
        
        ans = 0
        for k in range(100_000):
            s = str(k)
            t = s + s[-2::-1]
            v = int(t) ** 2
            if v > right:
                break
            if v >= left and is_palindrome(v):
                ans += 1
        
        for k in range(100_000):
            s = str(k)
            t = s + s[::-1]
            v = int(t) ** 2
            if v > right:
                break
            if v >= left and is_palindrome(v):
                ans += 1
        
        return ans
        
