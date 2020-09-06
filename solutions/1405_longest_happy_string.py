'''
A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.

Given three integers a, b and c, return any string s, which satisfies following conditions:

s is happy and longest possible.
s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
s will only contain 'a', 'b' and 'c' letters.
If there is no such string s return the empty string "".

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 2, b = 2, c = 1
Output: "aabbc"
Example 3:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It's the only correct answer in this case.
 

Constraints:

0 <= a, b, c <= 100
a + b + c > 0
'''

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        sb = []
        size = a + b + c
        A = B = C = 0
        for i in range(size):
            if (a >= b and a >= c and A != 2) or (B == 2 and a > 0) or (C == 2 and a > 0):
                sb.append('a')
                a -= 1
                A += 1
                B = C = 0
            elif (b >= a and b >= c and B != 2) or (A == 2 and b > 0) or (C == 2 and b > 0):
                sb.append('b')
                b -= 1
                B += 1
                A = C = 0
            elif (c >= a and c >= b and C != 2) or (A == 2 and c > 0) or (B == 2 and c > 0):
                sb.append('c')
                c -= 1
                C += 1
                A = B = 0
        
        return "".join(sb)
        
