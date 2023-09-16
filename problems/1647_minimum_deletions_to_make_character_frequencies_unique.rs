/*
 * A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.



Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.
Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
Example 3:

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).


Constraints:

1 <= s.length <= 105
s contains only lowercase English letters.
*/

use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    pub fn min_deletions(s: String) -> i32 {
        let mut cnt = HashMap::new();
        let mut deletions = 0;
        let mut used_frequencies = HashSet::new();

        for c in s.chars() {
            *cnt.entry(c).or_insert(0) += 1;
        }

        for freq in cnt.values() {
            let mut f = *freq;
            while f > 0 && used_frequencies.contains(&f) {
                f -= 1;
                deletions += 1;
            }
            used_frequencies.insert(f);
        }

        deletions
    }
}

