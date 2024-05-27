/*
 * Given a pattern and a string s, return true if s matches the pattern.

A string s matches a pattern if there is some bijective mapping of single characters to non-empty strings such that if each character in pattern is replaced by the string it maps to, then the resulting string is s. A bijective mapping means that no two characters map to the same string, and no character maps to two different strings.



Example 1:

Input: pattern = "abab", s = "redblueredblue"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "red"
'b' -> "blue"
Example 2:

Input: pattern = "aaaa", s = "asdasdasdasd"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "asd"
Example 3:

Input: pattern = "aabb", s = "xyzabcxzyabc"
Output: false


Constraints:

1 <= pattern.length, s.length <= 20
pattern and s consist of only lowercase English letters.
*/

class Solution {
    public boolean wordPatternMatch(String pattern, String s) {
        Map<Character, String> symbolMap = new HashMap<>();
        Set<String> wordSet = new HashSet<>();

        return isMatch(s, 0, pattern, 0, symbolMap, wordSet);
    }

    private boolean isMatch(String s, int sIndex, String pattern, int pIndex, Map<Character, String> symbolMap,
            Set<String> wordSet) {
        if (pIndex == pattern.length()) {
            return sIndex == s.length();
        }
        char symbol = pattern.charAt(pIndex);
        if (symbolMap.containsKey(symbol)) {
            String word = symbolMap.get(symbol);
            if (!s.startsWith(word, sIndex)) {
                return false;
            }
            return isMatch(s, sIndex + word.length(), pattern, pIndex + 1, symbolMap, wordSet);
        }
        for (int k = sIndex + 1; k <= s.length(); k++) {
            String newWord = s.substring(sIndex, k);
            if (wordSet.contains(newWord)) {
                continue;
            }
            symbolMap.put(symbol, newWord);
            wordSet.add(newWord);
            if (isMatch(s, k, pattern, pIndex + 1, symbolMap, wordSet)) {
                return true;
            }
            symbolMap.remove(symbol);
            wordSet.remove(newWord);
        }
        return false;
    }
}

