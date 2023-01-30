/*
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

 

Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false
 

Constraints:

1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
*/

impl Solution {
    pub fn detect_capital_use(word: String) -> bool {
        let v: Vec<char> = word.chars().collect();
        if v[0].is_lowercase() {
            return v.iter().all(|&c| c.is_lowercase());
        }
        if v.len() > 1 {
            let b = v[1].is_lowercase();
            return v.iter().skip(1).all(|&c| c.is_lowercase() == b);
        }
        true
    }
}

