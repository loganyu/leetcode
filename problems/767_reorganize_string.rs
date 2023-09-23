/*
 * Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.



Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""


Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
*/

use std::collections::HashMap;

impl Solution {
    pub fn reorganize_string(s: String) -> String {
        let mut freq_map: HashMap<char, usize> = HashMap::new();
        for c in s.chars() {
            *freq_map.entry(c).or_insert(0) += 1;
        }

        let mut sorted_chars: Vec<char> = freq_map.keys().cloned().collect();
        sorted_chars.sort_by_key(|&c| std::cmp::Reverse(freq_map[&c]));

        if freq_map[&sorted_chars[0]] > (s.len() + 1) / 2 {
            return "".to_string();
        }

        let mut res = vec![' '; s.len()];
        let mut i = 0;
        for &c in sorted_chars.iter() {
            for _ in 0..freq_map[&c] {
                if i >= s.len() {
                    i = 1;
                }
                res[i] = c;
                i += 2;
            }
        }

        res.iter().collect()
    }
}

