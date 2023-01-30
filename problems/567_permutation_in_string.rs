/*
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.

*/

impl Solution {
    pub fn check_inclusion(s1: String, s2: String) -> bool {
        let mut d1: [usize; 26] = [0; 26];
        let mut d2: [usize; 26] = [0; 26];
        for c in s1.chars() {
            d1[(c as u8 - b'a') as usize] += 1;
        }
        let s: &[u8] = s2.as_bytes();
        for (i, c) in s.iter().enumerate() {
            d2[(c - b'a') as usize] += 1;
            if i >= s1.len() {
                d2[(s[i - s1.len()] - b'a') as usize] -= 1
            }
            if d1 == d2 {
                return true;
            }
        }
        false
    }
}

