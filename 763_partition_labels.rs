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

impl Solution {
    pub fn partition_labels(s: String) -> Vec<i32> {
        let (mut v, mut l, mut r) = (vec![], 0, 0);

        let mut h = [0; 26];
        for (i, c) in s.chars().enumerate() {
            h[c as usize - 'a' as usize] = i;
        }

        for (i, c) in s.chars().enumerate() {
            r = std::cmp::max(r, h[c as usize - 'a' as usize]);
            if i == r { 
                v.push((r - l + 1) as i32);
                l = r + 1
            }
        }
        v
    }
}

