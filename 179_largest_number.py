'''
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
'''

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = map(str, nums)
        sorted_str_nums = sorted(str_nums, key=LargerNumKey)
        largest_num = ''.join(sorted_str_nums)
        
        return '0' if largest_num[0] == '0' else largest_num
        
