/*
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
*/

func validPalindrome(s string) bool {
    
    l := 0
    r := len(s)-1
    
    for l < r {
        if s[l] != s[r] {
            return helper(s, l+1, r) || helper(s, l, r-1)
        } else {
            l++
            r--
        }
    }
    return true
}

func helper(s string, l, r int) bool {
    for l < r {
        if s[l] != s[r] { return false }
        l++
        r--
    }
    return true
}

