/*
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

 

Example 1:

Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
Example 2:

Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
Example 3:

Input: n = 33
Output: 66045
 

Constraints:

1 <= n <= 50
*/

func countVowelStrings(n int) int {
    dp := make([][5]int, n + 1)
    
    for i := 0; i < 5; i++ {
        dp[0][i] = 1
    }
    
    for i := 1; i < n; i++ {
        for j := 0; j < 5; j++ {
            for k := j; k < 5; k++ {
                dp[i][j] += dp[i-1][k]
            }
        }
    }
    
    ans := 0
    for i := 0; i < 5; i++ {
        ans += dp[n-1][i]
    }
    
    return ans
}

