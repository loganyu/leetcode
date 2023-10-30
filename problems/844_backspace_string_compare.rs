/*
 * Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.



Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.


Follow up: Can you solve it in O(n) time and O(1) space?
*/

impl Solution {
    pub fn backspace_compare(s: String, t: String) -> bool {
        let mut a = vec![];
        for c in s.bytes() {
            if c == b'#' {
                a.pop();
            } else {
                a.push(c);
            }
        }
        let mut b = vec![];
        for c in t.bytes() {
            if c == b'#' {
                b.pop();
            } else {
                b.push(c);
            }
        }
        a == b
    }
}

