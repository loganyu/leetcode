/*
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
*/

func isValid(s string) bool {
    seen := map[rune]rune{
        ')' : '(',
        ']' : '[',
        '}' : '{',
    }
    
    stk := []rune{}
    
    for _, i := range s {
        if i == ')' || i == '}' || i == ']' {
            if len(stk) > 0 && seen[i] == stk[len(stk) - 1] {
                stk = stk[: len(stk) - 1]
                continue
            }
        }
        
        stk = append(stk, i)
    }
    
    return len(stk) == 0
}

