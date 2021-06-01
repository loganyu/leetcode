'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]
'''

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        return self.helper(n, n)

    def helper(self, length, n):
        if length == 0:
            return [""]
        if length == 1:
            return ["0", "1", "8"]
        
        nums = self.helper(length - 2, n)
        ans = []
        for i in range(len(nums)):
            if length != n:
                ans.append(f"0{nums[i]}0")
            ans.append(f"1{nums[i]}1")
            ans.append(f"6{nums[i]}9")
            ans.append(f"8{nums[i]}8")
            ans.append(f"9{nums[i]}6")
        
        return ans

