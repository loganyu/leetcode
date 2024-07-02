'''
An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
Any student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.



Example 1:

Input: n = 2
Output: 8
Explanation: There are 8 records with length 2 that are eligible for an award:
"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).
Example 2:

Input: n = 1
Output: 3
Example 3:

Input: n = 10101
Output: 183236316


Constraints:

1 <= n <= 105
'''

class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 1000000007
        dp_curr_state = [[0] * 3 for _ in range(2)]
        dp_next_state = [[0] * 3 for _ in range(2)]
        dp_curr_state[0][0] = 1
        for _ in range(n):
            for total_absences in range(2):
                for consecutive_lates in range(3):
                    dp_next_state[total_absences][0] = (
                        dp_next_state[total_absences][0] +
                        dp_curr_state[total_absences][consecutive_lates]
                    ) % MOD
                    if total_absences < 1:
                        dp_next_state[total_absences + 1][0] = (
                            dp_next_state[total_absences + 1][0] +
                            dp_curr_state[total_absences][consecutive_lates]
                        ) % MOD
                    if consecutive_lates < 2:
                        dp_next_state[total_absences][consecutive_lates + 1] = (
                            dp_next_state[total_absences][consecutive_lates + 1] +
                            dp_curr_state[total_absences][consecutive_lates]
                        ) % MOD
            dp_curr_state = [row[:] for row in dp_next_state]
            dp_next_state = [[0] * 3 for _ in range(2)]
        count = sum(dp_curr_state[total_absences][consecutive_lates] \
                    for total_absences in range(2) \
                    for consecutive_lates in range(3)) % MOD
        return count

