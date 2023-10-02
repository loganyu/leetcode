/*
 * Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.



Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"


Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
*/

impl Solution {
    pub fn reverse_words(s: String) -> String {
        let mut chars: Vec<char> = s.chars().collect();
        let mut start = 0;

        for i in 0..chars.len() {
            if chars[i] == ' ' || i == chars.len() - 1 {
                let mut end = if i == chars.len() - 1 && chars[i] != ' ' { i + 1 } else { i };
                while start < end {
                    chars.swap(start, end - 1);
                    start += 1;
                    end -= 1;
                }
                start = i + 1;
            }
        }

        chars.iter().collect()
    }
}

