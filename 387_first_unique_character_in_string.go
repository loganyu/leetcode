/*
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
*/

func firstUniqChar(s string) int {
    counts := make([]int, 26)
    for _, v := range s {
        counts[v - 'a']++
    }
    for i, v := range s {
        if counts[v - 'a'] == 1 {
            return i
        }
    }

    return -1
}
