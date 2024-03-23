/*
 * Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.



Example 1:

Input: s = "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:

Input: s = "aeiou"
Output: ""


Constraints:

1 <= s.length <= 1000
s consists of only lowercase English letters.
*/

class Solution {
    private boolean isVowel(char c) {
        return c == 'a' || c == 'i' || c == 'e' || c == 'o' || c == 'u';
    }

    public String removeVowels(String s) {
        StringBuffer ans = new StringBuffer(s.length());

        for (int i = 0; i < s.length(); i++) {
            if (!isVowel(s.charAt(i))) {
                ans.append(s.charAt(i));
            }
        }

        return ans.toString();
    }
}

