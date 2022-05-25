/*
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
*/

func longestValidParentheses(s string) int {
    max := 0
    l := 0
    r := 0
    for i := 0; i < len(s); i++ { 
        if s[i] == '(' { l++ }
        if s[i] == ')' { r++ }
        if r > l {
            r = 0
            l = 0
        } else if r == l {
            if r + l > max {
                max = r + l
            }
        }
    }
    l = 0
    r = 0
    for i := len(s)-1; i >= 0; i-- { 
        if s[i] == ')' { l++ }
        if s[i] == '(' { r++ }
        if r > l {
            r = 0
            l = 0
        } else if r == l {
            if r + l > max {
                max = r + l
            }
        }
    }
    return max
}

