'''
We know that 4 and 7 are lucky digits. Also, a number is called lucky if it contains only lucky digits.

You are given an integer k, return the kth lucky number represented as a string.



Example 1:

Input: k = 4
Output: "47"
Explanation: The first lucky number is 4, the second one is 7, the third one is 44 and the fourth one is 47.
Example 2:

Input: k = 10
Output: "477"
Explanation: Here are lucky numbers sorted in increasing order:
4, 7, 44, 47, 74, 77, 444, 447, 474, 477. So the 10th lucky number is 477.
Example 3:

Input: k = 1000
Output: "777747447"
Explanation: It can be shown that the 1000th lucky number is 777747447.


Constraints:

1 <= k <= 109
'''

class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        k = k + 1
        kth_lucky_num = bin(k)[3:]
        kth_lucky_num = kth_lucky_num.replace("0", "4").replace("1", "7")

        return kth_lucky_num

