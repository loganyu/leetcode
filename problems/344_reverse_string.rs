/*
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
*/

impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
        let mut left : usize = 0;
        let mut right : usize = s.len() - 1;

        while left < right {
          s.swap(left, right);
          left += 1;
          right -= 1;
        }
    }
}

