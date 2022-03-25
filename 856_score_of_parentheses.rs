/*
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: s = "()"
Output: 1
Example 2:

Input: s = "(())"
Output: 2
Example 3:

Input: s = "()()"
Output: 2
 

Constraints:

2 <= s.length <= 50
s consists of only '(' and ')'.
s is a balanced parentheses string.
*/

impl Solution {
    pub fn score_of_parentheses(s: String) -> i32 {
        let mut ans = 0;
        let mut bal = 0;
        
        for (i, chr) in s.chars().enumerate(){
            match chr{
                '(' => bal += 1,
                _ => {
                    bal -= 1;
                    if s.as_bytes()[i-1] == b'('{
                        ans += 1 << bal; 
                    }
                }
            }
        }
        ans
    }
}

