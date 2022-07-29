/*
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
*/

func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }
    counter := make(map[rune]int)
    for _, v := range s {
        counter[v]++
    }
    for _, v := range t {
        counter[v]--
    }
    for _, v := range counter {
        if v != 0 {
            return false
        }
    }
    return true
}

