/*
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
*/

impl Solution {
    pub fn can_construct(ransom_note: String, magazine: String) -> bool {
        let mut count: [usize; 256] = [0; 256];
        for c in magazine.chars().map(|c| (c as u8) as usize) {
            count[c] += 1;
        }
        for c in ransom_note.chars().map(|c| (c as u8) as usize) {
            if count[c] == 0 {
                return false;
            }
            count[c] -= 1;
        }
        true
    }
}

