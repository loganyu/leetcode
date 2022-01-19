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

func wordPattern(pattern string, s string) bool {
    codes := make(map[string]byte)
    used := make([]bool, 26)
    words := strings.Split(s, " ")
    if len(pattern) != len(words) {
        return false
    }
    for i, word := range words {
        code, ok := codes[word]
        if !ok {
            if used[pattern[i] - 'a'] {
                return false
            }
            used[pattern[i] - 'a'] = true
            codes[word] = pattern[i]
            continue
        }
        if code != pattern[i] {
            return false
        }
    }
    
    return true
}

