/*
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
*/

func partitionLabels(s string) []int {
    start := 0
    end := 0
    res := []int{}
    lastIndex := make([]int, 26)
    for i, c := range s {
        lastIndex[c - 'a'] = i
    }
    for i, c := range s {
        end = max(end, lastIndex[c - 'a'])
        if i == end {
            res = append(res, end - start + 1)
            start = end + 1
        }
    }
    return res
}

func max(a, b int) int {
    if a > b { return a }
    return b
}

