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

impl Solution {
    pub fn valid_palindrome(s: String) -> bool {
        Self::helper(&s.as_bytes(), true)
    }

    fn helper(chars: &[u8], can_skip: bool) -> bool {
        if chars.len() == 0 || chars.len() == 1 {
            return true;
        }

        let mut i = 0;
        let mut j = chars.len() - 1;
        while i <= j {
            if chars[i] == chars[j] {
                i += 1;
                j -= 1;
                continue;
            }
            if !can_skip {
                return false;
            }
            if Self::helper(&chars[(i + 1)..=j], false) {
                return true;
            } else if Self::helper(&chars[i..=(j - 1)], false) {
                return true;
            } else {
                return false;
            }
        }
        true
    }
}

