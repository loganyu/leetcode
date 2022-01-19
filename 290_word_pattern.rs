/*
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
*/

use std::collections::HashSet;

impl Solution {
    pub fn word_pattern(pattern: String, s: String) -> bool {
        if pattern.len() != s.split_whitespace().count() {
            return false;
        }
        
        const ASCII_LOWERCASE_BASE: usize = 97;
        let mut bindings: [Option<String>; 26] = Default::default();
        let mut used_words = HashSet::new();
        
        for (ch, word) in pattern.chars().zip(s.split_whitespace()) {
            let ch_idx = ch as usize - ASCII_LOWERCASE_BASE;
            match &bindings[ch_idx] {
                Some(binding) if binding != word => {
                    return false;
                },
                None if used_words.contains(word) => {
                    return false;
                }
                None => {
                    bindings[ch_idx] = Some(String::from(word));
                    used_words.insert(word);
                },
                _ => {}
            }
        }
        true
    }
}

