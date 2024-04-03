/*
 * Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.



Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true


Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
*/

impl Solution {
    pub fn is_isomorphic(s: String, t: String) -> bool {
        use std::collections::{HashSet, HashMap};
		let mut seen = HashSet::new();
		let mut mappings = HashMap::new();
		s.chars().zip(t.chars()).all(|(s, t)| {
			*mappings.entry(t).or_insert_with(|| Some(s).filter(|s| seen.insert(*s))) == Some(s)
		})
    }
}

