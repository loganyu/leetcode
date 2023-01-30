/*
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
*/

func checkInclusion(s1 string, s2 string) bool {
	length1 := len(s1)
	length2 := len(s2)
	if length1 > length2  {
		return false
	}

	array1 := [128]int{}
	array2 := [128]int{}

	for i := 0; i < length1; i++ {
		array1[s1[i]]++
		array2[s2[i]]++
	}
	if array1 == array2 {
		return true
	}

	for i := length1; i < length2; i++ {
		array2[s2[i]]++;
		array2[s2[i-length1]]--
		if array1 == array2 {
			return true
		}
	}
    return false
}

