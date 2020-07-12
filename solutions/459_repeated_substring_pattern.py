'''
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
'''

# KMP. O(N) time and O(N) space
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        dp = [0] * n
        for i in range(1, n):
            j = dp[i-1]
            while j > 0 and s[i] != s[j]:
                j = dp[j-1]
            if s[i] == s[j]:
                j += 1
            dp[i] = j
        l = dp[n-1]
        
        return l != 0 and n % (n-l) == 0
        
# Rabin-Karp. O(N*sqrt(N)) time and O(sqrt(N)) space
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n < 2:
            return False
        if n == 2:
            return s[0] == s[1]
    
        for i in reversed(range(1, int(n**0.5)+1)):
            print(i)
            if n % i == 0:
                divisors = [i]
                if i != 1:
                    divisors.append(n // i)
                for l in divisors:
                    first_hash = curr_hash = hash(s[:l])
                    start = l
                    while start != n and curr_hash == first_hash:
                        curr_hash = hash(s[start:start + l])
                        start += l
                    if start == n and curr_hash == first_hash:
                        return True
        return False

# Concatination. O(N^2) time and O(n) space
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        double = s * 2
        return s in double[1:-1]

