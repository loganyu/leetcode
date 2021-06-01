'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

Example:

Input: low = "50", high = "100"
Output: 3 
Explanation: 69, 88, and 96 are three strobogrammatic numbers.
Note:
Because the range might be a large number, the low and high numbers are represented as string.
'''

class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        mapping = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6",
        }
        low_len = len(low)
        high_len = len(high)
        queue = ["", "0", "1", "8"]
        count = 0
        while queue:
            num = queue.pop()
            if len(num) < high_len or len(num) == high_len and num <= high: 
                if len(num) > low_len or len(num) == low_len and num >= low:
                    if num == "0" or not num.startswith("0"):
                        count += 1
                if high_len - len(num) >= 2:
                    for start, end in mapping.items():
                        next_num = f"{start}{num}{end}"
                        queue.append(next_num)
        
        return count

