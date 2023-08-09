/*
 * Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
*/

impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
        let n = s.len();
        let mut dp = vec![false; n + 1];
        dp[0] = true;
        let max_len = word_dict.iter().map(|word| word.len()).max().unwrap_or(0);

        let word_dict: std::collections::HashSet<String> = word_dict.into_iter().collect();

        for i in 1..=n {
            for j in (std::cmp::max(i as isize - max_len as isize - 1, 0) as usize..i).rev() {
                if dp[j] && word_dict.contains(&s[j..i].to_string()) {
                    dp[i] = true;
                    break;
                }
            }
        }

        dp[n]
    }
}

