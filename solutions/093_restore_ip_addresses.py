'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address consists of exactly four integers (each integer is between 0 and 255) separated by single points.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
'''

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def valid(segment):
            if segment[0] == '0':
                return len(segment) == 1
            return int(segment) <= 255
        
        def recurse(start):
            for end in range(start+1, min(start + 4, n)):
                segment = s[start:end]
                if valid(segment):
                    segments.append(segment)
                    if len(segments) == 3:
                        if valid(s[end:n]):
                            segments.append(s[end:n])
                            output.append(".".join(segments))
                            segments.pop()
                    else:
                        recurse(end)
                    segments.pop()
            
        
        output = []
        segments = []
        n = len(s)
        recurse(0)
        
        return output
        
