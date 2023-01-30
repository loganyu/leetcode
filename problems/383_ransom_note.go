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

func canConstruct(ransomNote string, magazine string) bool {
    count := make([]int, 26)
	for _, v := range magazine {
		count[v-'a']++
	}
	for _, v := range ransomNote {
		count[v-'a']--
		if count[v-'a'] < 0 {
			return false
		}
	}
	return true
}

