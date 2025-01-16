'''
Given a digit string s, return the number of unique substrings of s where every digit appears the same number of times.


Example 1:

Input: s = "1212"
Output: 5
Explanation: The substrings that meet the requirements are "1", "2", "12", "21", "1212".
Note that although the substring "12" appears twice, it is only counted once.
Example 2:

Input: s = "12321"
Output: 9
Explanation: The substrings that meet the requirements are "1", "2", "3", "12", "23", "32", "21", "123", "321".


Constraints:

1 <= s.length <= 1000
s consists of digits.
'''

class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        n = len(s)
        valid_substrings = set()
        for start in range(n):
            digit_frequency = [0] * 10
            for end in range(start, n):
                digit_frequency[ord(s[end]) - ord("0")] += 1
                common_frequency = 0
                is_valid = True
                for count in digit_frequency:
                    if count == 0:
                        continue
                    if common_frequency == 0:
                        common_frequency = count
                    if common_frequency != count:
                        is_valid = False
                        break

                if is_valid:
                    substring = s[start : end + 1]
                    valid_substrings.add(substring)

        return len(valid_substrings)


