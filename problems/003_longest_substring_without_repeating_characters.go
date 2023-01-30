/*
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
*/

func lengthOfLongestSubstring(s string) int {
    if len(s) <= 1 {return len(s)}
    lo, hi, ans := 0, 0, 1.0
    m := make(map[byte]bool)

    for hi < len(s) {
        c := s[hi]
        hi++
        for lo < hi {
            if _, present := m[c]; !present {break}
            lowC := s[lo]
            lo++
            delete(m, lowC)
        }
        m[c] = true
        ans = math.Max(ans, float64(hi - lo))
    }
    return int(ans)
}

